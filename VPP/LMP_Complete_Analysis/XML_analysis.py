import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from datetime import datetime

class TimePoint:
    def __init__(self, interval_num, interval_start_gmt, interval_end_gmt, price=None, congestion=None, emission=None, loss=None):
        self.interval_num = interval_num
        self.interval_start_gmt = interval_start_gmt
        self.interval_end_gmt = interval_end_gmt
        self.price = price
        self.congestion = congestion
        self.emission = emission
        self.loss = loss

    def __repr__(self):
        return (f"TimePoint(interval_num={self.interval_num}, "
                f"start={self.interval_start_gmt}, "
                f"end={self.interval_end_gmt}, "
                f"price={self.price}, congestion={self.congestion}, "
                f"emission={self.emission}, loss={self.loss})")

class Node: #Node, as in DER resource
    def __init__(self, resource_name):
        self.resource_name = resource_name
        self.time_points = {} # Key: interval_num (indexed by interval num), Value: TimePoint object

    def add_time_point(self, time_point):
        self.time_points[time_point.interval_num] = time_point

    def get_parameter_values(self, parameter):
        values = []
        time_labels = []
        sorted_intervals = sorted(self.time_points.keys())

        for interval in sorted_intervals:
            time_point = self.time_points[interval]
            time_labels.append(time_point.interval_start_gmt)

            if parameter == "price":
                values.append(time_point.price)
            elif parameter == "congestion":
                values.append(time_point.congestion)
            elif parameter == "emission":
                values.append(time_point.emission)
            elif parameter == "loss":
                values.append(time_point.loss)
            else:
                raise ValueError("not one of four parameters")

        return time_labels, values

    def plot_parameter(self, parameter): # given a parameter, plot it out for node
        time_labels, values = self.get_parameter_values(parameter)
        time_values = [datetime.fromisoformat(t[:-6]) for t in time_labels] # cleaning

        plt.figure(figsize=(12, 6))
        plt.plot(time_values, values, marker='o')

        plt.xlabel("Time (GMT)")
        plt.ylabel(parameter.capitalize())
        plt.title(f"{self.resource_name} - {parameter.capitalize()}")

        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()

    def __repr__(self):
        return f"Node(resource_name={self.resource_name}), time_points={self.time_points.keys()}"

def parse_xml_data(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Define the XML namespace
    ns = {'caiso': 'http://www.caiso.com/soa/OASISReport_v12.xsd'}  # Use the correct namespace URI

    nodes = {}

    # Use namespace-aware findall()
    for report_item in root.findall(".//caiso:REPORT_ITEM", namespaces=ns):  # Double dot

        for report_data in report_item.findall(".//caiso:REPORT_DATA", namespaces=ns):  # Double dot
            resource_name = report_data.find("caiso:RESOURCE_NAME", namespaces=ns).text
            opr_date = report_data.find("caiso:OPR_DATE", namespaces=ns).text
            interval_num = int(report_data.find("caiso:INTERVAL_NUM", namespaces=ns).text)
            interval_start_gmt = report_data.find("caiso:INTERVAL_START_GMT", namespaces=ns).text
            interval_end_gmt = report_data.find("caiso:INTERVAL_END_GMT", namespaces=ns).text
            data_item_element = report_data.find("caiso:DATA_ITEM", namespaces=ns) # find, but don't assume
            value = float(report_data.find("caiso:VALUE",  namespaces=ns).text)

            if resource_name not in nodes:
                nodes[resource_name] = Node(resource_name)

            node = nodes[resource_name]

            # Create the TimePoint object (only once)
            if interval_num not in node.time_points:
                time_point = TimePoint(interval_num, interval_start_gmt, interval_end_gmt)
                node.add_time_point(time_point)
            else:
                time_point = node.time_points[interval_num]

            # Assign to relevant
            if data_item_element is not None:
                data_item = data_item_element.text  # Safely get the text
                if data_item == "LMP_PRC":
                    time_point.price = value
                elif data_item == "LMP_CONG_PRC":
                    time_point.congestion = value
                elif data_item == "LMP_ENE_PRC":
                    time_point.emission = value
                elif data_item == "LMP_LOSS_PRC":
                    time_point.loss = value

    return nodes

### Instantiate file
xml_file = "JanFeb.xml"
nodes = parse_xml_data(xml_file)
node_list = list(nodes.keys())


# Debugging:
print(f"Number of nodes created: {len(nodes)}")
print("List of all nodes:", node_list)

#Example
if 'AFPR_1_TOT_GEN-APND' in nodes:
    print("Node AFPR_1_TOT_GEN-APND exists!")
    node = nodes['AFPR_1_TOT_GEN-APND']
    print(f"Number of time points in this node: {len(node.time_points)}")
    if node.time_points: # Check if there are any timepoints
        first_interval = next(iter(node.time_points)) #Get the first interval
        print(f"Data in first interval: {node.time_points[first_interval]}") #print out all the datapoints
else:
    print("Node AFPR_1_TOT_GEN-APND does not exist.")

for node_name, node in nodes.items():
    print(f"Plotting price for node: {node_name}") #See if the loop is reached
    node.plot_parameter("loss")  # Or 'congestion', 'emission', 'loss'
