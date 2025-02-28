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
    nodes = {}

    for report_item in root.findall("REPORT_ITEM"):
        for report_data in report_item.findall("REPORT_DATA"):
            resource_name = report_data.find("RESOURCE_NAME").text
            opr_date = report_data.find("OPR_DATE").text
            interval_num = report_data.find("INTERVAL_NUM").text
            interval_start_gmt = report_data.find("INTERVAL_START_GMT").text
            data_item = report_data.find("DATA_ITEM")
            value = float(report_data.find("VALUE").text)

            if resource_name not in nodes:
                nodes[resource_name] = Node(resource_name)

            node = nodes[resource_name]

            if interval_num not in node.time_points:
                time_point = TimePoint(interval_num, interval_start_gmt)
                node.add_time_point(time_point)
            else:
                time_point = node.time_points[interval_num]

            if data_item == "LMP_PRC":
                time_point.price = value
            elif data_item == "LMP_CONG_PRC":
                time_point.price = value
            elif data_item == "LMP_ENE_PRC":
                time_point.congestion = value
            elif data_item == "LMP_LOSS_PRC":
                time_point.loss = value

    return nodes

### Instantiate file

xml_file = "JanFeb.xml"
nodes = parse_xml_data(xml_file)

for resource_name, node in nodes.items():
    print(f"Node: {node.resource_name}")
    for interval_num, time_point in node.time_points.items():
        print(f"Interval {interval_num}: {time_point}")

if nodes:
    first_node_name = next(iter(nodes))
    nodes[first_node_name].plot_parameter("LMP_PRC")