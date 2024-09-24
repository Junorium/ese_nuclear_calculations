# written by Hamza

import numpy as np
import matplotlib.pyplot as plt
import math

# from pyne import ace
'''
import pyne
#from pyne.xs.data_source import EAFDataSource, SimpleDataSource, NullDataSource

sds = SimpleDataSource(dst_group_struct=dst_e_g)
print(sds.exists)
rx = sds.reaction('U233', 'absorption') # cross section data

console.log(rx)
'''

# 0-.025 eV
# .025-.1eV
# .1-1   eV
# 1-100  eV
# .1-10 keV
# .01-1 MeV
# 1-5   MeV
# 5     MeV


numberofmeshes = 160
n = numberofmeshes

diameterreactorcore = 193  # 95.8*2.54 # cm
heightreactorcore = 97.5 * 2.54  # cm
diameterreflector = 193 + (25 * 2.54)  # 120*2.54 # cm
heightreflector = 120.5 * 2.54  # cm

uraniumenrichment = .09  # atompercent
# 0-.025 eV
# .025-.1eV
# .1-1   eV
# 1-100  eV
# .1-10 keV
# .01-1 MeV
# 1-5   MeV
# 5     MeV

chi1 = .054046
chi2 = .64135853
chi3 = .3094253
chi4 = .00045638
chi5 = 0
chi6 = 0
chi7 = 0
chi8 = 0

secondspermonth = 60 * 60 * 24 * 30.4375
secondsperyear = 60 * 60 * 24 * 365.25

timeperiteration = secondsperyear

u235f = [600, 250, 95, 20, 7, 1.7, 1, 1]  # b
u235a = [700, 310, 105, 40, 9, 2, 1.005, 1.001]  # b
# u235a = [100,60,10,20,2,.3  ,.005,.001]  #b
u238f = [10 ** (-4.5), 10 ** (-4.5), 10 ** (-4.5), 10 ** (-4.5), 10 ** (-6), 10 ** (-3), .8, 1]  # b
u238a = [4, 1.9, .97, 12, .2, .1, .801, 1.00001]  # b
# u238a = [4       ,1.9     ,.97     ,12      ,.2    ,.1    ,.801,1.00001]  #b

pu239f = [1000, 700, 600, 20, 5, 1.5, 1.6, 1.8]  # b
pu239c = [1300, 900, 950, 40, 8, 1.8, 1.606, 1.8007]  # b

u235s = [10, 9.5, 9, 7.7, 6.3, 5, 4.5, 4]  # b
u238s = [9, 8.5, 8, 7, 6, 5, 5.5, 5]  # b
pu239s = [9, 8.5, 8, 7, 6, 5, 5.5, 5]  # b

zr90a = [.1, .09, .03, .008, .0003, .04, .01, .001]  # b
zr90s = [1, 1, 1, 1, 1, 1, 1, 1]  # b

ha = [1, .25, .1, .02, .002, .0001, .00004, .00004]  # b
hs = [30, 20, 20, 20, 20, 10, 5, 1]  # b

oa = [.0001, .0001, .00001, .000001, .0000001, .00000009, .00000003, .00000003]  # b
os = [4, 4, 4, 4, 4, 3, 2, 1]  # b

bea = [.002, .002, .002, .001, .0005, .0001, .00001, .00001]  # b
bes = [5, 4.9, 4.8, 4.5, 3.5, 2.5, 2.1, 2]  # b

kaxialarray = [1]
kradialarray = [1]
timearray = [0]

u235ebar = .9915
u238ebar = .9916
pu239ebar = .9917
zr90ebar = .9785
hebar = .5
oebar = .88927
# beebar = .82
cebar = .858
beebar = cebar

energyperU235fission = 193.7  # MeV

NA = 6.022 * (10 ** 23)

neutronsperfissionU235 = 2.435
neutronsperfissionU238 = 2.819
neutronsperfissionPu239 = 2.88
ratiopu239u238 = 0

densityuo2fuel = 10.97  # g/cm^3
densitywater = 1.3  # g/cm^3
densitycladding = 6.56  # g/cm^3
densityreflector = 2.26  # g/cm^3

numberofassemblies = 45
assemblyfuelrods = 164
fuelradius = .500385  # cm
claddinginnerradius = .51  # cm
claddingoutterradius = .57  # cm

volumecore = heightreactorcore * 3.1415 * ((diameterreactorcore / 2) ** 2)  # cm^3
volumeuo2fuel = numberofassemblies * assemblyfuelrods * 3.1415 * (fuelradius ** 2) * heightreactorcore  # cm^3
volumecladding = numberofassemblies * assemblyfuelrods * 3.1415 * (
            (claddingoutterradius ** 2) - (claddinginnerradius ** 2)) * heightreactorcore  # cm^3
volumeh2o = volumecore - (
            (claddingoutterradius ** 2) * 3.1415 * numberofassemblies * assemblyfuelrods * heightreactorcore)  # cm^3

numberdensityuo2fuel = ((densityuo2fuel * NA) / (
            ((235.0409 * uraniumenrichment) + (238.0507 * (1 - uraniumenrichment))) + 16 + 16)) * (
                                   volumeuo2fuel / volumecore)
numberdensitycladding = ((densitycladding * NA) / (91)) * (volumecladding / volumecore)
numberdensitywater = ((densitywater * NA) / (18)) * (volumeh2o / volumecore)
numberdensityreflector = ((densityreflector * NA) / (12))

numberdensityu235local = numberdensityuo2fuel * uraniumenrichment
numberdensityu238local = numberdensityuo2fuel * (1 - uraniumenrichment) * (1 - ratiopu239u238)
numberdensitypu239local = numberdensityuo2fuel * (1 - uraniumenrichment) * ratiopu239u238

g154c = [100, 60, 2.2, 20, 3, .6, .5, .4]  # b .0218
g155c = [.9 * (10 ** 5), 4 * (10 ** 4), 7 * (10 ** 2), 100, 10, 1.3, .2, .15]  # b .1480
g156c = [2, 1.5, .6, 1, 2, .3, .5, .5]  # b .2047
g157c = [3.3 * (10 ** 5), 2 * (10 ** 5), 3 * (10 ** 3), 90, 5, .6, .1, .09]  # b .1565
g158c = [2.5, 1.8, .7, .7, 1, .3, .3, .3]  # b .2484
g160c = [2, 1.3, .4, .1, 1, .2, .04, .04]  # b .2186

densitygadolinium = 0  # g/cm^3

numberdensitygadolinium = ((densitygadolinium * NA) / 157.5)

numberdensitylocalg154 = numberdensitygadolinium * .0218

numberdensitylocalg155 = numberdensitygadolinium * .1480

numberdensitylocalg156 = numberdensitygadolinium * .2047

numberdensitylocalg157 = numberdensitygadolinium * .1565

numberdensitylocalg158 = numberdensitygadolinium * .2484

numberdensitylocalg160 = numberdensitygadolinium * .2186

numberdensityu235 = []
numberdensityu238 = []
numberdensitypu239 = []

numberdensityg154 = []
numberdensityg155 = []
numberdensityg156 = []
numberdensityg157 = []
numberdensityg158 = []
numberdensityg160 = []

deltax = heightreflector / (n * 2)
deltar = diameterreflector / (n * 2)

for i in range(math.ceil(n * (heightreactorcore / heightreflector))):
    numberdensityu235.append([])
    numberdensityu238.append([])
    numberdensitypu239.append([])
    numberdensityg154.append([])
    numberdensityg155.append([])
    numberdensityg156.append([])
    numberdensityg157.append([])
    numberdensityg158.append([])
    numberdensityg160.append([])
    for j in range(math.ceil(n * (diameterreactorcore / diameterreflector))):
        numberdensityu235[i].append(numberdensityu235local)
        numberdensityu238[i].append(numberdensityu238local)
        numberdensitypu239[i].append(numberdensitypu239local)
        '''
        numberdensityg154[i].append(numberdensitylocalg154 + (numberdensitylocalg154 * .2 * math.cos(  (i * deltax * (3.1415/2))/(heightreactorcore/2)     ) * math.cos(   (j * deltar * (3.1415/2))/(diameterreactorcore/2)       )))
        numberdensityg155[i].append(numberdensitylocalg155 + (numberdensitylocalg155 * .2 * math.cos(  (i * deltax * (3.1415/2))/(heightreactorcore/2)     ) * math.cos(   (j * deltar * (3.1415/2))/(diameterreactorcore/2)       )))
        numberdensityg156[i].append(numberdensitylocalg156 + (numberdensitylocalg156 * .2 * math.cos(  (i * deltax * (3.1415/2))/(heightreactorcore/2)     ) * math.cos(   (j * deltar * (3.1415/2))/(diameterreactorcore/2)       )))
        numberdensityg157[i].append(numberdensitylocalg157 + (numberdensitylocalg157 * .2 * math.cos(  (i * deltax * (3.1415/2))/(heightreactorcore/2)     ) * math.cos(   (j * deltar * (3.1415/2))/(diameterreactorcore/2)       )))
        numberdensityg158[i].append(numberdensitylocalg158 + (numberdensitylocalg158 * .2 * math.cos(  (i * deltax * (3.1415/2))/(heightreactorcore/2)     ) * math.cos(   (j * deltar * (3.1415/2))/(diameterreactorcore/2)       )))
        numberdensityg160[i].append(numberdensitylocalg160 + (numberdensitylocalg160 * .2 * math.cos(  (i * deltax * (3.1415/2))/(heightreactorcore/2)     ) * math.cos(   (j * deltar * (3.1415/2))/(diameterreactorcore/2)       )))          
        '''
        numberdensityg154[i].append(numberdensitylocalg154)
        numberdensityg155[i].append(numberdensitylocalg155)
        numberdensityg156[i].append(numberdensitylocalg156)
        numberdensityg157[i].append(numberdensitylocalg157)
        numberdensityg158[i].append(numberdensitylocalg158)
        numberdensityg160[i].append(numberdensitylocalg160)

averageindexradius = round(n * (diameterreactorcore / diameterreflector) * (2 / 3.1415))
averageindexaxial = round(n * (heightreactorcore / heightreflector) * (2 / 3.1415))

for w in range(1):

    nugroup1fission = []
    nugroup2fission = []
    nugroup3fission = []
    nugroup4fission = []
    nugroup5fission = []
    nugroup6fission = []
    nugroup7fission = []
    nugroup8fission = []

    group1fission1 = []
    group2fission2 = []
    group3fission3 = []
    group4fission4 = []
    group5fission5 = []
    group6fission6 = []
    group7fission7 = []
    group8fission8 = []

    group1absorptioncore = []
    group2absorptioncore = []
    group3absorptioncore = []
    group4absorptioncore = []
    group5absorptioncore = []
    group6absorptioncore = []
    group7absorptioncore = []
    group8absorptioncore = []

    for i in range(math.ceil(n * (heightreactorcore / heightreflector))):
        nugroup1fission.append([])
        nugroup2fission.append([])
        nugroup3fission.append([])
        nugroup4fission.append([])
        nugroup5fission.append([])
        nugroup6fission.append([])
        nugroup7fission.append([])
        nugroup8fission.append([])

        group1fission1.append([])
        group2fission2.append([])
        group3fission3.append([])
        group4fission4.append([])
        group5fission5.append([])
        group6fission6.append([])
        group7fission7.append([])
        group8fission8.append([])

        group1absorptioncore.append([])
        group2absorptioncore.append([])
        group3absorptioncore.append([])
        group4absorptioncore.append([])
        group5absorptioncore.append([])
        group6absorptioncore.append([])
        group7absorptioncore.append([])
        group8absorptioncore.append([])
        for j in range(math.ceil(n * (diameterreactorcore / diameterreflector))):
            nugroup1fission[i].append((neutronsperfissionU235 * numberdensityu235[i][j] * (10 ** -24) * u235f[7]) + (
                        neutronsperfissionU238 * numberdensityu238[i][j] * (10 ** -24) * u238f[7]) + (
                                                  neutronsperfissionPu239 * numberdensitypu239[i][j] * (10 ** -24) *
                                                  pu239f[7]))
            nugroup2fission[i].append((neutronsperfissionU235 * numberdensityu235[i][j] * (10 ** -24) * u235f[6]) + (
                        neutronsperfissionU238 * numberdensityu238[i][j] * (10 ** -24) * u238f[6]) + (
                                                  neutronsperfissionPu239 * numberdensitypu239[i][j] * (10 ** -24) *
                                                  pu239f[6]))
            nugroup3fission[i].append((neutronsperfissionU235 * numberdensityu235[i][j] * (10 ** -24) * u235f[5]) + (
                        neutronsperfissionU238 * numberdensityu238[i][j] * (10 ** -24) * u238f[5]) + (
                                                  neutronsperfissionPu239 * numberdensitypu239[i][j] * (10 ** -24) *
                                                  pu239f[5]))
            nugroup4fission[i].append((neutronsperfissionU235 * numberdensityu235[i][j] * (10 ** -24) * u235f[4]) + (
                        neutronsperfissionU238 * numberdensityu238[i][j] * (10 ** -24) * u238f[4]) + (
                                                  neutronsperfissionPu239 * numberdensitypu239[i][j] * (10 ** -24) *
                                                  pu239f[4]))
            nugroup5fission[i].append((neutronsperfissionU235 * numberdensityu235[i][j] * (10 ** -24) * u235f[3]) + (
                        neutronsperfissionU238 * numberdensityu238[i][j] * (10 ** -24) * u238f[3]) + (
                                                  neutronsperfissionPu239 * numberdensitypu239[i][j] * (10 ** -24) *
                                                  pu239f[3]))
            nugroup6fission[i].append((neutronsperfissionU235 * numberdensityu235[i][j] * (10 ** -24) * u235f[2]) + (
                        neutronsperfissionU238 * numberdensityu238[i][j] * (10 ** -24) * u238f[2]) + (
                                                  neutronsperfissionPu239 * numberdensitypu239[i][j] * (10 ** -24) *
                                                  pu239f[2]))
            nugroup7fission[i].append((neutronsperfissionU235 * numberdensityu235[i][j] * (10 ** -24) * u235f[1]) + (
                        neutronsperfissionU238 * numberdensityu238[i][j] * (10 ** -24) * u238f[1]) + (
                                                  neutronsperfissionPu239 * numberdensitypu239[i][j] * (10 ** -24) *
                                                  pu239f[1]))
            nugroup8fission[i].append((neutronsperfissionU235 * numberdensityu235[i][j] * (10 ** -24) * u235f[0]) + (
                        neutronsperfissionU238 * numberdensityu238[i][j] * (10 ** -24) * u238f[0]) + (
                                                  neutronsperfissionPu239 * numberdensitypu239[i][j] * (10 ** -24) *
                                                  pu239f[0]))

            group1fission1[i].append((numberdensityu235[i][j] * (10 ** -24) * u235f[7]) + (
                        numberdensityu238[i][j] * (10 ** -24) * u238f[7]) + (
                                                 numberdensitypu239[i][j] * (10 ** -24) * pu239f[7]))
            group2fission2[i].append((numberdensityu235[i][j] * (10 ** -24) * u235f[6]) + (
                        numberdensityu238[i][j] * (10 ** -24) * u238f[6]) + (
                                                 numberdensitypu239[i][j] * (10 ** -24) * pu239f[6]))
            group3fission3[i].append((numberdensityu235[i][j] * (10 ** -24) * u235f[5]) + (
                        numberdensityu238[i][j] * (10 ** -24) * u238f[5]) + (
                                                 numberdensitypu239[i][j] * (10 ** -24) * pu239f[5]))
            group4fission4[i].append((numberdensityu235[i][j] * (10 ** -24) * u235f[4]) + (
                        numberdensityu238[i][j] * (10 ** -24) * u238f[4]) + (
                                                 numberdensitypu239[i][j] * (10 ** -24) * pu239f[4]))
            group5fission5[i].append((numberdensityu235[i][j] * (10 ** -24) * u235f[3]) + (
                        numberdensityu238[i][j] * (10 ** -24) * u238f[3]) + (
                                                 numberdensitypu239[i][j] * (10 ** -24) * pu239f[3]))
            group6fission6[i].append((numberdensityu235[i][j] * (10 ** -24) * u235f[2]) + (
                        numberdensityu238[i][j] * (10 ** -24) * u238f[2]) + (
                                                 numberdensitypu239[i][j] * (10 ** -24) * pu239f[2]))
            group7fission7[i].append((numberdensityu235[i][j] * (10 ** -24) * u235f[1]) + (
                        numberdensityu238[i][j] * (10 ** -24) * u238f[1]) + (
                                                 numberdensitypu239[i][j] * (10 ** -24) * pu239f[1]))
            group8fission8[i].append((numberdensityu235[i][j] * (10 ** -24) * u235f[0]) + (
                        numberdensityu238[i][j] * (10 ** -24) * u238f[0]) + (
                                                 numberdensitypu239[i][j] * (10 ** -24) * pu239f[0]))

            group1absorptioncore[i].append((numberdensityu235[i][j] * (10 ** -24) * u235a[7]) + (
                        numberdensityu238[i][j] * (10 ** -24) * u238a[7]) + (
                                                       numberdensitypu239[i][j] * (10 ** -24) * pu239c[7]) + (
                                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) *
                                                       oa[7]) + (((numberdensitywater * 2)) * (10 ** -24) * ha[7]) + (
                                                       numberdensitycladding * (10 ** -24) * zr90a[7]) + (
                                                       numberdensityg154[i][j] * (10 ** -24) * g154c[7]) + (
                                                       numberdensityg155[i][j] * (10 ** -24) * g155c[7]) + (
                                                       numberdensityg156[i][j] * (10 ** -24) * g156c[7]) + (
                                                       numberdensityg157[i][j] * (10 ** -24) * g157c[7]) + (
                                                       numberdensityg158[i][j] * (10 ** -24) * g158c[7]) + (
                                                       numberdensityg160[i][j] * (10 ** -24) * g160c[7]))
            group2absorptioncore[i].append((numberdensityu235[i][j] * (10 ** -24) * u235a[6]) + (
                        numberdensityu238[i][j] * (10 ** -24) * u238a[6]) + (
                                                       numberdensitypu239[i][j] * (10 ** -24) * pu239c[6]) + (
                                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) *
                                                       oa[6]) + (((numberdensitywater * 2)) * (10 ** -24) * ha[6]) + (
                                                       numberdensitycladding * (10 ** -24) * zr90a[6]) + (
                                                       numberdensityg154[i][j] * (10 ** -24) * g154c[6]) + (
                                                       numberdensityg155[i][j] * (10 ** -24) * g155c[6]) + (
                                                       numberdensityg156[i][j] * (10 ** -24) * g156c[6]) + (
                                                       numberdensityg157[i][j] * (10 ** -24) * g157c[6]) + (
                                                       numberdensityg158[i][j] * (10 ** -24) * g158c[6]) + (
                                                       numberdensityg160[i][j] * (10 ** -24) * g160c[6]))
            group3absorptioncore[i].append((numberdensityu235[i][j] * (10 ** -24) * u235a[5]) + (
                        numberdensityu238[i][j] * (10 ** -24) * u238a[5]) + (
                                                       numberdensitypu239[i][j] * (10 ** -24) * pu239c[5]) + (
                                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) *
                                                       oa[5]) + (((numberdensitywater * 2)) * (10 ** -24) * ha[5]) + (
                                                       numberdensitycladding * (10 ** -24) * zr90a[5]) + (
                                                       numberdensityg154[i][j] * (10 ** -24) * g154c[5]) + (
                                                       numberdensityg155[i][j] * (10 ** -24) * g155c[5]) + (
                                                       numberdensityg156[i][j] * (10 ** -24) * g156c[5]) + (
                                                       numberdensityg157[i][j] * (10 ** -24) * g157c[5]) + (
                                                       numberdensityg158[i][j] * (10 ** -24) * g158c[5]) + (
                                                       numberdensityg160[i][j] * (10 ** -24) * g160c[5]))
            group4absorptioncore[i].append((numberdensityu235[i][j] * (10 ** -24) * u235a[4]) + (
                        numberdensityu238[i][j] * (10 ** -24) * u238a[4]) + (
                                                       numberdensitypu239[i][j] * (10 ** -24) * pu239c[4]) + (
                                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) *
                                                       oa[4]) + (((numberdensitywater * 2)) * (10 ** -24) * ha[4]) + (
                                                       numberdensitycladding * (10 ** -24) * zr90a[4]) + (
                                                       numberdensityg154[i][j] * (10 ** -24) * g154c[4]) + (
                                                       numberdensityg155[i][j] * (10 ** -24) * g155c[4]) + (
                                                       numberdensityg156[i][j] * (10 ** -24) * g156c[4]) + (
                                                       numberdensityg157[i][j] * (10 ** -24) * g157c[4]) + (
                                                       numberdensityg158[i][j] * (10 ** -24) * g158c[4]) + (
                                                       numberdensityg160[i][j] * (10 ** -24) * g160c[4]))
            group5absorptioncore[i].append((numberdensityu235[i][j] * (10 ** -24) * u235a[3]) + (
                        numberdensityu238[i][j] * (10 ** -24) * u238a[3]) + (
                                                       numberdensitypu239[i][j] * (10 ** -24) * pu239c[3]) + (
                                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) *
                                                       oa[3]) + (((numberdensitywater * 2)) * (10 ** -24) * ha[3]) + (
                                                       numberdensitycladding * (10 ** -24) * zr90a[3]) + (
                                                       numberdensityg154[i][j] * (10 ** -24) * g154c[3]) + (
                                                       numberdensityg155[i][j] * (10 ** -24) * g155c[3]) + (
                                                       numberdensityg156[i][j] * (10 ** -24) * g156c[3]) + (
                                                       numberdensityg157[i][j] * (10 ** -24) * g157c[3]) + (
                                                       numberdensityg158[i][j] * (10 ** -24) * g158c[3]) + (
                                                       numberdensityg160[i][j] * (10 ** -24) * g160c[3]))
            group6absorptioncore[i].append((numberdensityu235[i][j] * (10 ** -24) * u235a[2]) + (
                        numberdensityu238[i][j] * (10 ** -24) * u238a[2]) + (
                                                       numberdensitypu239[i][j] * (10 ** -24) * pu239c[2]) + (
                                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) *
                                                       oa[2]) + (((numberdensitywater * 2)) * (10 ** -24) * ha[2]) + (
                                                       numberdensitycladding * (10 ** -24) * zr90a[2]) + (
                                                       numberdensityg154[i][j] * (10 ** -24) * g154c[2]) + (
                                                       numberdensityg155[i][j] * (10 ** -24) * g155c[2]) + (
                                                       numberdensityg156[i][j] * (10 ** -24) * g156c[2]) + (
                                                       numberdensityg157[i][j] * (10 ** -24) * g157c[2]) + (
                                                       numberdensityg158[i][j] * (10 ** -24) * g158c[2]) + (
                                                       numberdensityg160[i][j] * (10 ** -24) * g160c[2]))
            group7absorptioncore[i].append((numberdensityu235[i][j] * (10 ** -24) * u235a[1]) + (
                        numberdensityu238[i][j] * (10 ** -24) * u238a[1]) + (
                                                       numberdensitypu239[i][j] * (10 ** -24) * pu239c[1]) + (
                                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) *
                                                       oa[1]) + (((numberdensitywater * 2)) * (10 ** -24) * ha[1]) + (
                                                       numberdensitycladding * (10 ** -24) * zr90a[1]) + (
                                                       numberdensityg154[i][j] * (10 ** -24) * g154c[1]) + (
                                                       numberdensityg155[i][j] * (10 ** -24) * g155c[1]) + (
                                                       numberdensityg156[i][j] * (10 ** -24) * g156c[1]) + (
                                                       numberdensityg157[i][j] * (10 ** -24) * g157c[1]) + (
                                                       numberdensityg158[i][j] * (10 ** -24) * g158c[1]) + (
                                                       numberdensityg160[i][j] * (10 ** -24) * g160c[1]))
            group8absorptioncore[i].append((numberdensityu235[i][j] * (10 ** -24) * u235a[0]) + (
                        numberdensityu238[i][j] * (10 ** -24) * u238a[0]) + (
                                                       numberdensitypu239[i][j] * (10 ** -24) * pu239c[0]) + (
                                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) *
                                                       oa[0]) + (((numberdensitywater * 2)) * (10 ** -24) * ha[0]) + (
                                                       numberdensitycladding * (10 ** -24) * zr90a[0]) + (
                                                       numberdensityg154[i][j] * (10 ** -24) * g154c[0]) + (
                                                       numberdensityg155[i][j] * (10 ** -24) * g155c[0]) + (
                                                       numberdensityg156[i][j] * (10 ** -24) * g156c[0]) + (
                                                       numberdensityg157[i][j] * (10 ** -24) * g157c[0]) + (
                                                       numberdensityg158[i][j] * (10 ** -24) * g158c[0]) + (
                                                       numberdensityg160[i][j] * (10 ** -24) * g160c[0]))

    '''
    nugroup1fission = (neutronsperfissionU235 * numberdensityu235[i][j] * (10**-24) * u235f[7]) + (neutronsperfissionU238 * numberdensityu238[i][j] * (10**-24) * u238f[7]) + (neutronsperfissionPu239 * numberdensitypu239[i][j] * (10**-24) * pu239f[7])
    nugroup2fission = (neutronsperfissionU235 * numberdensityu235[i][j] * (10**-24) * u235f[6]) + (neutronsperfissionU238 * numberdensityu238[i][j] * (10**-24) * u238f[6]) + (neutronsperfissionPu239 * numberdensitypu239[i][j] * (10**-24) * pu239f[6])
    nugroup3fission = (neutronsperfissionU235 * numberdensityu235[i][j] * (10**-24) * u235f[5]) + (neutronsperfissionU238 * numberdensityu238[i][j] * (10**-24) * u238f[5]) + (neutronsperfissionPu239 * numberdensitypu239[i][j] * (10**-24) * pu239f[5])
    nugroup4fission = (neutronsperfissionU235 * numberdensityu235[i][j] * (10**-24) * u235f[4]) + (neutronsperfissionU238 * numberdensityu238[i][j] * (10**-24) * u238f[4]) + (neutronsperfissionPu239 * numberdensitypu239[i][j] * (10**-24) * pu239f[4])
    nugroup5fission = (neutronsperfissionU235 * numberdensityu235[i][j] * (10**-24) * u235f[3]) + (neutronsperfissionU238 * numberdensityu238[i][j] * (10**-24) * u238f[3]) + (neutronsperfissionPu239 * numberdensitypu239[i][j] * (10**-24) * pu239f[3])
    nugroup6fission = (neutronsperfissionU235 * numberdensityu235[i][j] * (10**-24) * u235f[2]) + (neutronsperfissionU238 * numberdensityu238[i][j] * (10**-24) * u238f[2]) + (neutronsperfissionPu239 * numberdensitypu239[i][j] * (10**-24) * pu239f[2])
    nugroup7fission = (neutronsperfissionU235 * numberdensityu235[i][j] * (10**-24) * u235f[1]) + (neutronsperfissionU238 * numberdensityu238[i][j] * (10**-24) * u238f[1]) + (neutronsperfissionPu239 * numberdensitypu239[i][j] * (10**-24) * pu239f[1])
    nugroup8fission = (neutronsperfissionU235 * numberdensityu235[i][j] * (10**-24) * u235f[0]) + (neutronsperfissionU238 * numberdensityu238[i][j] * (10**-24) * u238f[0]) + (neutronsperfissionPu239 * numberdensitypu239[i][j] * (10**-24) * pu239f[0])



    group1fission1 = ( numberdensityu235[i][j] * (10**-24) * u235f[7]) + ( numberdensityu238[i][j] * (10**-24) * u238f[7]) + (numberdensitypu239[i][j] * (10**-24) * pu239f[7])
    group2fission2 = ( numberdensityu235[i][j] * (10**-24) * u235f[6]) + ( numberdensityu238[i][j] * (10**-24) * u238f[6]) + (numberdensitypu239[i][j] * (10**-24) * pu239f[6])
    group3fission3 = ( numberdensityu235[i][j] * (10**-24) * u235f[5]) + ( numberdensityu238[i][j] * (10**-24) * u238f[5]) + (numberdensitypu239[i][j] * (10**-24) * pu239f[5])
    group4fission4 = ( numberdensityu235[i][j] * (10**-24) * u235f[4]) + ( numberdensityu238[i][j] * (10**-24) * u238f[4]) + (numberdensitypu239[i][j] * (10**-24) * pu239f[4])
    group5fission5 = ( numberdensityu235[i][j] * (10**-24) * u235f[3]) + ( numberdensityu238[i][j] * (10**-24) * u238f[3]) + (numberdensitypu239[i][j] * (10**-24) * pu239f[3])
    group6fission6 = ( numberdensityu235[i][j] * (10**-24) * u235f[2]) + ( numberdensityu238[i][j] * (10**-24) * u238f[2]) + (numberdensitypu239[i][j] * (10**-24) * pu239f[2])
    group7fission7 = ( numberdensityu235[i][j] * (10**-24) * u235f[1]) + ( numberdensityu238[i][j] * (10**-24) * u238f[1]) + (numberdensitypu239[i][j] * (10**-24) * pu239f[1])
    group8fission8 = ( numberdensityu235[i][j] * (10**-24) * u235f[0]) + ( numberdensityu238[i][j] * (10**-24) * u238f[0]) + (numberdensitypu239[i][j] * (10**-24) * pu239f[0])
    '''
    # print(nugroup8fission)
    # print(nugroup7fission)
    # print(nugroup6fission)
    # print(nugroup5fission)
    # print(nugroup4fission)
    # print(nugroup3fission)
    # print(nugroup2fission)
    # print(nugroup1fission)

    group1scatteringcore = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[7]) + (
                numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[7]) + (
                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[7]) + (
                                       ((numberdensitywater * 2)) * (10 ** -24) * hs[7]) + (
                                       numberdensitycladding * (10 ** -24) * zr90s[7])

    group1scatteringreflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * hs[7]) + (
                (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * os[7])

    scattering1to2core = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[7] * (
                math.log(u235ebar) / math.log(.44))) + (
                                     numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[7] * (
                                         math.log(u238ebar) / math.log(.44))) + (
                                     (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[7] * (
                                         math.log(oebar) / math.log(.44))) + (
                                     ((numberdensitywater * 2)) * (10 ** -24) * hs[7] * (
                                         math.log(hebar) / math.log(.44))) + (
                                     numberdensitycladding * (10 ** -24) * zr90s[7] * (
                                         math.log(zr90ebar) / math.log(.44)))

    scattering1to2reflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * hs[7] * (
                math.log(hebar) / math.log(.44))) + (
                                          (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * os[7] * (
                                              math.log(oebar) / math.log(.44)))

    # group1absorptioncore = (numberdensityu235 * (10**-24) * u235a[7]) + (numberdensityu238 * (10**-24) * u238a[7]) + (numberdensitypu239 * (10**-24) * pu239c[7]) + ((numberdensitywater + (numberdensityuo2fuel * 2)) * (10**-24) * oa[7]  ) + ( ((numberdensitywater * 2)) * (10**-24) * ha[7]  ) + (numberdensitycladding * (10**-24) * zr90a[7])

    group1absorptionreflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * ha[7]) + (
                (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * oa[7])

    group2scatteringcore = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[6]) + (
                numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[6]) + (
                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[6]) + (
                                       ((numberdensitywater * 2)) * (10 ** -24) * hs[6]) + (
                                       numberdensitycladding * (10 ** -24) * zr90s[6])

    group2scatteringreflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * hs[6]) + (
                (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * os[6])

    scattering2to3core = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[6] * (
                math.log(u235ebar) / math.log(.0363636))) + (
                                     numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[6] * (
                                         math.log(u238ebar) / math.log(.0363636))) + (
                                     (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[6] * (
                                         math.log(oebar) / math.log(.0363636))) + (
                                     ((numberdensitywater * 2)) * (10 ** -24) * hs[6] * (
                                         math.log(hebar) / math.log(.0363636))) + (
                                     numberdensitycladding * (10 ** -24) * zr90s[6] * (
                                         math.log(zr90ebar) / math.log(.0363636)))

    scattering2to3reflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * hs[6] * (
                math.log(hebar) / math.log(.03636))) + (
                                          (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * os[6] * (
                                              math.log(oebar) / math.log(.03636)))

    # group2absorptioncore = (numberdensityu235 * (10**-24) * u235a[6]) + (numberdensityu238 * (10**-24) * u238a[6]) + (numberdensitypu239 * (10**-24) * pu239c[6]) + ((numberdensitywater + (numberdensityuo2fuel * 2)) * (10**-24) * oa[6]  ) + ( ((numberdensitywater * 2)) * (10**-24) * ha[6]  ) + (numberdensitycladding * (10**-24) * zr90a[6])

    group2absorptionreflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * ha[6]) + (
                (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * oa[6])

    group3scatteringcore = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[5]) + (
                numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[5]) + (
                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[5]) + (
                                       ((numberdensitywater * 2)) * (10 ** -24) * hs[5]) + (
                                       numberdensitycladding * (10 ** -24) * zr90s[5])

    group3scatteringreflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * hs[5]) + (
                (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * os[5])

    scattering3to4core = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[5] * (
                math.log(u235ebar) / math.log(.01))) + (
                                     numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[5] * (
                                         math.log(u238ebar) / math.log(.01))) + (
                                     (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[5] * (
                                         math.log(oebar) / math.log(.01))) + (
                                     ((numberdensitywater * 2)) * (10 ** -24) * hs[5] * (
                                         math.log(hebar) / math.log(.01))) + (
                                     numberdensitycladding * (10 ** -24) * zr90s[5] * (
                                         math.log(zr90ebar) / math.log(.01)))

    scattering3to4reflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * hs[5] * (
                math.log(hebar) / math.log(.01))) + (
                                          (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * os[5] * (
                                              math.log(oebar) / math.log(.01)))

    # group3absorptioncore = (numberdensityu235 * (10**-24) * u235a[5]) + (numberdensityu238 * (10**-24) * u238a[5]) + (numberdensitypu239 * (10**-24) * pu239c[5]) + ((numberdensitywater + (numberdensityuo2fuel * 2)) * (10**-24) * oa[5]  ) + ( ((numberdensitywater * 2)) * (10**-24) * ha[5]  ) + (numberdensitycladding * (10**-24) * zr90a[5])

    group3absorptionreflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * ha[5]) + (
                (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * oa[5])

    group4scatteringcore = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[4]) + (
                numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[4]) + (
                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[4]) + (
                                       ((numberdensitywater * 2)) * (10 ** -24) * hs[4]) + (
                                       numberdensitycladding * (10 ** -24) * zr90s[4])

    group4scatteringreflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * hs[4]) + (
                (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * os[4])

    scattering4to5core = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[4] * (
                math.log(u235ebar) / math.log(.01))) + (
                                     numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[4] * (
                                         math.log(u238ebar) / math.log(.01))) + (
                                     (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[4] * (
                                         math.log(oebar) / math.log(.01))) + (
                                     ((numberdensitywater * 2)) * (10 ** -24) * hs[4] * (
                                         math.log(hebar) / math.log(.01))) + (
                                     numberdensitycladding * (10 ** -24) * zr90s[4] * (
                                         math.log(zr90ebar) / math.log(.01)))

    scattering4to5reflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * hs[4] * (
                math.log(hebar) / math.log(.01))) + (
                                          (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * os[4] * (
                                              math.log(oebar) / math.log(.01)))

    # group4absorptioncore = (numberdensityu235 * (10**-24) * u235a[4]) + (numberdensityu238 * (10**-24) * u238a[4]) + (numberdensitypu239 * (10**-24) * pu239c[4]) + ((numberdensitywater + (numberdensityuo2fuel * 2)) * (10**-24) * oa[4]  ) + ( ((numberdensitywater * 2)) * (10**-24) * ha[4]  ) + (numberdensitycladding * (10**-24) * zr90a[4])

    group4absorptionreflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * ha[4]) + (
                (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * oa[4])

    group5scatteringcore = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[3]) + (
                numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[3]) + (
                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[3]) + (
                                       ((numberdensitywater * 2)) * (10 ** -24) * hs[3]) + (
                                       numberdensitycladding * (10 ** -24) * zr90s[3])

    group5scatteringreflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * hs[3]) + (
                (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * os[3])

    scattering5to6core = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[3] * (
                math.log(u235ebar) / math.log(.03083))) + (
                                     numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[3] * (
                                         math.log(u238ebar) / math.log(.03083))) + (
                                     (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[3] * (
                                         math.log(oebar) / math.log(.03083))) + (
                                     ((numberdensitywater * 2)) * (10 ** -24) * hs[3] * (
                                         math.log(hebar) / math.log(.03083))) + (
                                     numberdensitycladding * (10 ** -24) * zr90s[3] * (
                                         math.log(zr90ebar) / math.log(.03083)))

    scattering5to6reflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * hs[3] * (
                math.log(hebar) / math.log(.03083))) + (
                                          (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * os[3] * (
                                              math.log(oebar) / math.log(.03083)))

    # group5absorptioncore = (numberdensityu235 * (10**-24) * u235a[3]) + (numberdensityu238 * (10**-24) * u238a[3]) + (numberdensitypu239 * (10**-24) * pu239c[3]) + ((numberdensitywater + (numberdensityuo2fuel * 2)) * (10**-24) * oa[3]  ) + ( ((numberdensitywater * 2)) * (10**-24) * ha[3]  ) + (numberdensitycladding * (10**-24) * zr90a[3])

    group5absorptionreflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * ha[3]) + (
                (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * oa[3])

    group6scatteringcore = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[2]) + (
                numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[2]) + (
                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[2]) + (
                                       ((numberdensitywater * 2)) * (10 ** -24) * hs[2]) + (
                                       numberdensitycladding * (10 ** -24) * zr90s[2])

    group6scatteringreflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * hs[2]) + (
                (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * os[2])

    scattering6to7core = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[2] * (
                math.log(u235ebar) / math.log(.1))) + (
                                     numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[2] * (
                                         math.log(u238ebar) / math.log(.1))) + (
                                     (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[2] * (
                                         math.log(oebar) / math.log(.1))) + (
                                     ((numberdensitywater * 2)) * (10 ** -24) * hs[2] * (
                                         math.log(hebar) / math.log(.1))) + (
                                     numberdensitycladding * (10 ** -24) * zr90s[2] * (
                                         math.log(zr90ebar) / math.log(.1)))

    scattering6to7reflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * hs[2] * (
                math.log(hebar) / math.log(.1))) + (
                                          (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * os[2] * (
                                              math.log(oebar) / math.log(.1)))

    # group6absorptioncore = (numberdensityu235 * (10**-24) * u235a[2]) + (numberdensityu238 * (10**-24) * u238a[2]) + (numberdensitypu239 * (10**-24) * pu239c[2]) + ((numberdensitywater + (numberdensityuo2fuel * 2)) * (10**-24) * oa[2]  ) + ( ((numberdensitywater * 2)) * (10**-24) * ha[2]  ) + (numberdensitycladding * (10**-24) * zr90a[2])

    group6absorptionreflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * ha[2]) + (
                (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * oa[2])

    group7scatteringcore = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[1]) + (
                numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[1]) + (
                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[1]) + (
                                       ((numberdensitywater * 2)) * (10 ** -24) * hs[1]) + (
                                       numberdensitycladding * (10 ** -24) * zr90s[1])

    group7scatteringreflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * hs[1]) + (
                (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * os[1])

    scattering7to8core = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[1] * (
                math.log(u235ebar) / math.log(.1))) + (
                                     numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[1] * (
                                         math.log(u238ebar) / math.log(.1))) + (
                                     (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[1] * (
                                         math.log(oebar) / math.log(.1))) + (
                                     ((numberdensitywater * 2)) * (10 ** -24) * hs[1] * (
                                         math.log(hebar) / math.log(.1))) + (
                                     numberdensitycladding * (10 ** -24) * zr90s[1] * (
                                         math.log(zr90ebar) / math.log(.1)))

    scattering7to8reflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * hs[1] * (
                math.log(hebar) / math.log(.1))) + (
                                          (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * os[1] * (
                                              math.log(oebar) / math.log(.1)))

    # group7absorptioncore = (numberdensityu235 * (10**-24) * u235a[1]) + (numberdensityu238 * (10**-24) * u238a[1]) + (numberdensitypu239 * (10**-24) * pu239c[1]) + ((numberdensitywater + (numberdensityuo2fuel * 2)) * (10**-24) * oa[1]  ) + ( ((numberdensitywater * 2)) * (10**-24) * ha[1]  ) + (numberdensitycladding * (10**-24) * zr90a[1])

    group7absorptionreflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * ha[1]) + (
                (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * oa[1])

    group8scatteringcore = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[0]) + (
                numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[0]) + (
                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[0]) + (
                                       ((numberdensitywater * 2)) * (10 ** -24) * hs[0]) + (
                                       numberdensitycladding * (10 ** -24) * zr90s[0])

    group8scatteringreflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * hs[0]) + (
                (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * os[0])

    # group8absorptioncore = (numberdensityu235 * (10**-24) * u235a[0]) + (numberdensityu238 * (10**-24) * u238a[0]) + (numberdensitypu239 * (10**-24) * pu239c[0]) + ((numberdensitywater + (numberdensityuo2fuel * 2)) * (10**-24) * oa[0]  ) + ( ((numberdensitywater * 2)) * (10**-24) * ha[0]  ) + (numberdensitycladding * (10**-24) * zr90a[0])

    group8absorptionreflector = ((numberdensitywater * 2 * (volumecore / volumeh2o)) * (10 ** -24) * ha[0]) + (
                (numberdensitywater * (volumecore / volumeh2o)) * (10 ** -24) * oa[0])

    # print("group1fissiontest: " + str(group1fissiontest))
    # print("group2fissiontest: " + str(group2fissiontest))

    radialaxis = []
    axialaxis = []

    radialfluxdistributiongroup1 = []
    radialfluxdistributiongroup2 = []
    radialfluxdistributiongroup3 = []
    radialfluxdistributiongroup4 = []
    radialfluxdistributiongroup5 = []
    radialfluxdistributiongroup6 = []
    radialfluxdistributiongroup7 = []
    radialfluxdistributiongroup8 = []

    axialfluxdistributiongroup1 = []
    axialfluxdistributiongroup2 = []
    axialfluxdistributiongroup3 = []
    axialfluxdistributiongroup4 = []
    axialfluxdistributiongroup5 = []
    axialfluxdistributiongroup6 = []
    axialfluxdistributiongroup7 = []
    axialfluxdistributiongroup8 = []

    '''
    fueldiameter = 1 #cm

    claddinginnerradius = 1.05 #cm
    claddingoutterradius = 1.1 #cm
    '''

    k = kradialarray[len(kradialarray) - 1]

    kaxial = kaxialarray[len(kaxialarray) - 1];
    diffusiongroup1core = 1 / (3 * group1scatteringcore)  # cm
    diffusiongroup1reflector = 1 / (3 * group1scatteringreflector)  # cm

    diffusiongroup2core = 1 / (3 * group2scatteringcore)  # cm
    diffusiongroup2reflector = 1 / (3 * group2scatteringreflector)  # cm

    diffusiongroup3core = 1 / (3 * group3scatteringcore)  # cm
    diffusiongroup3reflector = 1 / (3 * group3scatteringreflector)  # cm

    diffusiongroup4core = 1 / (3 * group4scatteringcore)  # cm
    diffusiongroup4reflector = 1 / (3 * group4scatteringreflector)  # cm

    diffusiongroup5core = 1 / (3 * group5scatteringcore)  # cm
    diffusiongroup5reflector = 1 / (3 * group5scatteringreflector)  # cm

    diffusiongroup6core = 1 / (3 * group6scatteringcore)  # cm
    diffusiongroup6reflector = 1 / (3 * group6scatteringreflector)  # cm

    diffusiongroup7core = 1 / (3 * group7scatteringcore)  # cm
    diffusiongroup7reflector = 1 / (3 * group7scatteringreflector)  # cm

    diffusiongroup8core = 1 / (3 * group8scatteringcore)  # cm
    diffusiongroup8reflector = 1 / (3 * group8scatteringreflector)  # cm

    '''
    group1absorptioncore = .009 #cm^-1
    group1absorptionreflector = .001 #cm^-1

    group2absorptioncore = .092 #cm^-1
    group2absorptionreflector = .04 #cm^-1

    group3absorptioncore = .009 #cm^-1
    group3absorptionreflector = .001 #cm^-1

    group4absorptioncore = .092 #cm^-1
    group4absorptionreflector = .04 #cm^-1

    group5absorptioncore = .009 #cm^-1
    group5absorptionreflector = .001 #cm^-1

    group6absorptioncore = .092 #cm^-1
    group6absorptionreflector = .04 #cm^-1

    group7absorptioncore = .009 #cm^-1
    group7absorptionreflector = .001 #cm^-1

    group8absorptioncore = .092 #cm^-1
    group8absorptionreflector = .04 #cm^-1
    '''

    '''
    nugroup1fission = .005 #cm^-1
    nugroup2fission = .006 #cm^-1
    nugroup3fission = .007 #cm^-1
    nugroup4fission = .008 #cm^-1
    nugroup5fission = .011 #cm^-1
    nugroup6fission = .040 #cm^-1
    nugroup7fission = .090 #cm^-1
    nugroup8fission = .114 #cm^-1

    scattering1to2core = .02 #cm^-1
    scattering1to2reflector = .05 #cm^-1

    scattering2to3core = .02 #cm^-1
    scattering2to3reflector = .05 #cm^-1

    scattering3to4core = .02 #cm^-1
    scattering3to4reflector = .05 #cm^-1

    scattering4to5core = .02 #cm^-1
    scattering4to5reflector = .05 #cm^-1

    scattering5to6core = .02 #cm^-1
    scattering5to6reflector = .05 #cm^-1

    scattering6to7core = .02 #cm^-1
    scattering6to7reflector = .05 #cm^-1

    scattering7to8core = .02 #cm^-1
    scattering7to8reflector = .05 #cm^-1

    '''

    chimatrix = [1, 0, 0, 0, 0, 0, 0, 0]

    absorptionmatrix = [0, 0, 0, 0, 0, 0, 0, 0]

    scatteringmatrix = [

        # TO
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
        # F
        # R
        # O
        # M

    ]

    '''
    scattering2to1core = 0 #cm^-1
    scattering2to1reflector = 0 #cm^-1
    '''

    '''

    elif j == (n2/2)-1:
        matrix2[j,j-1] = (-2 * dc * dc)/(2*dc*(deltax2**2))
        matrix2[j,j] =
        ((1/(deltax2**2))*(((2*dc*dr)/(dc+dr))+((2*dc*dc)/(2*dc)) )) + sigmac
        matrix2[j,j+1] = (-2 * dr* dc)/((dr+dc)*(deltax2**2))
    elif j == (n2/2):
        matrix2[j,j-1] = (-2*dr*dc)/((dr+dc)*(deltax2**2))
        matrix2[j,j] =
        ((1/(deltax2**2))*(((2*dc*dr)/(dc+dr))+((2*dr*dr)/(2*dr)) )) + sigmar
        matrix2[j,j+1] = (-2*dr*dr)/(2*dr*(deltax2**2))


    '''

    Agroup1 = []
    Agroup2 = []
    Agroup3 = []
    Agroup4 = []
    Agroup5 = []
    Agroup6 = []
    Agroup7 = []
    Agroup8 = []

    Agroup1axial = []
    Agroup2axial = []
    Agroup3axial = []
    Agroup4axial = []
    Agroup5axial = []
    Agroup6axial = []
    Agroup7axial = []
    Agroup8axial = []

    group1fission = []
    group2fission = []

    for i in range(n):
        Agroup1axial.append([])
        Agroup2axial.append([])
        Agroup1.append([])
        Agroup2.append([])
        Agroup3axial.append([])
        Agroup4axial.append([])
        Agroup3.append([])
        Agroup4.append([])
        Agroup5axial.append([])
        Agroup6axial.append([])
        Agroup5.append([])
        Agroup6.append([])
        Agroup7axial.append([])
        Agroup8axial.append([])
        Agroup7.append([])
        Agroup8.append([])
        axialaxis.append(i * (heightreflector / (2 * n)))
        radialaxis.append((i) * (diameterreflector / (2 * n)))

        radialfluxdistributiongroup1.append([1])
        radialfluxdistributiongroup2.append([1])
        radialfluxdistributiongroup3.append([1])
        radialfluxdistributiongroup4.append([1])
        radialfluxdistributiongroup5.append([1])
        radialfluxdistributiongroup6.append([1])
        radialfluxdistributiongroup7.append([1])
        radialfluxdistributiongroup8.append([1])

        axialfluxdistributiongroup1.append([1])
        axialfluxdistributiongroup2.append([1])
        axialfluxdistributiongroup3.append([1])
        axialfluxdistributiongroup4.append([1])
        axialfluxdistributiongroup5.append([1])
        axialfluxdistributiongroup6.append([1])
        axialfluxdistributiongroup7.append([1])
        axialfluxdistributiongroup8.append([1])

        if ((i / n) < (diameterreactorcore / diameterreflector)):
            group1fission.append(nugroup1fission)
            group2fission.append(nugroup2fission)
        else:
            group1fission.append(0)
            group2fission.append(0)

        for j in range(n):
            Agroup1[i].append(0)
            Agroup2[i].append(0)
            Agroup1axial[i].append(0)
            Agroup2axial[i].append(0)
            Agroup3[i].append(0)
            Agroup4[i].append(0)
            Agroup3axial[i].append(0)
            Agroup4axial[i].append(0)
            Agroup5[i].append(0)
            Agroup6[i].append(0)
            Agroup5axial[i].append(0)
            Agroup6axial[i].append(0)
            Agroup7[i].append(0)
            Agroup8[i].append(0)
            Agroup7axial[i].append(0)
            Agroup8axial[i].append(0)

    '''
    for i in range(0,n-5):
        radialaxis.append( (i+5)*(diameterreflector/(2*n))   )
        Agroup1.append([])
        Agroup2.append([])
        radialfluxdistributiongroup1.append([1])
        radialfluxdistributiongroup2.append([1])
        for j in range(0,n-5):
            Agroup1[i].append(0)
            Agroup2[i].append(0)    
    '''

    for i in range(n):
        if (((i + 1) / n) < (heightreactorcore / heightreflector)):
            if i == 0:
                Agroup1axial[i][i] = (diffusiongroup1core / (deltax ** 2)) + group1absorptioncore[i][
                    averageindexradius] + scattering1to2core
                Agroup1axial[i][i + 1] = -diffusiongroup1core / (deltax ** 2)

                Agroup2axial[i][i] = (diffusiongroup2core / (deltax ** 2)) + group2absorptioncore[i][
                    averageindexradius] + scattering2to3core
                Agroup2axial[i][i + 1] = -diffusiongroup2core / (deltax ** 2)

                Agroup3axial[i][i] = (diffusiongroup3core / (deltax ** 2)) + group3absorptioncore[i][
                    averageindexradius] + scattering3to4core
                Agroup3axial[i][i + 1] = -diffusiongroup3core / (deltax ** 2)

                Agroup4axial[i][i] = (diffusiongroup4core / (deltax ** 2)) + group4absorptioncore[i][
                    averageindexradius] + scattering4to5core
                Agroup4axial[i][i + 1] = -diffusiongroup4core / (deltax ** 2)

                Agroup5axial[i][i] = (diffusiongroup5core / (deltax ** 2)) + group5absorptioncore[i][
                    averageindexradius] + scattering5to6core
                Agroup5axial[i][i + 1] = -diffusiongroup5core / (deltax ** 2)

                Agroup6axial[i][i] = (diffusiongroup6core / (deltax ** 2)) + group6absorptioncore[i][
                    averageindexradius] + scattering6to7core
                Agroup6axial[i][i + 1] = -diffusiongroup6core / (deltax ** 2)

                Agroup7axial[i][i] = (diffusiongroup7core / (deltax ** 2)) + group7absorptioncore[i][
                    averageindexradius] + scattering7to8core
                Agroup7axial[i][i + 1] = -diffusiongroup7core / (deltax ** 2)

                Agroup8axial[i][i] = (diffusiongroup8core / (deltax ** 2)) + group8absorptioncore[i][averageindexradius]
                Agroup8axial[i][i + 1] = -diffusiongroup8core / (deltax ** 2)


            elif (i > 0 and i < n - 1):
                Agroup1axial[i][i - 1] = (-diffusiongroup1core / (deltax ** 2))
                Agroup1axial[i][i] = ((2 * diffusiongroup1core) / (deltax ** 2)) + group1absorptioncore[i][
                    averageindexradius] + scattering1to2core
                Agroup1axial[i][i + 1] = (-diffusiongroup1core / (deltax ** 2))

                Agroup2axial[i][i - 1] = (-diffusiongroup2core / (deltax ** 2))
                Agroup2axial[i][i] = ((2 * diffusiongroup2core) / (deltax ** 2)) + group2absorptioncore[i][
                    averageindexradius] + scattering2to3core
                Agroup2axial[i][i + 1] = (-diffusiongroup2core / (deltax ** 2))

                Agroup3axial[i][i - 1] = (-diffusiongroup3core / (deltax ** 2))
                Agroup3axial[i][i] = ((2 * diffusiongroup3core) / (deltax ** 2)) + group3absorptioncore[i][
                    averageindexradius] + scattering3to4core
                Agroup3axial[i][i + 1] = (-diffusiongroup3core / (deltax ** 2))

                Agroup4axial[i][i - 1] = (-diffusiongroup4core / (deltax ** 2))
                Agroup4axial[i][i] = ((2 * diffusiongroup4core) / (deltax ** 2)) + group4absorptioncore[i][
                    averageindexradius] + scattering4to5core
                Agroup4axial[i][i + 1] = (-diffusiongroup4core / (deltax ** 2))

                Agroup5axial[i][i - 1] = (-diffusiongroup5core / (deltax ** 2))
                Agroup5axial[i][i] = ((2 * diffusiongroup5core) / (deltax ** 2)) + group5absorptioncore[i][
                    averageindexradius] + scattering5to6core
                Agroup5axial[i][i + 1] = (-diffusiongroup5core / (deltax ** 2))

                Agroup6axial[i][i - 1] = (-diffusiongroup6core / (deltax ** 2))
                Agroup6axial[i][i] = ((2 * diffusiongroup6core) / (deltax ** 2)) + group6absorptioncore[i][
                    averageindexradius] + scattering6to7core
                Agroup6axial[i][i + 1] = (-diffusiongroup6core / (deltax ** 2))

                Agroup7axial[i][i - 1] = (-diffusiongroup7core / (deltax ** 2))
                Agroup7axial[i][i] = ((2 * diffusiongroup7core) / (deltax ** 2)) + group7absorptioncore[i][
                    averageindexradius] + scattering7to8core
                Agroup7axial[i][i + 1] = (-diffusiongroup7core / (deltax ** 2))

                Agroup8axial[i][i - 1] = (-diffusiongroup8core / (deltax ** 2))
                Agroup8axial[i][i] = ((2 * diffusiongroup8core) / (deltax ** 2)) + group8absorptioncore[i][
                    averageindexradius]
                Agroup8axial[i][i + 1] = (-diffusiongroup8core / (deltax ** 2))




            elif i == n - 1:
                Agroup1axial[i][i - 1] = (-diffusiongroup1core / (deltax ** 2))
                Agroup1axial[i][i] = ((3 * diffusiongroup1core) / (deltax ** 2)) + group1absorptioncore[i][
                    averageindexradius] + scattering1to2core

                Agroup2axial[i][i - 1] = (-diffusiongroup2core / (deltax ** 2))
                Agroup2axial[i][i] = ((3 * diffusiongroup2core) / (deltax ** 2)) + group2absorptioncore[i][
                    averageindexradius] + scattering2to3core

                Agroup3axial[i][i - 1] = (-diffusiongroup3core / (deltax ** 2))
                Agroup3axial[i][i] = ((3 * diffusiongroup3core) / (deltax ** 2)) + group3absorptioncore[i][
                    averageindexradius] + scattering3to4core

                Agroup4axial[i][i - 1] = (-diffusiongroup4core / (deltax ** 2))
                Agroup4axial[i][i] = ((3 * diffusiongroup4core) / (deltax ** 2)) + group4absorptioncore[i][
                    averageindexradius] + scattering4to5core

                Agroup5axial[i][i - 1] = (-diffusiongroup5core / (deltax ** 2))
                Agroup5axial[i][i] = ((3 * diffusiongroup5core) / (deltax ** 2)) + group5absorptioncore[i][
                    averageindexradius] + scattering5to6core

                Agroup6axial[i][i - 1] = (-diffusiongroup6core / (deltax ** 2))
                Agroup6axial[i][i] = ((3 * diffusiongroup6core) / (deltax ** 2)) + group6absorptioncore[i][
                    averageindexradius] + scattering6to7core

                Agroup7axial[i][i - 1] = (-diffusiongroup7core / (deltax ** 2))
                Agroup7axial[i][i] = ((3 * diffusiongroup7core) / (deltax ** 2)) + group7absorptioncore[i][
                    averageindexradius] + scattering7to8core

                Agroup8axial[i][i - 1] = (-diffusiongroup8core / (deltax ** 2))
                Agroup8axial[i][i] = ((3 * diffusiongroup8core) / (deltax ** 2)) + group8absorptioncore[i][
                    averageindexradius]





        elif (((i + 1) / n) >= heightreactorcore / heightreflector and (i / n) < heightreactorcore / heightreflector):

            Agroup1axial[i][i - 1] = (-2 * (diffusiongroup1core ** 2)) / (2 * diffusiongroup1core * (deltax ** 2))
            Agroup1axial[i][i] = ((1 / (deltax ** 2)) * (((2 * diffusiongroup1core * diffusiongroup1reflector) / (
                        diffusiongroup1core + diffusiongroup1reflector)) + (diffusiongroup1core))) + \
                                 group1absorptioncore[i][averageindexradius] + scattering1to2core
            Agroup1axial[i][i + 1] = ((-2 * diffusiongroup1core * diffusiongroup1reflector) / (
                        diffusiongroup1core + diffusiongroup1reflector)) * (1 / (deltax ** 2))

            Agroup2axial[i][i - 1] = (-2 * (diffusiongroup2core ** 2)) / (2 * diffusiongroup2core * (deltax ** 2))
            Agroup2axial[i][i] = ((1 / (deltax ** 2)) * (((2 * diffusiongroup2core * diffusiongroup2reflector) / (
                        diffusiongroup2core + diffusiongroup2reflector)) + (diffusiongroup2core))) + \
                                 group2absorptioncore[i][averageindexradius] + scattering2to3core
            Agroup2axial[i][i + 1] = ((-2 * diffusiongroup2core * diffusiongroup2reflector) / (
                        diffusiongroup2core + diffusiongroup2reflector)) * (1 / (deltax ** 2))

            Agroup3axial[i][i - 1] = (-2 * (diffusiongroup3core ** 2)) / (2 * diffusiongroup3core * (deltax ** 2))
            Agroup3axial[i][i] = ((1 / (deltax ** 2)) * (((2 * diffusiongroup3core * diffusiongroup3reflector) / (
                        diffusiongroup3core + diffusiongroup3reflector)) + (diffusiongroup3core))) + \
                                 group3absorptioncore[i][averageindexradius] + scattering3to4core
            Agroup3axial[i][i + 1] = ((-2 * diffusiongroup3core * diffusiongroup3reflector) / (
                        diffusiongroup3core + diffusiongroup3reflector)) * (1 / (deltax ** 2))

            Agroup4axial[i][i - 1] = (-2 * (diffusiongroup4core ** 2)) / (2 * diffusiongroup4core * (deltax ** 2))
            Agroup4axial[i][i] = ((1 / (deltax ** 2)) * (((2 * diffusiongroup4core * diffusiongroup4reflector) / (
                        diffusiongroup4core + diffusiongroup4reflector)) + (diffusiongroup4core))) + \
                                 group4absorptioncore[i][averageindexradius] + scattering4to5core
            Agroup4axial[i][i + 1] = ((-2 * diffusiongroup4core * diffusiongroup4reflector) / (
                        diffusiongroup4core + diffusiongroup4reflector)) * (1 / (deltax ** 2))

            Agroup5axial[i][i - 1] = (-2 * (diffusiongroup5core ** 2)) / (2 * diffusiongroup5core * (deltax ** 2))
            Agroup5axial[i][i] = ((1 / (deltax ** 2)) * (((2 * diffusiongroup5core * diffusiongroup5reflector) / (
                        diffusiongroup5core + diffusiongroup5reflector)) + (diffusiongroup5core))) + \
                                 group5absorptioncore[i][averageindexradius] + scattering5to6core
            Agroup5axial[i][i + 1] = ((-2 * diffusiongroup5core * diffusiongroup5reflector) / (
                        diffusiongroup5core + diffusiongroup5reflector)) * (1 / (deltax ** 2))

            Agroup6axial[i][i - 1] = (-2 * (diffusiongroup6core ** 2)) / (2 * diffusiongroup6core * (deltax ** 2))
            Agroup6axial[i][i] = ((1 / (deltax ** 2)) * (((2 * diffusiongroup6core * diffusiongroup6reflector) / (
                        diffusiongroup6core + diffusiongroup6reflector)) + (diffusiongroup6core))) + \
                                 group6absorptioncore[i][averageindexradius] + scattering6to7core
            Agroup6axial[i][i + 1] = ((-2 * diffusiongroup6core * diffusiongroup6reflector) / (
                        diffusiongroup6core + diffusiongroup6reflector)) * (1 / (deltax ** 2))

            Agroup7axial[i][i - 1] = (-2 * (diffusiongroup7core ** 2)) / (2 * diffusiongroup7core * (deltax ** 2))
            Agroup7axial[i][i] = ((1 / (deltax ** 2)) * (((2 * diffusiongroup7core * diffusiongroup7reflector) / (
                        diffusiongroup7core + diffusiongroup7reflector)) + (diffusiongroup7core))) + \
                                 group7absorptioncore[i][averageindexradius] + scattering7to8core
            Agroup7axial[i][i + 1] = ((-2 * diffusiongroup7core * diffusiongroup7reflector) / (
                        diffusiongroup7core + diffusiongroup7reflector)) * (1 / (deltax ** 2))

            Agroup8axial[i][i - 1] = (-2 * (diffusiongroup8core ** 2)) / (2 * diffusiongroup8core * (deltax ** 2))
            Agroup8axial[i][i] = ((1 / (deltax ** 2)) * (((2 * diffusiongroup8core * diffusiongroup8reflector) / (
                        diffusiongroup8core + diffusiongroup8reflector)) + (diffusiongroup8core))) + \
                                 group8absorptioncore[i][averageindexradius]
            Agroup8axial[i][i + 1] = ((-2 * diffusiongroup8core * diffusiongroup8reflector) / (
                        diffusiongroup8core + diffusiongroup8reflector)) * (1 / (deltax ** 2))




        elif (((i - 1) / n) < heightreactorcore / heightreflector and (i / n) >= heightreactorcore / heightreflector):
            Agroup1axial[i][i - 1] = ((-2 * diffusiongroup1core * diffusiongroup1reflector) / (
                        diffusiongroup1core + diffusiongroup1reflector)) * (1 / (deltax ** 2))
            Agroup1axial[i][i] = ((1 / (deltax ** 2)) * (((2 * diffusiongroup1core * diffusiongroup1reflector) / (
                        diffusiongroup1core + diffusiongroup1reflector)) + (
                                                             diffusiongroup1reflector))) + group1absorptionreflector + scattering1to2reflector
            Agroup1axial[i][i + 1] = (-2 * (diffusiongroup1reflector ** 2)) / (
                        2 * diffusiongroup1reflector * (deltax ** 2))

            Agroup2axial[i][i - 1] = ((-2 * diffusiongroup2core * diffusiongroup2reflector) / (
                        diffusiongroup2core + diffusiongroup2reflector)) * (1 / (deltax ** 2))
            Agroup2axial[i][i] = ((1 / (deltax ** 2)) * (((2 * diffusiongroup2core * diffusiongroup2reflector) / (
                        diffusiongroup2core + diffusiongroup2reflector)) + (
                                                             diffusiongroup2reflector))) + group2absorptionreflector + scattering2to3reflector
            Agroup2axial[i][i + 1] = (-2 * (diffusiongroup2reflector ** 2)) / (
                        2 * diffusiongroup2reflector * (deltax ** 2))

            Agroup3axial[i][i - 1] = ((-2 * diffusiongroup3core * diffusiongroup3reflector) / (
                        diffusiongroup3core + diffusiongroup3reflector)) * (1 / (deltax ** 2))
            Agroup3axial[i][i] = ((1 / (deltax ** 2)) * (((2 * diffusiongroup3core * diffusiongroup3reflector) / (
                        diffusiongroup3core + diffusiongroup3reflector)) + (
                                                             diffusiongroup3reflector))) + group3absorptionreflector + scattering3to4reflector
            Agroup3axial[i][i + 1] = (-2 * (diffusiongroup3reflector ** 2)) / (
                        2 * diffusiongroup3reflector * (deltax ** 2))

            Agroup4axial[i][i - 1] = ((-2 * diffusiongroup4core * diffusiongroup4reflector) / (
                        diffusiongroup4core + diffusiongroup4reflector)) * (1 / (deltax ** 2))
            Agroup4axial[i][i] = ((1 / (deltax ** 2)) * (((2 * diffusiongroup4core * diffusiongroup4reflector) / (
                        diffusiongroup4core + diffusiongroup4reflector)) + (
                                                             diffusiongroup4reflector))) + group4absorptionreflector + scattering4to5reflector
            Agroup4axial[i][i + 1] = (-2 * (diffusiongroup4reflector ** 2)) / (
                        2 * diffusiongroup4reflector * (deltax ** 2))

            Agroup5axial[i][i - 1] = ((-2 * diffusiongroup5core * diffusiongroup5reflector) / (
                        diffusiongroup5core + diffusiongroup5reflector)) * (1 / (deltax ** 2))
            Agroup5axial[i][i] = ((1 / (deltax ** 2)) * (((2 * diffusiongroup5core * diffusiongroup5reflector) / (
                        diffusiongroup5core + diffusiongroup5reflector)) + (
                                                             diffusiongroup5reflector))) + group5absorptionreflector + scattering5to6reflector
            Agroup5axial[i][i + 1] = (-2 * (diffusiongroup5reflector ** 2)) / (
                        2 * diffusiongroup5reflector * (deltax ** 2))

            Agroup6axial[i][i - 1] = ((-2 * diffusiongroup6core * diffusiongroup6reflector) / (
                        diffusiongroup6core + diffusiongroup6reflector)) * (1 / (deltax ** 2))
            Agroup6axial[i][i] = ((1 / (deltax ** 2)) * (((2 * diffusiongroup6core * diffusiongroup6reflector) / (
                        diffusiongroup6core + diffusiongroup6reflector)) + (
                                                             diffusiongroup6reflector))) + group6absorptionreflector + scattering6to7reflector
            Agroup6axial[i][i + 1] = (-2 * (diffusiongroup6reflector ** 2)) / (
                        2 * diffusiongroup6reflector * (deltax ** 2))

            Agroup7axial[i][i - 1] = ((-2 * diffusiongroup7core * diffusiongroup7reflector) / (
                        diffusiongroup7core + diffusiongroup7reflector)) * (1 / (deltax ** 2))
            Agroup7axial[i][i] = ((1 / (deltax ** 2)) * (((2 * diffusiongroup7core * diffusiongroup7reflector) / (
                        diffusiongroup7core + diffusiongroup7reflector)) + (
                                                             diffusiongroup7reflector))) + group7absorptionreflector + scattering7to8reflector
            Agroup7axial[i][i + 1] = (-2 * (diffusiongroup7reflector ** 2)) / (
                        2 * diffusiongroup7reflector * (deltax ** 2))

            Agroup8axial[i][i - 1] = ((-2 * diffusiongroup8core * diffusiongroup8reflector) / (
                        diffusiongroup8core + diffusiongroup8reflector)) * (1 / (deltax ** 2))
            Agroup8axial[i][i] = ((1 / (deltax ** 2)) * (((2 * diffusiongroup8core * diffusiongroup8reflector) / (
                        diffusiongroup8core + diffusiongroup8reflector)) + (
                                                             diffusiongroup8reflector))) + group8absorptionreflector
            Agroup8axial[i][i + 1] = (-2 * (diffusiongroup8reflector ** 2)) / (
                        2 * diffusiongroup8reflector * (deltax ** 2))


        elif ((i / n) > (heightreactorcore / heightreflector)):
            if i > 0 and i < n - 1:
                Agroup1axial[i][i - 1] = (-diffusiongroup1reflector / (deltax ** 2))
                Agroup1axial[i][i] = ((2 * diffusiongroup1reflector) / (
                            deltax ** 2)) + group1absorptionreflector + scattering1to2reflector
                Agroup1axial[i][i + 1] = (-diffusiongroup1reflector / (deltax ** 2))

                Agroup2axial[i][i - 1] = (-diffusiongroup2reflector / (deltax ** 2))
                Agroup2axial[i][i] = ((2 * diffusiongroup2reflector) / (
                            deltax ** 2)) + group2absorptionreflector + scattering2to3reflector
                Agroup2axial[i][i + 1] = (-diffusiongroup2reflector / (deltax ** 2))

                Agroup3axial[i][i - 1] = (-diffusiongroup3reflector / (deltax ** 2))
                Agroup3axial[i][i] = ((2 * diffusiongroup3reflector) / (
                            deltax ** 2)) + group3absorptionreflector + scattering3to4reflector
                Agroup3axial[i][i + 1] = (-diffusiongroup3reflector / (deltax ** 2))

                Agroup4axial[i][i - 1] = (-diffusiongroup4reflector / (deltax ** 2))
                Agroup4axial[i][i] = ((2 * diffusiongroup4reflector) / (
                            deltax ** 2)) + group4absorptionreflector + scattering4to5reflector
                Agroup4axial[i][i + 1] = (-diffusiongroup4reflector / (deltax ** 2))

                Agroup5axial[i][i - 1] = (-diffusiongroup5reflector / (deltax ** 2))
                Agroup5axial[i][i] = ((2 * diffusiongroup5reflector) / (
                            deltax ** 2)) + group5absorptionreflector + scattering5to6reflector
                Agroup5axial[i][i + 1] = (-diffusiongroup5reflector / (deltax ** 2))

                Agroup6axial[i][i - 1] = (-diffusiongroup6reflector / (deltax ** 2))
                Agroup6axial[i][i] = ((2 * diffusiongroup6reflector) / (
                            deltax ** 2)) + group6absorptionreflector + scattering6to7reflector
                Agroup6axial[i][i + 1] = (-diffusiongroup6reflector / (deltax ** 2))

                Agroup7axial[i][i - 1] = (-diffusiongroup7reflector / (deltax ** 2))
                Agroup7axial[i][i] = ((2 * diffusiongroup7reflector) / (
                            deltax ** 2)) + group7absorptionreflector + scattering7to8reflector
                Agroup7axial[i][i + 1] = (-diffusiongroup7reflector / (deltax ** 2))

                Agroup8axial[i][i - 1] = (-diffusiongroup8reflector / (deltax ** 2))
                Agroup8axial[i][i] = ((2 * diffusiongroup8reflector) / (deltax ** 2)) + group8absorptionreflector
                Agroup8axial[i][i + 1] = (-diffusiongroup8reflector / (deltax ** 2))

            elif i == n - 1:
                Agroup1axial[i][i - 1] = (-diffusiongroup1reflector / (deltax ** 2))
                Agroup1axial[i][i] = ((3 * diffusiongroup1reflector) / (
                            deltax ** 2)) + group1absorptionreflector + scattering1to2reflector

                Agroup2axial[i][i - 1] = (-diffusiongroup2reflector / (deltax ** 2))
                Agroup2axial[i][i] = ((3 * diffusiongroup2reflector) / (
                            deltax ** 2)) + group2absorptionreflector + scattering2to3reflector

                Agroup3axial[i][i - 1] = (-diffusiongroup3reflector / (deltax ** 2))
                Agroup3axial[i][i] = ((3 * diffusiongroup3reflector) / (
                            deltax ** 2)) + group3absorptionreflector + scattering3to4reflector

                Agroup4axial[i][i - 1] = (-diffusiongroup4reflector / (deltax ** 2))
                Agroup4axial[i][i] = ((3 * diffusiongroup4reflector) / (
                            deltax ** 2)) + group4absorptionreflector + scattering4to5reflector

                Agroup5axial[i][i - 1] = (-diffusiongroup5reflector / (deltax ** 2))
                Agroup5axial[i][i] = ((3 * diffusiongroup5reflector) / (
                            deltax ** 2)) + group5absorptionreflector + scattering5to6reflector

                Agroup6axial[i][i - 1] = (-diffusiongroup6reflector / (deltax ** 2))
                Agroup6axial[i][i] = ((3 * diffusiongroup6reflector) / (
                            deltax ** 2)) + group6absorptionreflector + scattering6to7reflector

                Agroup7axial[i][i - 1] = (-diffusiongroup7reflector / (deltax ** 2))
                Agroup7axial[i][i] = ((3 * diffusiongroup7reflector) / (
                            deltax ** 2)) + group7absorptionreflector + scattering7to8reflector

                Agroup8axial[i][i - 1] = (-diffusiongroup8reflector / (deltax ** 2))
                Agroup8axial[i][i] = ((3 * diffusiongroup8reflector) / (deltax ** 2)) + group8absorptionreflector

                # for j in range(100):
    boolean1 = True
    while boolean1:
        group1production = []
        group2production = []
        group3production = []
        group4production = []
        group5production = []
        group6production = []
        group7production = []
        group8production = []

        for i in range(n):
            if ((i / n) < (heightreactorcore / heightreflector)):
                group1production.append([((chi1 / kaxial) * (
                            (nugroup1fission[i][averageindexradius] * axialfluxdistributiongroup1[i][0]) + (
                                nugroup2fission[i][averageindexradius] * axialfluxdistributiongroup2[i][0]) +
                            (nugroup3fission[i][averageindexradius] * axialfluxdistributiongroup3[i][0]) + (
                                        nugroup4fission[i][averageindexradius] * axialfluxdistributiongroup4[i][0]) +
                            (nugroup5fission[i][averageindexradius] * axialfluxdistributiongroup5[i][0]) + (
                                        nugroup6fission[i][averageindexradius] * axialfluxdistributiongroup6[i][0]) +
                            (nugroup7fission[i][averageindexradius] * axialfluxdistributiongroup7[i][0]) + (
                                        nugroup8fission[i][averageindexradius] * axialfluxdistributiongroup8[i][0])
                            ))])

            else:
                group1production.append([0])
        axialfluxonenew = np.linalg.solve(np.array(Agroup1axial), np.array(group1production))

        for i in range(n):
            if ((i / n) < (heightreactorcore / heightreflector)):
                group2production.append([((chi2 / kaxial) * (
                            (nugroup1fission[i][averageindexradius] * axialfluxonenew[i][0]) + (
                                nugroup2fission[i][averageindexradius] * axialfluxdistributiongroup2[i][0]) +
                            (nugroup3fission[i][averageindexradius] * axialfluxdistributiongroup3[i][0]) + (
                                        nugroup4fission[i][averageindexradius] * axialfluxdistributiongroup4[i][0]) +
                            (nugroup5fission[i][averageindexradius] * axialfluxdistributiongroup5[i][0]) + (
                                        nugroup6fission[i][averageindexradius] * axialfluxdistributiongroup6[i][0]) +
                            (nugroup7fission[i][averageindexradius] * axialfluxdistributiongroup7[i][0]) + (
                                        nugroup8fission[i][averageindexradius] * axialfluxdistributiongroup8[i][0])
                            )) + (scattering1to2core * axialfluxonenew[i][0])])
            else:
                group2production.append([(scattering1to2reflector * axialfluxonenew[i][0])])
        axialfluxtwonew = np.linalg.solve(np.array(Agroup2axial), np.array(group2production))

        for i in range(n):
            if ((i / n) < (heightreactorcore / heightreflector)):
                group3production.append([((chi3 / kaxial) * (
                            (nugroup1fission[i][averageindexradius] * axialfluxonenew[i][0]) + (
                                nugroup2fission[i][averageindexradius] * axialfluxtwonew[i][0]) +
                            (nugroup3fission[i][averageindexradius] * axialfluxdistributiongroup3[i][0]) + (
                                        nugroup4fission[i][averageindexradius] * axialfluxdistributiongroup4[i][0]) +
                            (nugroup5fission[i][averageindexradius] * axialfluxdistributiongroup5[i][0]) + (
                                        nugroup6fission[i][averageindexradius] * axialfluxdistributiongroup6[i][0]) +
                            (nugroup7fission[i][averageindexradius] * axialfluxdistributiongroup7[i][0]) + (
                                        nugroup8fission[i][averageindexradius] * axialfluxdistributiongroup8[i][0])
                            )) + (scattering2to3core * axialfluxtwonew[i][0])])
            else:
                group3production.append([(scattering2to3reflector * axialfluxtwonew[i][0])])
        axialfluxthreenew = np.linalg.solve(np.array(Agroup3axial), np.array(group3production))

        for i in range(n):
            if ((i / n) < (heightreactorcore / heightreflector)):
                group4production.append([((chi4 / kaxial) * (
                            (nugroup1fission[i][averageindexradius] * axialfluxonenew[i][0]) + (
                                nugroup2fission[i][averageindexradius] * axialfluxtwonew[i][0]) +
                            (nugroup3fission[i][averageindexradius] * axialfluxthreenew[i][0]) + (
                                        nugroup4fission[i][averageindexradius] * axialfluxdistributiongroup4[i][0]) +
                            (nugroup5fission[i][averageindexradius] * axialfluxdistributiongroup5[i][0]) + (
                                        nugroup6fission[i][averageindexradius] * axialfluxdistributiongroup6[i][0]) +
                            (nugroup7fission[i][averageindexradius] * axialfluxdistributiongroup7[i][0]) + (
                                        nugroup8fission[i][averageindexradius] * axialfluxdistributiongroup8[i][0])
                            )) + (scattering3to4core * axialfluxthreenew[i][0])])
            else:
                group4production.append([(scattering3to4reflector * axialfluxthreenew[i][0])])
        axialfluxfournew = np.linalg.solve(np.array(Agroup4axial), np.array(group4production))

        for i in range(n):
            if ((i / n) < (heightreactorcore / heightreflector)):
                group5production.append([((chi5 / kaxial) * (
                            (nugroup1fission[i][averageindexradius] * axialfluxonenew[i][0]) + (
                                nugroup2fission[i][averageindexradius] * axialfluxtwonew[i][0]) +
                            (nugroup3fission[i][averageindexradius] * axialfluxthreenew[i][0]) + (
                                        nugroup4fission[i][averageindexradius] * axialfluxfournew[i][0]) +
                            (nugroup5fission[i][averageindexradius] * axialfluxdistributiongroup5[i][0]) + (
                                        nugroup6fission[i][averageindexradius] * axialfluxdistributiongroup6[i][0]) +
                            (nugroup7fission[i][averageindexradius] * axialfluxdistributiongroup7[i][0]) + (
                                        nugroup8fission[i][averageindexradius] * axialfluxdistributiongroup8[i][0])
                            )) + (scattering4to5core * axialfluxfournew[i][0])])
            else:
                group5production.append([(scattering4to5reflector * axialfluxfournew[i][0])])
        axialfluxfivenew = np.linalg.solve(np.array(Agroup5axial), np.array(group5production))

        for i in range(n):
            if ((i / n) < (heightreactorcore / heightreflector)):
                group6production.append([((chi6 / kaxial) * (
                            (nugroup1fission[i][averageindexradius] * axialfluxonenew[i][0]) + (
                                nugroup2fission[i][averageindexradius] * axialfluxtwonew[i][0]) +
                            (nugroup3fission[i][averageindexradius] * axialfluxthreenew[i][0]) + (
                                        nugroup4fission[i][averageindexradius] * axialfluxfournew[i][0]) +
                            (nugroup5fission[i][averageindexradius] * axialfluxfivenew[i][0]) + (
                                        nugroup6fission[i][averageindexradius] * axialfluxdistributiongroup6[i][0]) +
                            (nugroup7fission[i][averageindexradius] * axialfluxdistributiongroup7[i][0]) + (
                                        nugroup8fission[i][averageindexradius] * axialfluxdistributiongroup8[i][0])
                            )) + (scattering5to6core * axialfluxfivenew[i][0])])
            else:
                group6production.append([(scattering5to6reflector * axialfluxfivenew[i][0])])
        axialfluxsixnew = np.linalg.solve(np.array(Agroup6axial), np.array(group6production))

        for i in range(n):
            if ((i / n) < (heightreactorcore / heightreflector)):
                group7production.append([((chi7 / kaxial) * (
                            (nugroup1fission[i][averageindexradius] * axialfluxonenew[i][0]) + (
                                nugroup2fission[i][averageindexradius] * axialfluxtwonew[i][0]) +
                            (nugroup3fission[i][averageindexradius] * axialfluxthreenew[i][0]) + (
                                        nugroup4fission[i][averageindexradius] * axialfluxfournew[i][0]) +
                            (nugroup5fission[i][averageindexradius] * axialfluxfivenew[i][0]) + (
                                        nugroup6fission[i][averageindexradius] * axialfluxsixnew[i][0]) +
                            (nugroup7fission[i][averageindexradius] * axialfluxdistributiongroup7[i][0]) + (
                                        nugroup8fission[i][averageindexradius] * axialfluxdistributiongroup8[i][0])
                            )) + (scattering6to7core * axialfluxsixnew[i][0])])
            else:
                group7production.append([(scattering6to7reflector * axialfluxsixnew[i][0])])
        axialfluxsevennew = np.linalg.solve(np.array(Agroup7axial), np.array(group7production))

        for i in range(n):
            if ((i / n) < (heightreactorcore / heightreflector)):
                group8production.append([((chi7 / kaxial) * (
                            (nugroup1fission[i][averageindexradius] * axialfluxonenew[i][0]) + (
                                nugroup2fission[i][averageindexradius] * axialfluxtwonew[i][0]) +
                            (nugroup3fission[i][averageindexradius] * axialfluxthreenew[i][0]) + (
                                        nugroup4fission[i][averageindexradius] * axialfluxfournew[i][0]) +
                            (nugroup5fission[i][averageindexradius] * axialfluxfivenew[i][0]) + (
                                        nugroup6fission[i][averageindexradius] * axialfluxsixnew[i][0]) +
                            (nugroup7fission[i][averageindexradius] * axialfluxsevennew[i][0]) + (
                                        nugroup8fission[i][averageindexradius] * axialfluxdistributiongroup8[i][0])
                            )) + (scattering7to8core * axialfluxsevennew[i][0])])
            else:
                group8production.append([(scattering7to8reflector * axialfluxsevennew[i][0])])
        axialfluxeightnew = np.linalg.solve(np.array(Agroup8axial), np.array(group8production))

        newfluxonesum = 0
        newfluxtwosum = 0
        oldfluxonesum = 0
        oldfluxtwosum = 0
        newfluxthreesum = 0
        newfluxfoursum = 0
        oldfluxthreesum = 0
        oldfluxfoursum = 0
        newfluxfivesum = 0
        newfluxsixsum = 0
        oldfluxfivesum = 0
        oldfluxsixsum = 0
        newfluxsevensum = 0
        newfluxeightsum = 0
        oldfluxsevensum = 0
        oldfluxeightsum = 0

        for i in range(n):
            newfluxonesum = newfluxonesum + axialfluxonenew[i][0]
            newfluxtwosum = newfluxtwosum + axialfluxtwonew[i][0]
            oldfluxonesum = oldfluxonesum + axialfluxdistributiongroup1[i][0]
            oldfluxtwosum = oldfluxtwosum + axialfluxdistributiongroup2[i][0]

            newfluxthreesum = newfluxthreesum + axialfluxthreenew[i][0]
            newfluxfoursum = newfluxfoursum + axialfluxfournew[i][0]
            oldfluxthreesum = oldfluxthreesum + axialfluxdistributiongroup3[i][0]
            oldfluxfoursum = oldfluxfoursum + axialfluxdistributiongroup4[i][0]

            newfluxfivesum = newfluxfivesum + axialfluxfivenew[i][0]
            newfluxsixsum = newfluxsixsum + axialfluxsixnew[i][0]
            oldfluxfivesum = oldfluxfivesum + axialfluxdistributiongroup5[i][0]
            oldfluxsixsum = oldfluxsixsum + axialfluxdistributiongroup6[i][0]

            newfluxsevensum = newfluxsevensum + axialfluxsevennew[i][0]
            newfluxeightsum = newfluxeightsum + axialfluxeightnew[i][0]
            oldfluxsevensum = oldfluxsevensum + axialfluxdistributiongroup7[i][0]
            oldfluxeightsum = oldfluxeightsum + axialfluxdistributiongroup8[i][0]

        knew = kaxial * ((
                                     newfluxonesum + newfluxtwosum + newfluxthreesum + newfluxfoursum + newfluxfivesum + newfluxsixsum + newfluxsevensum + newfluxeightsum) / (
                                     oldfluxonesum + oldfluxtwosum + oldfluxthreesum + oldfluxfoursum + oldfluxfivesum + oldfluxsixsum + oldfluxsevensum + oldfluxeightsum))
        if (abs(knew - kaxial) < (10 ** (-7))):
            boolean1 = False
        kaxial = knew

        axialfluxdistributiongroup1 = axialfluxonenew

        axialfluxdistributiongroup2 = axialfluxtwonew
        axialfluxdistributiongroup3 = axialfluxthreenew

        axialfluxdistributiongroup4 = axialfluxfournew
        axialfluxdistributiongroup5 = axialfluxfivenew

        axialfluxdistributiongroup6 = axialfluxsixnew
        axialfluxdistributiongroup7 = axialfluxsevennew
        axialfluxdistributiongroup8 = axialfluxeightnew
        # print(kaxial)

    print(kaxial)
    kaxialarray.append(kaxial)
    print(timearray[(len(timearray) - 1)] + timeperiteration)
    timearray.append(timearray[(len(timearray) - 1)] + timeperiteration)

    '''
    for i in range(n):
        if ((i+1)/n) < (diameterreactorcore/diameterreflector):
            diffusiongroup1 = diffusiongroup1core
            diffusiongroup2 = diffusiongroup2core
            if i == 0:
                localinput1 =   (((diameterreflector * (i+.0001))/(2 * n)))/( ((diameterreflector * (i + .0001))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                localinput2 = ((diameterreflector * (i+.5))/(2 * n))/( ((diameterreflector * (i + .0001))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                Agroup1[0][0] = (localinput1 * (-diffusiongroup1)) + group1absorptioncore + scattering1to2core
                Agroup1[0][1] = (localinput2 * (-diffusiongroup1))
                Agroup2[0][0] = (localinput1 * (-diffusiongroup2)) + group2absorptioncore + scattering2to1core
                Agroup2[0][1] = (localinput2 * (-diffusiongroup2))          


            elif(i > 0 and i < n-1):           
                localinput1 = (((diameterreflector * (i-.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
                localinput2 = ((-1) * (((diameterreflector * (i-.5))/(2 * n)) + ((diameterreflector * (i+.5))/(2 * n))   )      )/( ((diameterreflector * i)/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
                localinput3 = (  ((diameterreflector * (i+.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
                Agroup1[i][i] = localinput2 * (-diffusiongroup1)
                Agroup1[i][i-1] = (localinput1 * (-diffusiongroup1)) + group1absorptioncore + scattering1to2core
                Agroup1[i][i+1] = localinput3 * (-diffusiongroup1)
                Agroup2[i][i] = localinput2 * (-diffusiongroup2)
                Agroup2[i][i-1] = (localinput1 * (-diffusiongroup2)) + group2absorptioncore + scattering2to1core
                Agroup2[i][i+1] = localinput3 * (-diffusiongroup2)            
            elif i == n-1:
                localinput2 = (     ((diameterreflector * (i-1))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                localinput3 = (     (-3)*((diameterreflector * (i))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                Agroup1[n-1][n-2] = localinput2 * (-diffusiongroup1)
                Agroup1[n-1][n-1] = localinput3 * (-diffusiongroup1) + group1absorptioncore + scattering1to2core
                Agroup2[n-1][n-2] = localinput2 * (-diffusiongroup2)
                Agroup2[n-1][n-1] = localinput3 * (-diffusiongroup2) + group2absorptioncore + scattering2to1core 
        elif (((i+1)/n) > (diameterreactorcore/diameterreflector) and (i/n) < (diameterreactorcore/diameterreflector)):
            localinput1 = (((diameterreflector * (i-.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
            localinput2 = ( (((diameterreflector * (i-.5))/(2 * n)) + ((diameterreflector * (i+.5))/(2 * n))   )      )/( ((diameterreflector * i)/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
            localinput3 = (  ((diameterreflector * (i+.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
            Agroup1[i][i] = (localinput2 *  (((2*diffusiongroup1core*diffusiongroup1reflector)/(diffusiongroup1core + diffusiongroup1reflector)) + ((2*(diffusiongroup1core**2))/(2*diffusiongroup1core))     )   )   + group1absorptioncore + scattering1to2core
            Agroup1[i][i-1] = localinput1 * ((-2*(diffusiongroup1core**2))/(2*diffusiongroup1core))
            Agroup1[i][i+1] = localinput3 * ((-(2*diffusiongroup1core*diffusiongroup1reflector))/(diffusiongroup1core + diffusiongroup1reflector))
            Agroup2[i][i] = localinput2 * (-diffusiongroup2)
            Agroup2[i][i-1] = localinput1 * (-diffusiongroup2) + group2absorptioncore + scattering2to1core
            Agroup2[i][i+1] = localinput3 * (-diffusiongroup2)      
        elif (((i)/n) > (diameterreactorcore/diameterreflector) and ((i-1)/n) < (diameterreactorcore/diameterreflector)):
            localinput1 = (((diameterreflector * (i-.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
            localinput2 = ((-1) * (((diameterreflector * (i-.5))/(2 * n)) + ((diameterreflector * (i+.5))/(2 * n))   )      )/( ((diameterreflector * i)/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
            localinput3 = (  ((diameterreflector * (i+.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
            Agroup1[i][i] = (localinput2 * (((2*diffusiongroup1core*diffusiongroup1reflector)/(diffusiongroup1core + diffusiongroup1reflector)) + ((2*(diffusiongroup1core**2))/(2*diffusiongroup1core))     )   )   + group1absorptionreflector + scattering1to2reflector
            Agroup1[i][i-1] = localinput1 * ((-(2*diffusiongroup1core*diffusiongroup1reflector))/(diffusiongroup1core + diffusiongroup1reflector))
            Agroup1[i][i+1] = localinput3 * ((-2*(diffusiongroup1reflector**2))/(2*diffusiongroup1reflector))
            Agroup2[i][i] = localinput2 * (-diffusiongroup2)
            Agroup2[i][i-1] = localinput1 * (-diffusiongroup2) + group2absorptionreflector + scattering2to1reflector
            Agroup2[i][i+1] = localinput3 * (-diffusiongroup2)  
        elif (i/n) > (diameterreactorcore/diameterreflector):
            diffusiongroup1 = diffusiongroup1reflector
            diffusiongroup2 = diffusiongroup2reflector
            if i == 0:
                localinput1 =   (((diameterreflector * (i+.0001))/(2 * n)))/( ((diameterreflector * (i + .0001))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                localinput2 = ((diameterreflector * (i+.5))/(2 * n))/( ((diameterreflector * (i + .0001))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                Agroup1[0][0] = localinput1 * (-diffusiongroup1) + group1absorptionreflector + scattering1to2reflector
                Agroup1[0][1] = localinput2 * (-diffusiongroup1)
                Agroup2[0][0] = localinput1 * (-diffusiongroup2) + group2absorptionreflector + scattering2to1reflector
                Agroup2[0][1] = localinput2 * (-diffusiongroup2)           


            elif(i > 0 and i < n-1):           
                localinput1 = (((diameterreflector * (i-.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
                localinput2 = ((-1) * (((diameterreflector * (i-.5))/(2 * n)) + ((diameterreflector * (i+.5))/(2 * n))   )      )/( ((diameterreflector * i)/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
                localinput3 = (  ((diameterreflector * (i+.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
                Agroup1[i][i] = localinput2 * (-diffusiongroup1) + group1absorptionreflector + scattering1to2reflector
                Agroup1[i][i-1] = localinput1 * (-diffusiongroup1)
                Agroup1[i][i+1] = localinput3 * (-diffusiongroup1)
                Agroup2[i][i] = localinput2 * (-diffusiongroup2) + group2absorptionreflector + scattering2to1reflector
                Agroup2[i][i-1] = localinput1 * (-diffusiongroup2)
                Agroup2[i][i+1] = localinput3 * (-diffusiongroup2)            
            elif i == n-1:
                localinput2 = (     ((diameterreflector * (i-1))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                localinput3 = (     (-3)*((diameterreflector * (i))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                Agroup1[n-1][n-2] = localinput2 * (-diffusiongroup1)
                Agroup1[n-1][n-1] = localinput3 * (-diffusiongroup1) + group1absorptionreflector + scattering1to2reflector
                Agroup2[n-1][n-2] = localinput2 * (-diffusiongroup2)
                Agroup2[n-1][n-1] = localinput3 * (-diffusiongroup2) + group2absorptionreflector + scattering2to1reflector

    '''
    '''
    for i in range(0,n-5):
        if ((i+1+5)/(n-5)) < (diameterreactorcore/diameterreflector):
            diffusiongroup1 = diffusiongroup1core
            diffusiongroup2 = diffusiongroup2core
            if i == 0:
                localinput1 =   (((diameterreflector * (i+5+.0001))/(2 * (n-5))))/( ((diameterreflector * (i+5 + .0001))/(2 * (n-5)))  *    (((diameterreflector/(2*(n-5))))**2)      )
                localinput2 = ((diameterreflector * (i+5+.5))/(2 * (n-5)))/( ((diameterreflector * (i+5 + .0001))/(2 * (n-5)))  *    (((diameterreflector/(2*(n-5))))**2)      )
                Agroup1[0][0] = (localinput1 * (diffusiongroup1)) + group1absorptioncore + scattering1to2core
                Agroup1[0][1] = (localinput2 * (-diffusiongroup1))
                Agroup2[0][0] = (localinput1 * (diffusiongroup2)) + group2absorptioncore + scattering2to1core
                Agroup2[0][1] = (localinput2 * (-diffusiongroup2))          


            elif(i > 0 and i < n-1-5):           
                localinput1 = (((diameterreflector * (i+5-.5))/(2 * (n-5)))      )/( ((diameterreflector * (i+5))/(2 * (n-5))) * (((diameterreflector/(2*(n-5))))**2)   )
                localinput2 = ((-1) * (((diameterreflector * (i+5-.5))/(2 * (n-5))) + ((diameterreflector * (i+5+.5))/(2 * (n-5)))   )      )/( ((diameterreflector * (i+5))/(2 * (n-5))) * (((diameterreflector/(2*(n-5))))**2)   )
                localinput3 = (  ((diameterreflector * (i+5+.5))/(2 * (n-5)))      )/( ((diameterreflector * (i))/(2 * (n-5))) * (((diameterreflector/(2*(n-5))))**2)   )
                Agroup1[i][i] = (localinput2 * (-diffusiongroup1)) + group1absorptioncore + scattering1to2core
                Agroup1[i][i-1] = (localinput1 * (-diffusiongroup1))
                Agroup1[i][i+1] = localinput3 * (-diffusiongroup1)
                Agroup2[i][i] = (localinput2 * (-diffusiongroup2)) + group2absorptioncore + scattering2to1core
                Agroup2[i][i-1] = (localinput1 * (-diffusiongroup2))
                Agroup2[i][i+1] = localinput3 * (-diffusiongroup2)            
            elif i == n-1-5:
                localinput2 = (     ((diameterreflector * (i-1))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                localinput3 = (     (-3)*((diameterreflector * (i))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                Agroup1[n-1][n-2] = localinput2 * (-diffusiongroup1)
                Agroup1[n-1][n-1] = (localinput3 * (-diffusiongroup1)) + group1absorptioncore + scattering1to2core
                Agroup2[n-1][n-2] = localinput2 * (-diffusiongroup2)
                Agroup2[n-1][n-1] = (localinput3 * (-diffusiongroup2)) + group2absorptioncore + scattering2to1core       
        elif (((i+5+1)/(n-5)) >= (diameterreactorcore/diameterreflector) and ((i+5)/(n-5)) < (diameterreactorcore/diameterreflector)):
            localinput1 = (((diameterreflector * (i+5-.5))/(2 * (n-5)))      )/( ((diameterreflector * (i+5))/(2 * (n-5))) * (((diameterreflector/(2*(n-5))))**2)   )
            localinput2 = ( (((diameterreflector * (i+5-.5))/(2 * (n-5))) + ((diameterreflector * (i+5+.5))/(2 * (n-5)))   )      )/( ((diameterreflector * (i+5))/(2 * (n-5))) * (((diameterreflector/(2*(n-5))))**2)   )
            localinput3 = (  ((diameterreflector * (i+5+.5))/(2 * (n-5)))      )/( ((diameterreflector * (i+5))/(2 * (n-5))) * (((diameterreflector/(2*(n-5))))**2)   )
            Agroup1[i][i] = (localinput2 *  (((2*diffusiongroup1core*diffusiongroup1reflector)/(diffusiongroup1core + diffusiongroup1reflector)) + ((2*(diffusiongroup1core**2))/(2*diffusiongroup1core))     )   )   + group1absorptioncore + scattering1to2core
            Agroup1[i][i-1] = localinput1 * (((-2)*(diffusiongroup1core**2))/(2*diffusiongroup1core))
            Agroup1[i][i+1] = localinput3 * ((-(2*diffusiongroup1core*diffusiongroup1reflector))/(diffusiongroup1core + diffusiongroup1reflector))
            Agroup2[i][i] = (localinput2 *(((2*diffusiongroup2core*diffusiongroup2reflector)/(diffusiongroup2core + diffusiongroup2reflector)) + ((2*(diffusiongroup2core**2))/(2*diffusiongroup2core))     ))   + group2absorptioncore + scattering2to1core
            Agroup2[i][i-1] = (localinput1 * (((-2)*(diffusiongroup2core**2))/(2*diffusiongroup2core)) ) 
            Agroup2[i][i+1] = localinput3 * ((-(2*diffusiongroup2core*diffusiongroup2reflector))/(diffusiongroup2core + diffusiongroup2reflector))     
        elif (((i+5)/(n-5)) >= (diameterreactorcore/diameterreflector) and ((i+5-1)/(n-5)) < (diameterreactorcore/diameterreflector)):
            localinput1 = (((diameterreflector * (i+5-.5))/(2 * (n-5)))      )/( ((diameterreflector * (i+5))/(2 * (n-5))) * (((diameterreflector/(2*(n-5))))**2)   )
            localinput2 = ((-1) * (((diameterreflector * (i+5-.5))/(2 * (n-5))) + ((diameterreflector * (i+5+.5))/(2 * (n-5)))   )      )/( ((diameterreflector * (i+5))/(2 * (n-5))) * (((diameterreflector/(2*(n-5))))**2)   )
            localinput3 = (  ((diameterreflector * (i+5+.5))/(2 * (n-5)))      )/( ((diameterreflector * (i+5))/(2 * (n-5))) * (((diameterreflector/(2*(n-5))))**2)   )
            Agroup1[i][i] = (localinput2 * (((2*diffusiongroup1core*diffusiongroup1reflector)/(diffusiongroup1core + diffusiongroup1reflector)) + ((2*(diffusiongroup1core**2))/(2*diffusiongroup1core))     )   )   + group1absorptionreflector + scattering1to2reflector
            Agroup1[i][i-1] = localinput1 * ((-(2*diffusiongroup1core*diffusiongroup1reflector))/(diffusiongroup1core + diffusiongroup1reflector))
            Agroup1[i][i+1] = localinput3 * ((-2*(diffusiongroup1reflector**2))/(2*diffusiongroup1reflector))
            Agroup2[i][i] = localinput2 * (((2*diffusiongroup2core*diffusiongroup2reflector)/(diffusiongroup2core + diffusiongroup2reflector)) + ((2*(diffusiongroup2core**2))/(2*diffusiongroup2core))     ) + group2absorptionreflector + scattering2to1reflector
            Agroup2[i][i-1] = localinput1 * ((-(2*diffusiongroup2core*diffusiongroup2reflector))/(diffusiongroup2core + diffusiongroup2reflector))
            Agroup2[i][i+1] = localinput3 * ((-2*(diffusiongroup2reflector**2))/(2*diffusiongroup2reflector))
        elif ((i+5)/(n-5)) > (diameterreactorcore/diameterreflector):
            diffusiongroup1 = diffusiongroup1reflector
            diffusiongroup2 = diffusiongroup2reflector
            if i == 0:
                localinput1 =   (((diameterreflector * (i+.0001))/(2 * n)))/( ((diameterreflector * (i + .0001))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                localinput2 = ((diameterreflector * (i+.5))/(2 * n))/( ((diameterreflector * (i + .0001))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                Agroup1[0][0] = (localinput1 * (-diffusiongroup1)) + group1absorptionreflector + scattering1to2reflector
                Agroup1[0][1] = localinput2 * (-diffusiongroup1)
                Agroup2[0][0] = (localinput1 * (-diffusiongroup2)) + group2absorptionreflector + scattering2to1reflector
                Agroup2[0][1] = localinput2 * (-diffusiongroup2)           


            elif(i > 0 and i < n-1-5):           
                localinput1 = (((diameterreflector * (i+5-.5))/(2 * (n-5)))      )/( ((diameterreflector * (i+5))/(2 * (n-5))) * (((diameterreflector/(2*(n-5))))**2)   )
                localinput2 = ((-1) * (((diameterreflector * (i+5-.5))/(2 * (n-5))) + ((diameterreflector * (i+5+.5))/(2 * (n-5)))   )      )/( ((diameterreflector * (i+5))/(2 * (n-5))) * (((diameterreflector/(2*(n-5))))**2)   )
                localinput3 = (  ((diameterreflector * (i+5+.5))/(2 * (n-5)))      )/( ((diameterreflector * (i+5))/(2 * (n-5))) * (((diameterreflector/(2*(n-5))))**2)   )
                Agroup1[i][i] = (localinput2 * (-diffusiongroup1)) + group1absorptionreflector + scattering1to2reflector
                Agroup1[i][i-1] = localinput1 * (-diffusiongroup1)
                Agroup1[i][i+1] = localinput3 * (-diffusiongroup1)
                Agroup2[i][i] = (localinput2 * (-diffusiongroup2)) + group2absorptionreflector + scattering2to1reflector
                Agroup2[i][i-1] = localinput1 * (-diffusiongroup2)
                Agroup2[i][i+1] = localinput3 * (-diffusiongroup2)            
            elif i == n-1-5:
                localinput2 = (     ((diameterreflector * (i+5-1))/(2 * (n-5)))      )/( ((diameterreflector * (i+5))/(2 * (n-5)))  *    (((diameterreflector/(2*(n-5))))**2)      )
                localinput3 = (     (-3)*((diameterreflector * (i+5))/(2 * (n-5)))      )/( ((diameterreflector * (i+5))/(2 * (n-5)))  *    (((diameterreflector/(2*(n-5))))**2)   )
                Agroup1[n-5-1][n-5-2] = localinput2 * (-diffusiongroup1)
                Agroup1[n-5-1][n-5-1] = (localinput3 * (-diffusiongroup1)) + group1absorptionreflector + scattering1to2reflector
                Agroup2[n-5-1][n-5-2] = localinput2 * (-diffusiongroup2)
                Agroup2[n-5-1][n-5-1] = (localinput3 * (-diffusiongroup2)) + group2absorptionreflector + scattering2to1reflector
    '''

    '''
    for i in range(n):
        if ((i+1)/n) < (diameterreactorcore/diameterreflector):
            diffusiongroup1 = diffusiongroup1core
            diffusiongroup2 = diffusiongroup2core
            if i == 0:
                #localinput1 =   (((diameterreflector * (i+.0001))/(2 * n)))/( ((diameterreflector * (i + .0001))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                #localinput2 = ((diameterreflector * (i+.5))/(2 * n))/( ((diameterreflector * (i + .0001))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                localinput1 =   (((diameterreflector * (i+.5))/(2 * n)))/( ((diameterreflector * (i + .0001))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                localinput2 = ((diameterreflector * (i+.5))/(2 * n))/( ((diameterreflector * (i + .0001))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )            
                Agroup1[0][0] = (localinput1 * (diffusiongroup1)) + group1absorptioncore + scattering1to2core
                Agroup1[0][1] = (localinput2 * (-diffusiongroup1))
                Agroup2[0][0] = (localinput1 * (diffusiongroup2)) + group2absorptioncore + scattering2to1core
                Agroup2[0][1] = (localinput2 * (-diffusiongroup2))          


            elif(i > 0 and i < n-1):           
                localinput1 = (((diameterreflector * (i-.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
                localinput2 = ((-1) * (((diameterreflector * (i-.5))/(2 * n)) + ((diameterreflector * (i+.5))/(2 * n))   )      )/( ((diameterreflector * i)/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
                localinput3 = (  ((diameterreflector * (i+.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
                Agroup1[i][i] = (localinput2 * (-diffusiongroup1)) + group1absorptioncore + scattering1to2core
                Agroup1[i][i-1] = (localinput1 * (-diffusiongroup1))
                Agroup1[i][i+1] = localinput3 * (-diffusiongroup1)
                Agroup2[i][i] = (localinput2 * (-diffusiongroup2)) + group2absorptioncore + scattering2to1core
                Agroup2[i][i-1] = (localinput1 * (-diffusiongroup2))
                Agroup2[i][i+1] = localinput3 * (-diffusiongroup2)            
            elif i == n-1:
                localinput2 = (     ((diameterreflector * (i-1))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                localinput3 = (     (-3)*((diameterreflector * (i))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                Agroup1[n-1][n-2] = localinput2 * (-diffusiongroup1)
                Agroup1[n-1][n-1] = (localinput3 * (-diffusiongroup1)) + group1absorptioncore + scattering1to2core
                Agroup2[n-1][n-2] = localinput2 * (-diffusiongroup2)
                Agroup2[n-1][n-1] = (localinput3 * (-diffusiongroup2)) + group2absorptioncore + scattering2to1core       
        elif (((i+1)/n) >= (diameterreactorcore/diameterreflector) and (i/n) < (diameterreactorcore/diameterreflector)):
            localinput1 = (((diameterreflector * (i-.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
            localinput2 = ( (((diameterreflector * (i-.5))/(2 * n)) + ((diameterreflector * (i+.5))/(2 * n))   )      )/( ((diameterreflector * i)/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
            localinput3 = (  ((diameterreflector * (i+.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
            Agroup1[i][i] = (localinput2 *  (((2*diffusiongroup1core*diffusiongroup1reflector)/(diffusiongroup1core + diffusiongroup1reflector)) + ((2*(diffusiongroup1core**2))/(2*diffusiongroup1core))     )   )   + group1absorptioncore + scattering1to2core
            Agroup1[i][i-1] = localinput1 * (((-2)*(diffusiongroup1core**2))/(2*diffusiongroup1core))
            Agroup1[i][i+1] = localinput3 * ((-(2*diffusiongroup1core*diffusiongroup1reflector))/(diffusiongroup1core + diffusiongroup1reflector))

            Agroup2[i][i] = (localinput2 *(((2*diffusiongroup2core*diffusiongroup2reflector)/(diffusiongroup2core + diffusiongroup2reflector)) + ((2*(diffusiongroup2core**2))/(2*diffusiongroup2core))     ))   + group2absorptioncore + scattering2to1core
            Agroup2[i][i-1] = (localinput1 * (((-2)*(diffusiongroup2core**2))/(2*diffusiongroup2core)) ) 
            Agroup2[i][i+1] = localinput3 * ((-(2*diffusiongroup2core*diffusiongroup2reflector))/(diffusiongroup2core + diffusiongroup2reflector))     
        elif (((i)/n) >= (diameterreactorcore/diameterreflector) and ((i-1)/n) < (diameterreactorcore/diameterreflector)):
            localinput1 = (((diameterreflector * (i-.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
            localinput2 = ((-1) * (((diameterreflector * (i-.5))/(2 * n)) + ((diameterreflector * (i+.5))/(2 * n))   )      )/( ((diameterreflector * i)/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
            localinput3 = (  ((diameterreflector * (i+.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
            Agroup1[i][i] = (localinput2 * (((2*diffusiongroup1core*diffusiongroup1reflector)/(diffusiongroup1core + diffusiongroup1reflector)) + ((2*(diffusiongroup1core**2))/(2*diffusiongroup1core))     )   )   + group1absorptionreflector + scattering1to2reflector
            Agroup1[i][i-1] = localinput1 * ((-(2*diffusiongroup1core*diffusiongroup1reflector))/(diffusiongroup1core + diffusiongroup1reflector))
            Agroup1[i][i+1] = localinput3 * ((-2*(diffusiongroup1reflector**2))/(2*diffusiongroup1reflector))

            Agroup2[i][i] = localinput2 * (((2*diffusiongroup2core*diffusiongroup2reflector)/(diffusiongroup2core + diffusiongroup2reflector)) + ((2*(diffusiongroup2core**2))/(2*diffusiongroup2core))     ) + group2absorptionreflector + scattering2to1reflector
            Agroup2[i][i-1] = localinput1 * ((-(2*diffusiongroup2core*diffusiongroup2reflector))/(diffusiongroup2core + diffusiongroup2reflector))
            Agroup2[i][i+1] = localinput3 * ((-2*(diffusiongroup2reflector**2))/(2*diffusiongroup2reflector))             
        elif (i/n) > (diameterreactorcore/diameterreflector):
            diffusiongroup1 = diffusiongroup1reflector
            diffusiongroup2 = diffusiongroup2reflector
            if i == 0:
                localinput1 =   (((diameterreflector * (i+.0001))/(2 * n)))/( ((diameterreflector * (i + .0001))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                localinput2 = ((diameterreflector * (i+.5))/(2 * n))/( ((diameterreflector * (i + .0001))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                Agroup1[0][0] = localinput1 * (-diffusiongroup1) + group1absorptionreflector + scattering1to2reflector
                Agroup1[0][1] = localinput2 * (-diffusiongroup1)
                Agroup2[0][0] = localinput1 * (-diffusiongroup2) + group2absorptionreflector + scattering2to1reflector
                Agroup2[0][1] = localinput2 * (-diffusiongroup2)           


            elif(i > 0 and i < n-1):           
                localinput1 = (((diameterreflector * (i-.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
                localinput2 = ((-1) * (((diameterreflector * (i-.5))/(2 * n)) + ((diameterreflector * (i+.5))/(2 * n))   )      )/( ((diameterreflector * i)/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
                localinput3 = (  ((diameterreflector * (i+.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
                Agroup1[i][i] = localinput2 * (-diffusiongroup1) + group1absorptionreflector + scattering1to2reflector
                Agroup1[i][i-1] = localinput1 * (-diffusiongroup1)
                Agroup1[i][i+1] = localinput3 * (-diffusiongroup1)
                Agroup2[i][i] = localinput2 * (-diffusiongroup2) + group2absorptionreflector + scattering2to1reflector
                Agroup2[i][i-1] = localinput1 * (-diffusiongroup2)
                Agroup2[i][i+1] = localinput3 * (-diffusiongroup2)            
            elif i == n-1:
                localinput2 = (     ((diameterreflector * (i-1))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                localinput3 = (     (-3)*((diameterreflector * (i))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                Agroup1[n-1][n-2] = localinput2 * (-diffusiongroup1)
                Agroup1[n-1][n-1] = localinput3 * (-diffusiongroup1) + group1absorptionreflector + scattering1to2reflector
                Agroup2[n-1][n-2] = localinput2 * (-diffusiongroup2)
                Agroup2[n-1][n-1] = localinput3 * (-diffusiongroup2) + group2absorptionreflector + scattering2to1reflector
    '''

    ''' PLUS OR MINUS .5
    for i in range(n):
        if ((i+1)/n) < (diameterreactorcore/diameterreflector):
            diffusiongroup1 = diffusiongroup1core
            diffusiongroup2 = diffusiongroup2core
            if i == 0:
                #localinput1 =   (((diameterreflector * (i+.0001))/(2 * n)))/( ((diameterreflector * (i + .0001))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                #localinput2 = ((diameterreflector * (i+.5))/(2 * n))/( ((diameterreflector * (i + .0001))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                localinput1 =   (((diameterreflector * (i+.5))/(2 * n)))/( ((diameterreflector * (i + .0001))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                localinput2 = ((diameterreflector * (i+.5))/(2 * n))/( ((diameterreflector * (i + .0001))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )  
                Agroup1[0][0] = (localinput1 * (diffusiongroup1)) + group1absorptioncore + scattering1to2core
                Agroup1[0][1] = (localinput2 * (-diffusiongroup1))
                Agroup2[0][0] = (localinput1 * (diffusiongroup2)) + group2absorptioncore + scattering2to1core
                Agroup2[0][1] = (localinput2 * (-diffusiongroup2))          


            elif(i > 0 and i < n-1):           
                localinput1 = (((diameterreflector * (i-.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
                localinput2 = ((-1) * (((diameterreflector * (i-.5))/(2 * n)) + ((diameterreflector * (i+.5))/(2 * n))   )      )/( ((diameterreflector * i)/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
                localinput3 = (  ((diameterreflector * (i+.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
                Agroup1[i][i] = (localinput2 * (-diffusiongroup1)) + group1absorptioncore + scattering1to2core
                Agroup1[i][i-1] = (localinput1 * (-diffusiongroup1))
                Agroup1[i][i+1] = localinput3 * (-diffusiongroup1)
                Agroup2[i][i] = (localinput2 * (-diffusiongroup2)) + group2absorptioncore + scattering2to1core
                Agroup2[i][i-1] = (localinput1 * (-diffusiongroup2))
                Agroup2[i][i+1] = localinput3 * (-diffusiongroup2)            
            elif i == n-1:
                localinput2 = (     ((diameterreflector * (i-1))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                localinput3 = (     (-3)*((diameterreflector * (i))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                Agroup1[n-1][n-2] = localinput2 * (-diffusiongroup1)
                Agroup1[n-1][n-1] = (localinput3 * (-diffusiongroup1)) + group1absorptioncore + scattering1to2core
                Agroup2[n-1][n-2] = localinput2 * (-diffusiongroup2)
                Agroup2[n-1][n-1] = (localinput3 * (-diffusiongroup2)) + group2absorptioncore + scattering2to1core       
        elif (((i+1)/n) >= (diameterreactorcore/diameterreflector) and (i/n) < (diameterreactorcore/diameterreflector)):
            localinput1 = (((diameterreflector * (i-.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
            localinput2 = ( (((diameterreflector * (i-.5))/(2 * n)) + ((diameterreflector * (i+.5))/(2 * n))   )      )/( ((diameterreflector * i)/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
            localinput3 = (  ((diameterreflector * (i+.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
            Agroup1[i][i] = (localinput2 * .5 * (((2*diffusiongroup1core*diffusiongroup1reflector)/(diffusiongroup1core + diffusiongroup1reflector)) + ((2*(diffusiongroup1core**2))/(2*diffusiongroup1core))     )   )   + group1absorptioncore + scattering1to2core
            Agroup1[i][i-1] = localinput1 * (((-2)*(diffusiongroup1core**2))/(2*diffusiongroup1core))
            Agroup1[i][i+1] = localinput3 * ((((-2)*diffusiongroup1core*diffusiongroup1reflector))/(diffusiongroup1core + diffusiongroup1reflector))

            Agroup2[i][i] = (localinput2 * .5 * (((2*diffusiongroup2core*diffusiongroup2reflector)/(diffusiongroup2core + diffusiongroup2reflector)) + ((2*(diffusiongroup2core**2))/(2*diffusiongroup2core))     ))   + group2absorptioncore + scattering2to1core
            Agroup2[i][i-1] = (localinput1 * (((-2)*(diffusiongroup2core**2))/(2*diffusiongroup2core)) ) 
            Agroup2[i][i+1] = localinput3 * ((((-2)*diffusiongroup2core*diffusiongroup2reflector))/(diffusiongroup2core + diffusiongroup2reflector))     
        elif (((i)/n) >= (diameterreactorcore/diameterreflector) and ((i-1)/n) < (diameterreactorcore/diameterreflector)):
            localinput1 = (((diameterreflector * (i-.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
            localinput2 = ((1) * (((diameterreflector * (i-.5))/(2 * n)) + ((diameterreflector * (i+.5))/(2 * n))   )      )/( ((diameterreflector * i)/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
            localinput3 = (  ((diameterreflector * (i+.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
            Agroup1[i][i] = (localinput2 * .5 * (((2*diffusiongroup1core*diffusiongroup1reflector)/(diffusiongroup1core + diffusiongroup1reflector)) + ((2*(diffusiongroup1reflector**2))/(2*diffusiongroup1reflector))     )   )   + group1absorptionreflector + scattering1to2reflector
            Agroup1[i][i-1] = localinput1 * ((-(2*diffusiongroup1core*diffusiongroup1reflector))/(diffusiongroup1core + diffusiongroup1reflector))
            Agroup1[i][i+1] = localinput3 * ((-2*(diffusiongroup1reflector**2))/(2*diffusiongroup1reflector))

            Agroup2[i][i] = localinput2 * .5 * (((2*diffusiongroup2core*diffusiongroup2reflector)/(diffusiongroup2core + diffusiongroup2reflector)) + ((2*(diffusiongroup2reflector**2))/(2*diffusiongroup2reflector))     ) + group2absorptionreflector + scattering2to1reflector
            Agroup2[i][i-1] = localinput1 * ((-(2*diffusiongroup2core*diffusiongroup2reflector))/(diffusiongroup2core + diffusiongroup2reflector))
            Agroup2[i][i+1] = localinput3 * ((-2*(diffusiongroup2reflector**2))/(2*diffusiongroup2reflector))             
        elif ((i+1)/n) > (diameterreactorcore/diameterreflector):
            diffusiongroup1 = diffusiongroup1reflector
            diffusiongroup2 = diffusiongroup2reflector
            if i == 0:
                localinput1 =   (((diameterreflector * (i+.0001))/(2 * n)))/( ((diameterreflector * (i + .0001))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                localinput2 = ((diameterreflector * (i+.5))/(2 * n))/( ((diameterreflector * (i + .0001))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                Agroup1[0][0] = localinput1 * (-diffusiongroup1) + group1absorptionreflector + scattering1to2reflector
                Agroup1[0][1] = localinput2 * (-diffusiongroup1)
                Agroup2[0][0] = localinput1 * (-diffusiongroup2) + group2absorptionreflector + scattering2to1reflector
                Agroup2[0][1] = localinput2 * (-diffusiongroup2)           

            elif(i > 0 and i < n-1):           
                localinput1 = (((diameterreflector * (i-.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
                localinput2 = ((-1) * (((diameterreflector * (i-.5))/(2 * n)) + ((diameterreflector * (i+.5))/(2 * n))   )      )/( ((diameterreflector * i)/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
                localinput3 = (  ((diameterreflector * (i+.5))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n)) * (((diameterreflector/(2*n)))**2)   )
                Agroup1[i][i] = (localinput2 * (-diffusiongroup1)) + group1absorptionreflector + scattering1to2reflector
                Agroup1[i][i-1] = localinput1 * (-diffusiongroup1)
                Agroup1[i][i+1] = localinput3 * (-diffusiongroup1)
                Agroup2[i][i] = (localinput2 * (-diffusiongroup2)) + group2absorptionreflector + scattering2to1reflector
                Agroup2[i][i-1] = localinput1 * (-diffusiongroup2)
                Agroup2[i][i+1] = localinput3 * (-diffusiongroup2)            
            elif i == n-1:
                localinput2 = (     ((diameterreflector * (i-1))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                localinput3 = (     (-3)*((diameterreflector * (i))/(2 * n))      )/( ((diameterreflector * (i))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                Agroup1[n-1][n-2] = localinput2 * (-diffusiongroup1)
                Agroup1[n-1][n-1] = (localinput3 * (-diffusiongroup1)) + group1absorptionreflector + scattering1to2reflector
                Agroup2[n-1][n-2] = localinput2 * (-diffusiongroup2)
                Agroup2[n-1][n-1] = (localinput3 * (-diffusiongroup2)) + group2absorptionreflector + scattering2to1reflector
    '''

    group1scatteringcore = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[7]) + (
                numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[7]) + (
                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[7]) + (
                                       ((numberdensitywater * 2)) * (10 ** -24) * hs[7]) + (
                                       numberdensitycladding * (10 ** -24) * zr90s[7])

    group1scatteringreflector = (numberdensityreflector * (10 ** -24) * bes[7])

    scattering1to2core = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[7] * (
                math.log(u235ebar) / math.log(.44))) + (
                                     numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[7] * (
                                         math.log(u238ebar) / math.log(.44))) + (
                                     (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[7] * (
                                         math.log(oebar) / math.log(.44))) + (
                                     ((numberdensitywater * 2)) * (10 ** -24) * hs[7] * (
                                         math.log(hebar) / math.log(.44))) + (
                                     numberdensitycladding * (10 ** -24) * zr90s[7] * (
                                         math.log(zr90ebar) / math.log(.44)))

    scattering1to2reflector = (numberdensityreflector * (10 ** -24) * bes[7] * (math.log(beebar) / math.log(.44)))

    # group1absorptioncore = (numberdensityu235 * (10**-24) * u235a[7]) + (numberdensityu238 * (10**-24) * u238a[7]) + (numberdensitypu239 * (10**-24) * pu239c[7]) + ((numberdensitywater + (numberdensityuo2fuel * 2)) * (10**-24) * oa[7]  ) + ( ((numberdensitywater * 2)) * (10**-24) * ha[7]  ) + (numberdensitycladding * (10**-24) * zr90a[7])

    group1absorptionreflector = (numberdensityreflector * (10 ** -24) * bea[7])

    group2scatteringcore = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[6]) + (
                numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[6]) + (
                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[6]) + (
                                       ((numberdensitywater * 2)) * (10 ** -24) * hs[6]) + (
                                       numberdensitycladding * (10 ** -24) * zr90s[6])

    group2scatteringreflector = (numberdensityreflector * (10 ** -24) * bes[6])

    scattering2to3core = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[6] * (
                math.log(u235ebar) / math.log(.0363636))) + (
                                     numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[6] * (
                                         math.log(u238ebar) / math.log(.0363636))) + (
                                     (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[6] * (
                                         math.log(oebar) / math.log(.0363636))) + (
                                     ((numberdensitywater * 2)) * (10 ** -24) * hs[6] * (
                                         math.log(hebar) / math.log(.0363636))) + (
                                     numberdensitycladding * (10 ** -24) * zr90s[6] * (
                                         math.log(zr90ebar) / math.log(.0363636)))

    scattering2to3reflector = (numberdensityreflector * (10 ** -24) * bes[6] * (math.log(beebar) / math.log(.0363636)))

    # group2absorptioncore = (numberdensityu235 * (10**-24) * u235a[6]) + (numberdensityu238 * (10**-24) * u238a[6]) + (numberdensitypu239 * (10**-24) * pu239c[6]) + ((numberdensitywater + (numberdensityuo2fuel * 2)) * (10**-24) * oa[6]  ) + ( ((numberdensitywater * 2)) * (10**-24) * ha[6]  ) + (numberdensitycladding * (10**-24) * zr90a[6])

    group2absorptionreflector = (numberdensityreflector * (10 ** -24) * bea[6])

    group3scatteringcore = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[5]) + (
                numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[5]) + (
                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[5]) + (
                                       ((numberdensitywater * 2)) * (10 ** -24) * hs[5]) + (
                                       numberdensitycladding * (10 ** -24) * zr90s[5])

    group3scatteringreflector = (numberdensityreflector * (10 ** -24) * bes[5])

    scattering3to4core = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[5] * (
                math.log(u235ebar) / math.log(.01))) + (
                                     numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[5] * (
                                         math.log(u238ebar) / math.log(.01))) + (
                                     (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[5] * (
                                         math.log(oebar) / math.log(.01))) + (
                                     ((numberdensitywater * 2)) * (10 ** -24) * hs[5] * (
                                         math.log(hebar) / math.log(.01))) + (
                                     numberdensitycladding * (10 ** -24) * zr90s[5] * (
                                         math.log(zr90ebar) / math.log(.01)))

    scattering3to4reflector = (numberdensityreflector * (10 ** -24) * bes[5] * (math.log(beebar) / math.log(.01)))

    # group3absorptioncore = (numberdensityu235 * (10**-24) * u235a[5]) + (numberdensityu238 * (10**-24) * u238a[5]) + (numberdensitypu239 * (10**-24) * pu239c[5]) + ((numberdensitywater + (numberdensityuo2fuel * 2)) * (10**-24) * oa[5]  ) + ( ((numberdensitywater * 2)) * (10**-24) * ha[5]  ) + (numberdensitycladding * (10**-24) * zr90a[5])

    group3absorptionreflector = (numberdensityreflector * (10 ** -24) * bea[5])

    group4scatteringcore = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[4]) + (
                numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[4]) + (
                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[4]) + (
                                       ((numberdensitywater * 2)) * (10 ** -24) * hs[4]) + (
                                       numberdensitycladding * (10 ** -24) * zr90s[4])

    group4scatteringreflector = (numberdensityreflector * (10 ** -24) * bes[4])

    scattering4to5core = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[4] * (
                math.log(u235ebar) / math.log(.01))) + (
                                     numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[4] * (
                                         math.log(u238ebar) / math.log(.01))) + (
                                     (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[4] * (
                                         math.log(oebar) / math.log(.01))) + (
                                     ((numberdensitywater * 2)) * (10 ** -24) * hs[4] * (
                                         math.log(hebar) / math.log(.01))) + (
                                     numberdensitycladding * (10 ** -24) * zr90s[4] * (
                                         math.log(zr90ebar) / math.log(.01)))

    scattering4to5reflector = (numberdensityreflector * (10 ** -24) * bes[4] * (math.log(beebar) / math.log(.01)))

    # group4absorptioncore = (numberdensityu235 * (10**-24) * u235a[4]) + (numberdensityu238 * (10**-24) * u238a[4]) + (numberdensitypu239 * (10**-24) * pu239c[4]) + ((numberdensitywater + (numberdensityuo2fuel * 2)) * (10**-24) * oa[4]  ) + ( ((numberdensitywater * 2)) * (10**-24) * ha[4]  ) + (numberdensitycladding * (10**-24) * zr90a[4])

    group4absorptionreflector = (numberdensityreflector * (10 ** -24) * bea[4])

    group5scatteringcore = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[3]) + (
                numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[3]) + (
                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[3]) + (
                                       ((numberdensitywater * 2)) * (10 ** -24) * hs[3]) + (
                                       numberdensitycladding * (10 ** -24) * zr90s[3])

    group5scatteringreflector = (numberdensityreflector * (10 ** -24) * bes[3])

    scattering5to6core = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[3] * (
                math.log(u235ebar) / math.log(.03083))) + (
                                     numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[3] * (
                                         math.log(u238ebar) / math.log(.03083))) + (
                                     (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[3] * (
                                         math.log(oebar) / math.log(.03083))) + (
                                     ((numberdensitywater * 2)) * (10 ** -24) * hs[3] * (
                                         math.log(hebar) / math.log(.03083))) + (
                                     numberdensitycladding * (10 ** -24) * zr90s[3] * (
                                         math.log(zr90ebar) / math.log(.03083)))

    scattering5to6reflector = (numberdensityreflector * (10 ** -24) * bes[3] * (math.log(beebar) / math.log(.03083)))

    # group5absorptioncore = (numberdensityu235 * (10**-24) * u235a[3]) + (numberdensityu238 * (10**-24) * u238a[3]) + (numberdensitypu239 * (10**-24) * pu239c[3]) + ((numberdensitywater + (numberdensityuo2fuel * 2)) * (10**-24) * oa[3]  ) + ( ((numberdensitywater * 2)) * (10**-24) * ha[3]  ) + (numberdensitycladding * (10**-24) * zr90a[3])

    group5absorptionreflector = (numberdensityreflector * (10 ** -24) * bea[3])

    group6scatteringcore = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[2]) + (
                numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[2]) + (
                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[2]) + (
                                       ((numberdensitywater * 2)) * (10 ** -24) * hs[2]) + (
                                       numberdensitycladding * (10 ** -24) * zr90s[2])

    group6scatteringreflector = (numberdensityreflector * (10 ** -24) * bes[2])

    scattering6to7core = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[2] * (
                math.log(u235ebar) / math.log(.1))) + (
                                     numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[2] * (
                                         math.log(u238ebar) / math.log(.1))) + (
                                     (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[2] * (
                                         math.log(oebar) / math.log(.1))) + (
                                     ((numberdensitywater * 2)) * (10 ** -24) * hs[2] * (
                                         math.log(hebar) / math.log(.1))) + (
                                     numberdensitycladding * (10 ** -24) * zr90s[2] * (
                                         math.log(zr90ebar) / math.log(.1)))

    scattering6to7reflector = (numberdensityreflector * (10 ** -24) * bes[2] * (math.log(beebar) / math.log(.1)))

    # group6absorptioncore = (numberdensityu235 * (10**-24) * u235a[2]) + (numberdensityu238 * (10**-24) * u238a[2]) + (numberdensitypu239 * (10**-24) * pu239c[2]) + ((numberdensitywater + (numberdensityuo2fuel * 2)) * (10**-24) * oa[2]  ) + ( ((numberdensitywater * 2)) * (10**-24) * ha[2]  ) + (numberdensitycladding * (10**-24) * zr90a[2])

    group6absorptionreflector = (numberdensityreflector * (10 ** -24) * bea[2])

    group7scatteringcore = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[1]) + (
                numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[1]) + (
                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[1]) + (
                                       ((numberdensitywater * 2)) * (10 ** -24) * hs[1]) + (
                                       numberdensitycladding * (10 ** -24) * zr90s[1])

    group7scatteringreflector = (numberdensityreflector * (10 ** -24) * bes[1])

    scattering7to8core = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[1] * (
                math.log(u235ebar) / math.log(.1))) + (
                                     numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[1] * (
                                         math.log(u238ebar) / math.log(.1))) + (
                                     (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[1] * (
                                         math.log(oebar) / math.log(.1))) + (
                                     ((numberdensitywater * 2)) * (10 ** -24) * hs[1] * (
                                         math.log(hebar) / math.log(.1))) + (
                                     numberdensitycladding * (10 ** -24) * zr90s[1] * (
                                         math.log(zr90ebar) / math.log(.1)))

    scattering7to8reflector = (numberdensityreflector * (10 ** -24) * bes[1] * (math.log(beebar) / math.log(.1)))

    # group7absorptioncore = (numberdensityu235 * (10**-24) * u235a[1]) + (numberdensityu238 * (10**-24) * u238a[1]) + (numberdensitypu239 * (10**-24) * pu239c[1]) + ((numberdensitywater + (numberdensityuo2fuel * 2)) * (10**-24) * oa[1]  ) + ( ((numberdensitywater * 2)) * (10**-24) * ha[1]  ) + (numberdensitycladding * (10**-24) * zr90a[1])

    group7absorptionreflector = (numberdensityreflector * (10 ** -24) * bea[1])

    group8scatteringcore = (numberdensityuo2fuel * uraniumenrichment * (10 ** -24) * u235s[0]) + (
                numberdensityuo2fuel * (1 - uraniumenrichment) * (10 ** -24) * u238s[0]) + (
                                       (numberdensitywater + (numberdensityuo2fuel * 2)) * (10 ** -24) * os[0]) + (
                                       ((numberdensitywater * 2)) * (10 ** -24) * hs[0]) + (
                                       numberdensitycladding * (10 ** -24) * zr90s[0])

    group8scatteringreflector = (numberdensityreflector * (10 ** -24) * bes[0])

    # group8absorptioncore = (numberdensityu235 * (10**-24) * u235a[0]) + (numberdensityu238 * (10**-24) * u238a[0]) + (numberdensitypu239 * (10**-24) * pu239c[0]) + ((numberdensitywater + (numberdensityuo2fuel * 2)) * (10**-24) * oa[0]  ) + ( ((numberdensitywater * 2)) * (10**-24) * ha[0]  ) + (numberdensitycladding * (10**-24) * zr90a[0])

    group8absorptionreflector = (numberdensityreflector * (10 ** -24) * bea[0])

    diffusiongroup1core = 1 / (3 * group1scatteringcore)  # cm
    diffusiongroup1reflector = 1 / (3 * group1scatteringreflector)  # cm

    diffusiongroup2core = 1 / (3 * group2scatteringcore)  # cm
    diffusiongroup2reflector = 1 / (3 * group2scatteringreflector)  # cm

    diffusiongroup3core = 1 / (3 * group3scatteringcore)  # cm
    diffusiongroup3reflector = 1 / (3 * group3scatteringreflector)  # cm

    diffusiongroup4core = 1 / (3 * group4scatteringcore)  # cm
    diffusiongroup4reflector = 1 / (3 * group4scatteringreflector)  # cm

    diffusiongroup5core = 1 / (3 * group5scatteringcore)  # cm
    diffusiongroup5reflector = 1 / (3 * group5scatteringreflector)  # cm

    diffusiongroup6core = 1 / (3 * group6scatteringcore)  # cm
    diffusiongroup6reflector = 1 / (3 * group6scatteringreflector)  # cm

    diffusiongroup7core = 1 / (3 * group7scatteringcore)  # cm
    diffusiongroup7reflector = 1 / (3 * group7scatteringreflector)  # cm

    diffusiongroup8core = 1 / (3 * group8scatteringcore)  # cm
    diffusiongroup8reflector = 1 / (3 * group8scatteringreflector)  # cm

    for i in range(n):
        if ((i + 1) / n) < (diameterreactorcore / diameterreflector):
            diffusiongroup1 = diffusiongroup1core
            diffusiongroup2 = diffusiongroup2core
            diffusiongroup3 = diffusiongroup3core
            diffusiongroup4 = diffusiongroup4core
            diffusiongroup5 = diffusiongroup5core
            diffusiongroup6 = diffusiongroup6core
            diffusiongroup7 = diffusiongroup7core
            diffusiongroup8 = diffusiongroup8core
            if i == 0:
                # localinput1 =   (((diameterreflector * (i+.0001))/(2 * n)))/( ((diameterreflector * (i + .0001))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                # localinput2 = ((diameterreflector * (i+.5))/(2 * n))/( ((diameterreflector * (i + .0001))/(2 * n))  *    (((diameterreflector/(2*n)))**2)      )
                localinput1 = (((diameterreflector * (i + .5)) / (2 * n))) / (
                            ((diameterreflector * (i + .0001)) / (2 * n)) * (((diameterreflector / (2 * n))) ** 2))
                localinput2 = ((diameterreflector * (i + .5)) / (2 * n)) / (
                            ((diameterreflector * (i + .0001)) / (2 * n)) * (((diameterreflector / (2 * n))) ** 2))
                Agroup1[0][0] = (localinput1 * (diffusiongroup1)) + group1absorptioncore[averageindexaxial][
                    i] + scattering1to2core
                Agroup1[0][1] = (localinput2 * (-diffusiongroup1))
                Agroup2[0][0] = (localinput1 * (diffusiongroup2)) + group2absorptioncore[averageindexaxial][
                    i] + scattering2to3core
                Agroup2[0][1] = (localinput2 * (-diffusiongroup2))

                Agroup3[0][0] = (localinput1 * (diffusiongroup3)) + group3absorptioncore[averageindexaxial][
                    i] + scattering3to4core
                Agroup3[0][1] = (localinput2 * (-diffusiongroup3))
                Agroup4[0][0] = (localinput1 * (diffusiongroup4)) + group4absorptioncore[averageindexaxial][
                    i] + scattering4to5core
                Agroup4[0][1] = (localinput2 * (-diffusiongroup4))

                Agroup5[0][0] = (localinput1 * (diffusiongroup5)) + group5absorptioncore[averageindexaxial][
                    i] + scattering5to6core
                Agroup5[0][1] = (localinput2 * (-diffusiongroup5))
                Agroup6[0][0] = (localinput1 * (diffusiongroup6)) + group6absorptioncore[averageindexaxial][
                    i] + scattering6to7core
                Agroup6[0][1] = (localinput2 * (-diffusiongroup6))

                Agroup7[0][0] = (localinput1 * (diffusiongroup7)) + group7absorptioncore[averageindexaxial][
                    i] + scattering7to8core
                Agroup7[0][1] = (localinput2 * (-diffusiongroup7))
                Agroup8[0][0] = (localinput1 * (diffusiongroup8)) + group8absorptioncore[averageindexaxial][i]
                Agroup8[0][1] = (localinput2 * (-diffusiongroup8))



            elif (i > 0 and i < n - 1):
                localinput1 = (((diameterreflector * (i - 1)) / (2 * n))) / (
                            ((diameterreflector * (i)) / (2 * n)) * (((diameterreflector / (2 * n))) ** 2))
                localinput2 = ((-1) * (((diameterreflector * (i - .5)) / (2 * n)) + (
                            (diameterreflector * (i + .5)) / (2 * n)))) / (
                                          ((diameterreflector * i) / (2 * n)) * (((diameterreflector / (2 * n))) ** 2))
                localinput3 = (((diameterreflector * (i + 1)) / (2 * n))) / (
                            ((diameterreflector * (i)) / (2 * n)) * (((diameterreflector / (2 * n))) ** 2))
                Agroup1[i][i] = (localinput2 * (-diffusiongroup1)) + group1absorptioncore[averageindexaxial][
                    i] + scattering1to2core
                Agroup1[i][i - 1] = (localinput1 * (-diffusiongroup1))
                Agroup1[i][i + 1] = localinput3 * (-diffusiongroup1)
                Agroup2[i][i] = (localinput2 * (-diffusiongroup2)) + group2absorptioncore[averageindexaxial][
                    i] + scattering2to3core
                Agroup2[i][i - 1] = (localinput1 * (-diffusiongroup2))
                Agroup2[i][i + 1] = localinput3 * (-diffusiongroup2)
                Agroup3[i][i] = (localinput2 * (-diffusiongroup3)) + group3absorptioncore[averageindexaxial][
                    i] + scattering3to4core
                Agroup3[i][i - 1] = (localinput1 * (-diffusiongroup3))
                Agroup3[i][i + 1] = localinput3 * (-diffusiongroup3)
                Agroup4[i][i] = (localinput2 * (-diffusiongroup4)) + group4absorptioncore[averageindexaxial][
                    i] + scattering4to5core
                Agroup4[i][i - 1] = (localinput1 * (-diffusiongroup4))
                Agroup4[i][i + 1] = localinput3 * (-diffusiongroup4)
                Agroup5[i][i] = (localinput2 * (-diffusiongroup5)) + group5absorptioncore[averageindexaxial][
                    i] + scattering5to6core
                Agroup5[i][i - 1] = (localinput1 * (-diffusiongroup5))
                Agroup5[i][i + 1] = localinput3 * (-diffusiongroup5)
                Agroup6[i][i] = (localinput2 * (-diffusiongroup6)) + group6absorptioncore[averageindexaxial][
                    i] + scattering6to7core
                Agroup6[i][i - 1] = (localinput1 * (-diffusiongroup6))
                Agroup6[i][i + 1] = localinput3 * (-diffusiongroup6)
                Agroup7[i][i] = (localinput2 * (-diffusiongroup7)) + group7absorptioncore[averageindexaxial][
                    i] + scattering7to8core
                Agroup7[i][i - 1] = (localinput1 * (-diffusiongroup7))
                Agroup7[i][i + 1] = localinput3 * (-diffusiongroup7)
                Agroup8[i][i] = (localinput2 * (-diffusiongroup8)) + group8absorptioncore[averageindexaxial][i]
                Agroup8[i][i - 1] = (localinput1 * (-diffusiongroup8))
                Agroup8[i][i + 1] = localinput3 * (-diffusiongroup8)




            elif i == n - 1:
                localinput2 = (((diameterreflector * (i - 1)) / (2 * n))) / (
                            ((diameterreflector * (i)) / (2 * n)) * (((diameterreflector / (2 * n))) ** 2))
                localinput3 = ((-3) * ((diameterreflector * (i)) / (2 * n))) / (
                            ((diameterreflector * (i)) / (2 * n)) * (((diameterreflector / (2 * n))) ** 2))
                Agroup1[n - 1][n - 2] = localinput2 * (-diffusiongroup1)
                Agroup1[n - 1][n - 1] = (localinput3 * (-diffusiongroup1)) + group1absorptioncore[averageindexaxial][
                    i] + scattering1to2core
                Agroup2[n - 1][n - 2] = localinput2 * (-diffusiongroup2)
                Agroup2[n - 1][n - 1] = (localinput3 * (-diffusiongroup2)) + group2absorptioncore[averageindexaxial][
                    i] + scattering2to3core
                Agroup3[n - 1][n - 2] = localinput2 * (-diffusiongroup3)
                Agroup3[n - 1][n - 1] = (localinput3 * (-diffusiongroup3)) + group3absorptioncore[averageindexaxial][
                    i] + scattering3to4core
                Agroup4[n - 1][n - 2] = localinput2 * (-diffusiongroup4)
                Agroup4[n - 1][n - 1] = (localinput3 * (-diffusiongroup4)) + group4absorptioncore[averageindexaxial][
                    i] + scattering4to5core
                Agroup5[n - 1][n - 2] = localinput2 * (-diffusiongroup5)
                Agroup5[n - 1][n - 1] = (localinput3 * (-diffusiongroup5)) + group5absorptioncore[averageindexaxial][
                    i] + scattering5to6core
                Agroup6[n - 1][n - 2] = localinput2 * (-diffusiongroup6)
                Agroup6[n - 1][n - 1] = (localinput3 * (-diffusiongroup6)) + group6absorptioncore[averageindexaxial][
                    i] + scattering6to7core
                Agroup7[n - 1][n - 2] = localinput2 * (-diffusiongroup7)
                Agroup7[n - 1][n - 1] = (localinput3 * (-diffusiongroup7)) + group7absorptioncore[averageindexaxial][
                    i] + scattering7to8core
                Agroup8[n - 1][n - 2] = localinput2 * (-diffusiongroup8)
                Agroup8[n - 1][n - 1] = (localinput3 * (-diffusiongroup8)) + group8absorptioncore[averageindexaxial][i]


        elif (((i + 1) / n) >= (diameterreactorcore / diameterreflector) and (i / n) < (
                diameterreactorcore / diameterreflector)):
            localinput1 = (((diameterreflector * (i - 1)) / (2 * n))) / (
                        ((diameterreflector * (i)) / (2 * n)) * (((diameterreflector / (2 * n))) ** 2))
            localinput2 = (
                          (((diameterreflector * (i - .5)) / (2 * n)) + ((diameterreflector * (i + .5)) / (2 * n)))) / (
                                      ((diameterreflector * i) / (2 * n)) * (((diameterreflector / (2 * n))) ** 2))
            localinput3 = (((diameterreflector * (i + 1)) / (2 * n))) / (
                        ((diameterreflector * (i)) / (2 * n)) * (((diameterreflector / (2 * n))) ** 2))
            Agroup1[i][i] = (localinput2 * .5 * (((2 * diffusiongroup1core * diffusiongroup1reflector) / (
                        diffusiongroup1core + diffusiongroup1reflector)) + ((2 * (diffusiongroup1core ** 2)) / (
                        2 * diffusiongroup1core)))) + group1absorptioncore[averageindexaxial][i] + scattering1to2core
            Agroup1[i][i - 1] = localinput1 * (((-2) * (diffusiongroup1core ** 2)) / (2 * diffusiongroup1core))
            Agroup1[i][i + 1] = localinput3 * ((((-2) * diffusiongroup1core * diffusiongroup1reflector)) / (
                        diffusiongroup1core + diffusiongroup1reflector))

            Agroup2[i][i] = (localinput2 * .5 * (((2 * diffusiongroup2core * diffusiongroup2reflector) / (
                        diffusiongroup2core + diffusiongroup2reflector)) + ((2 * (diffusiongroup2core ** 2)) / (
                        2 * diffusiongroup2core)))) + group2absorptioncore[averageindexaxial][i] + scattering2to3core
            Agroup2[i][i - 1] = (localinput1 * (((-2) * (diffusiongroup2core ** 2)) / (2 * diffusiongroup2core)))
            Agroup2[i][i + 1] = localinput3 * ((((-2) * diffusiongroup2core * diffusiongroup2reflector)) / (
                        diffusiongroup2core + diffusiongroup2reflector))

            Agroup3[i][i] = (localinput2 * .5 * (((2 * diffusiongroup3core * diffusiongroup3reflector) / (
                        diffusiongroup3core + diffusiongroup3reflector)) + ((2 * (diffusiongroup3core ** 2)) / (
                        2 * diffusiongroup3core)))) + group3absorptioncore[averageindexaxial][i] + scattering3to4core
            Agroup3[i][i - 1] = localinput1 * (((-2) * (diffusiongroup3core ** 2)) / (2 * diffusiongroup3core))
            Agroup3[i][i + 1] = localinput3 * ((((-2) * diffusiongroup3core * diffusiongroup3reflector)) / (
                        diffusiongroup3core + diffusiongroup3reflector))

            Agroup4[i][i] = (localinput2 * .5 * (((2 * diffusiongroup4core * diffusiongroup4reflector) / (
                        diffusiongroup4core + diffusiongroup4reflector)) + ((2 * (diffusiongroup4core ** 2)) / (
                        2 * diffusiongroup4core)))) + group4absorptioncore[averageindexaxial][i] + scattering4to5core
            Agroup4[i][i - 1] = (localinput1 * (((-2) * (diffusiongroup4core ** 2)) / (2 * diffusiongroup4core)))
            Agroup4[i][i + 1] = localinput3 * ((((-2) * diffusiongroup4core * diffusiongroup4reflector)) / (
                        diffusiongroup4core + diffusiongroup4reflector))

            Agroup5[i][i] = (localinput2 * .5 * (((2 * diffusiongroup5core * diffusiongroup5reflector) / (
                        diffusiongroup5core + diffusiongroup5reflector)) + ((2 * (diffusiongroup5core ** 2)) / (
                        2 * diffusiongroup5core)))) + group5absorptioncore[averageindexaxial][i] + scattering5to6core
            Agroup5[i][i - 1] = localinput1 * (((-2) * (diffusiongroup5core ** 2)) / (2 * diffusiongroup5core))
            Agroup5[i][i + 1] = localinput3 * ((((-2) * diffusiongroup5core * diffusiongroup5reflector)) / (
                        diffusiongroup5core + diffusiongroup5reflector))

            Agroup6[i][i] = (localinput2 * .5 * (((2 * diffusiongroup6core * diffusiongroup6reflector) / (
                        diffusiongroup6core + diffusiongroup6reflector)) + ((2 * (diffusiongroup6core ** 2)) / (
                        2 * diffusiongroup6core)))) + group6absorptioncore[averageindexaxial][i] + scattering6to7core
            Agroup6[i][i - 1] = localinput1 * (((-2) * (diffusiongroup6core ** 2)) / (2 * diffusiongroup6core))
            Agroup6[i][i + 1] = localinput3 * ((((-2) * diffusiongroup6core * diffusiongroup6reflector)) / (
                        diffusiongroup6core + diffusiongroup6reflector))

            Agroup7[i][i] = (localinput2 * .5 * (((2 * diffusiongroup7core * diffusiongroup7reflector) / (
                        diffusiongroup7core + diffusiongroup7reflector)) + ((2 * (diffusiongroup7core ** 2)) / (
                        2 * diffusiongroup7core)))) + group7absorptioncore[averageindexaxial][i] + scattering7to8core
            Agroup7[i][i - 1] = (localinput1 * (((-2) * (diffusiongroup7core ** 2)) / (2 * diffusiongroup7core)))
            Agroup7[i][i + 1] = localinput3 * ((((-2) * diffusiongroup7core * diffusiongroup7reflector)) / (
                        diffusiongroup7core + diffusiongroup7reflector))

            Agroup8[i][i] = (localinput2 * .5 * (((2 * diffusiongroup8core * diffusiongroup8reflector) / (
                        diffusiongroup8core + diffusiongroup8reflector)) + ((2 * (diffusiongroup8core ** 2)) / (
                        2 * diffusiongroup8core)))) + group8absorptioncore[averageindexaxial][i]
            Agroup8[i][i - 1] = localinput1 * (((-2) * (diffusiongroup8core ** 2)) / (2 * diffusiongroup8core))
            Agroup8[i][i + 1] = localinput3 * ((((-2) * diffusiongroup8core * diffusiongroup8reflector)) / (
                        diffusiongroup8core + diffusiongroup8reflector))




        elif (((i) / n) >= (diameterreactorcore / diameterreflector) and ((i - 1) / n) < (
                diameterreactorcore / diameterreflector)):
            localinput1 = (((diameterreflector * (i - 1)) / (2 * n))) / (
                        ((diameterreflector * (i)) / (2 * n)) * (((diameterreflector / (2 * n))) ** 2))
            localinput2 = ((1) * (
                        ((diameterreflector * (i - .5)) / (2 * n)) + ((diameterreflector * (i + .5)) / (2 * n)))) / (
                                      ((diameterreflector * i) / (2 * n)) * (((diameterreflector / (2 * n))) ** 2))
            localinput3 = (((diameterreflector * (i + 1)) / (2 * n))) / (
                        ((diameterreflector * (i)) / (2 * n)) * (((diameterreflector / (2 * n))) ** 2))
            Agroup1[i][i] = (localinput2 * .5 * (((2 * diffusiongroup1core * diffusiongroup1reflector) / (
                        diffusiongroup1core + diffusiongroup1reflector)) + ((2 * (diffusiongroup1reflector ** 2)) / (
                        2 * diffusiongroup1reflector)))) + group1absorptionreflector + scattering1to2reflector
            Agroup1[i][i - 1] = localinput1 * ((-(2 * diffusiongroup1core * diffusiongroup1reflector)) / (
                        diffusiongroup1core + diffusiongroup1reflector))
            Agroup1[i][i + 1] = localinput3 * ((-2 * (diffusiongroup1reflector ** 2)) / (2 * diffusiongroup1reflector))

            Agroup2[i][i] = localinput2 * .5 * (((2 * diffusiongroup2core * diffusiongroup2reflector) / (
                        diffusiongroup2core + diffusiongroup2reflector)) + ((2 * (diffusiongroup2reflector ** 2)) / (
                        2 * diffusiongroup2reflector))) + group2absorptionreflector + scattering2to3reflector
            Agroup2[i][i - 1] = localinput1 * ((-(2 * diffusiongroup2core * diffusiongroup2reflector)) / (
                        diffusiongroup2core + diffusiongroup2reflector))
            Agroup2[i][i + 1] = localinput3 * ((-2 * (diffusiongroup2reflector ** 2)) / (2 * diffusiongroup2reflector))

            Agroup3[i][i] = localinput2 * .5 * (((2 * diffusiongroup3core * diffusiongroup3reflector) / (
                        diffusiongroup3core + diffusiongroup3reflector)) + ((2 * (diffusiongroup3reflector ** 2)) / (
                        2 * diffusiongroup3reflector))) + group3absorptionreflector + scattering3to4reflector
            Agroup3[i][i - 1] = localinput1 * ((-(2 * diffusiongroup3core * diffusiongroup3reflector)) / (
                        diffusiongroup3core + diffusiongroup3reflector))
            Agroup3[i][i + 1] = localinput3 * ((-2 * (diffusiongroup3reflector ** 2)) / (2 * diffusiongroup3reflector))

            Agroup4[i][i] = localinput2 * .5 * (((2 * diffusiongroup4core * diffusiongroup4reflector) / (
                        diffusiongroup4core + diffusiongroup4reflector)) + ((2 * (diffusiongroup4reflector ** 2)) / (
                        2 * diffusiongroup4reflector))) + group4absorptionreflector + scattering4to5reflector
            Agroup4[i][i - 1] = localinput1 * ((-(2 * diffusiongroup4core * diffusiongroup4reflector)) / (
                        diffusiongroup4core + diffusiongroup4reflector))
            Agroup4[i][i + 1] = localinput3 * ((-2 * (diffusiongroup4reflector ** 2)) / (2 * diffusiongroup4reflector))

            Agroup5[i][i] = localinput2 * .5 * (((2 * diffusiongroup5core * diffusiongroup5reflector) / (
                        diffusiongroup5core + diffusiongroup5reflector)) + ((2 * (diffusiongroup5reflector ** 2)) / (
                        2 * diffusiongroup5reflector))) + group5absorptionreflector + scattering5to6reflector
            Agroup5[i][i - 1] = localinput1 * ((-(2 * diffusiongroup5core * diffusiongroup5reflector)) / (
                        diffusiongroup5core + diffusiongroup5reflector))
            Agroup5[i][i + 1] = localinput3 * ((-2 * (diffusiongroup5reflector ** 2)) / (2 * diffusiongroup5reflector))

            Agroup6[i][i] = localinput2 * .5 * (((2 * diffusiongroup6core * diffusiongroup6reflector) / (
                        diffusiongroup6core + diffusiongroup6reflector)) + ((2 * (diffusiongroup6reflector ** 2)) / (
                        2 * diffusiongroup6reflector))) + group6absorptionreflector + scattering6to7reflector
            Agroup6[i][i - 1] = localinput1 * ((-(2 * diffusiongroup6core * diffusiongroup6reflector)) / (
                        diffusiongroup6core + diffusiongroup6reflector))
            Agroup6[i][i + 1] = localinput3 * ((-2 * (diffusiongroup6reflector ** 2)) / (2 * diffusiongroup6reflector))

            Agroup7[i][i] = localinput2 * .5 * (((2 * diffusiongroup7core * diffusiongroup7reflector) / (
                        diffusiongroup7core + diffusiongroup7reflector)) + ((2 * (diffusiongroup7reflector ** 2)) / (
                        2 * diffusiongroup7reflector))) + group7absorptionreflector + scattering7to8reflector
            Agroup7[i][i - 1] = localinput1 * ((-(2 * diffusiongroup7core * diffusiongroup7reflector)) / (
                        diffusiongroup7core + diffusiongroup7reflector))
            Agroup7[i][i + 1] = localinput3 * ((-2 * (diffusiongroup7reflector ** 2)) / (2 * diffusiongroup7reflector))

            Agroup8[i][i] = localinput2 * .5 * (((2 * diffusiongroup8core * diffusiongroup8reflector) / (
                        diffusiongroup8core + diffusiongroup8reflector)) + ((2 * (diffusiongroup8reflector ** 2)) / (
                        2 * diffusiongroup8reflector))) + group8absorptionreflector
            Agroup8[i][i - 1] = localinput1 * ((-(2 * diffusiongroup8core * diffusiongroup8reflector)) / (
                        diffusiongroup8core + diffusiongroup8reflector))
            Agroup8[i][i + 1] = localinput3 * ((-2 * (diffusiongroup8reflector ** 2)) / (2 * diffusiongroup8reflector))



        elif ((i + 1) / n) > (diameterreactorcore / diameterreflector):
            diffusiongroup1 = diffusiongroup1reflector
            diffusiongroup2 = diffusiongroup2reflector
            diffusiongroup3 = diffusiongroup3reflector
            diffusiongroup4 = diffusiongroup4reflector
            diffusiongroup5 = diffusiongroup5reflector
            diffusiongroup6 = diffusiongroup6reflector
            diffusiongroup7 = diffusiongroup7reflector
            diffusiongroup8 = diffusiongroup8reflector
            if i == 0:
                localinput1 = (((diameterreflector * (i + .0001)) / (2 * n))) / (
                            ((diameterreflector * (i + .0001)) / (2 * n)) * (((diameterreflector / (2 * n))) ** 2))
                localinput2 = ((diameterreflector * (i + .5)) / (2 * n)) / (
                            ((diameterreflector * (i + .0001)) / (2 * n)) * (((diameterreflector / (2 * n))) ** 2))
                Agroup1[0][0] = localinput1 * (-diffusiongroup1) + group1absorptionreflector + scattering1to2reflector
                Agroup1[0][1] = localinput2 * (-diffusiongroup1)
                Agroup2[0][0] = localinput1 * (-diffusiongroup2) + group2absorptionreflector + scattering2to3reflector
                Agroup2[0][1] = localinput2 * (-diffusiongroup2)
                Agroup3[0][0] = localinput1 * (-diffusiongroup3) + group3absorptionreflector + scattering3to4reflector
                Agroup3[0][1] = localinput2 * (-diffusiongroup3)
                Agroup4[0][0] = localinput1 * (-diffusiongroup4) + group4absorptionreflector + scattering4to5reflector
                Agroup4[0][1] = localinput2 * (-diffusiongroup4)
                Agroup5[0][0] = localinput1 * (-diffusiongroup5) + group5absorptionreflector + scattering5to6reflector
                Agroup5[0][1] = localinput2 * (-diffusiongroup5)
                Agroup6[0][0] = localinput1 * (-diffusiongroup6) + group6absorptionreflector + scattering6to7reflector
                Agroup6[0][1] = localinput2 * (-diffusiongroup6)
                Agroup7[0][0] = localinput1 * (-diffusiongroup7) + group7absorptionreflector + scattering7to8reflector
                Agroup7[0][1] = localinput2 * (-diffusiongroup7)
                Agroup8[0][0] = localinput1 * (-diffusiongroup8) + group8absorptionreflector
                Agroup8[0][1] = localinput2 * (-diffusiongroup8)




            elif (i > 0 and i < n - 1):
                localinput1 = (((diameterreflector * (i - 1)) / (2 * n))) / (
                            ((diameterreflector * (i)) / (2 * n)) * (((diameterreflector / (2 * n))) ** 2))
                localinput2 = ((-1) * (((diameterreflector * (i - .5)) / (2 * n)) + (
                            (diameterreflector * (i + .5)) / (2 * n)))) / (
                                          ((diameterreflector * i) / (2 * n)) * (((diameterreflector / (2 * n))) ** 2))
                localinput3 = (((diameterreflector * (i + 1)) / (2 * n))) / (
                            ((diameterreflector * (i)) / (2 * n)) * (((diameterreflector / (2 * n))) ** 2))
                Agroup1[i][i] = (localinput2 * (-diffusiongroup1)) + group1absorptionreflector + scattering1to2reflector
                Agroup1[i][i - 1] = localinput1 * (-diffusiongroup1)
                Agroup1[i][i + 1] = localinput3 * (-diffusiongroup1)
                Agroup2[i][i] = (localinput2 * (-diffusiongroup2)) + group2absorptionreflector + scattering2to3reflector
                Agroup2[i][i - 1] = localinput1 * (-diffusiongroup2)
                Agroup2[i][i + 1] = localinput3 * (-diffusiongroup2)
                Agroup3[i][i] = (localinput2 * (-diffusiongroup3)) + group3absorptionreflector + scattering3to4reflector
                Agroup3[i][i - 1] = localinput1 * (-diffusiongroup3)
                Agroup3[i][i + 1] = localinput3 * (-diffusiongroup3)
                Agroup4[i][i] = (localinput2 * (-diffusiongroup4)) + group4absorptionreflector + scattering4to5reflector
                Agroup4[i][i - 1] = localinput1 * (-diffusiongroup4)
                Agroup4[i][i + 1] = localinput3 * (-diffusiongroup4)
                Agroup5[i][i] = (localinput2 * (-diffusiongroup5)) + group5absorptionreflector + scattering5to6reflector
                Agroup5[i][i - 1] = localinput1 * (-diffusiongroup5)
                Agroup5[i][i + 1] = localinput3 * (-diffusiongroup5)
                Agroup6[i][i] = (localinput2 * (-diffusiongroup6)) + group6absorptionreflector + scattering6to7reflector
                Agroup6[i][i - 1] = localinput1 * (-diffusiongroup6)
                Agroup6[i][i + 1] = localinput3 * (-diffusiongroup6)
                Agroup7[i][i] = (localinput2 * (-diffusiongroup7)) + group7absorptionreflector + scattering7to8reflector
                Agroup7[i][i - 1] = localinput1 * (-diffusiongroup7)
                Agroup7[i][i + 1] = localinput3 * (-diffusiongroup7)
                Agroup8[i][i] = (localinput2 * (-diffusiongroup8)) + group8absorptionreflector
                Agroup8[i][i - 1] = localinput1 * (-diffusiongroup8)
                Agroup8[i][i + 1] = localinput3 * (-diffusiongroup8)

            elif i == n - 1:
                localinput2 = (((diameterreflector * (i - 1)) / (2 * n))) / (
                            ((diameterreflector * (i)) / (2 * n)) * (((diameterreflector / (2 * n))) ** 2))
                localinput3 = ((-3) * ((diameterreflector * (i)) / (2 * n))) / (
                            ((diameterreflector * (i)) / (2 * n)) * (((diameterreflector / (2 * n))) ** 2))
                Agroup1[n - 1][n - 2] = localinput2 * (-diffusiongroup1)
                Agroup1[n - 1][n - 1] = (localinput3 * (
                    -diffusiongroup1)) + group1absorptionreflector + scattering1to2reflector
                Agroup2[n - 1][n - 2] = localinput2 * (-diffusiongroup2)
                Agroup2[n - 1][n - 1] = (localinput3 * (
                    -diffusiongroup2)) + group2absorptionreflector + scattering2to3reflector
                Agroup3[n - 1][n - 2] = localinput2 * (-diffusiongroup3)
                Agroup3[n - 1][n - 1] = (localinput3 * (
                    -diffusiongroup3)) + group3absorptionreflector + scattering3to4reflector
                Agroup4[n - 1][n - 2] = localinput2 * (-diffusiongroup4)
                Agroup4[n - 1][n - 1] = (localinput3 * (
                    -diffusiongroup4)) + group4absorptionreflector + scattering4to5reflector
                Agroup5[n - 1][n - 2] = localinput2 * (-diffusiongroup5)
                Agroup5[n - 1][n - 1] = (localinput3 * (
                    -diffusiongroup5)) + group5absorptionreflector + scattering5to6reflector
                Agroup6[n - 1][n - 2] = localinput2 * (-diffusiongroup6)
                Agroup6[n - 1][n - 1] = (localinput3 * (
                    -diffusiongroup6)) + group6absorptionreflector + scattering6to7reflector
                Agroup7[n - 1][n - 2] = localinput2 * (-diffusiongroup7)
                Agroup7[n - 1][n - 1] = (localinput3 * (
                    -diffusiongroup7)) + group7absorptionreflector + scattering7to8reflector
                Agroup8[n - 1][n - 2] = localinput2 * (-diffusiongroup8)
                Agroup8[n - 1][n - 1] = (localinput3 * (-diffusiongroup8)) + group8absorptionreflector

                # for j in range(150):
    boolean = True
    while boolean:
        group1production = []
        group2production = []
        group3production = []
        group4production = []
        group5production = []
        group6production = []
        group7production = []
        group8production = []
        for i in range(n):
            if (((i) / (n)) < (diameterreactorcore / diameterreflector)):
                group1production.append([((chi1 / k) * (
                            (nugroup1fission[averageindexaxial][i] * radialfluxdistributiongroup1[i][0]) + (
                                nugroup2fission[averageindexaxial][i] * radialfluxdistributiongroup2[i][0]) +
                            (nugroup3fission[averageindexaxial][i] * radialfluxdistributiongroup3[i][0]) + (
                                        nugroup4fission[averageindexaxial][i] * radialfluxdistributiongroup4[i][0]) +
                            (nugroup5fission[averageindexaxial][i] * radialfluxdistributiongroup5[i][0]) + (
                                        nugroup6fission[averageindexaxial][i] * radialfluxdistributiongroup6[i][0]) +
                            (nugroup7fission[averageindexaxial][i] * radialfluxdistributiongroup7[i][0]) + (
                                        nugroup8fission[averageindexaxial][i] * radialfluxdistributiongroup8[i][0])))
                                         + 0])
            else:
                group1production.append([0])

        radialfluxonenew = np.linalg.solve(np.array(Agroup1), np.array(group1production))

        for i in range(n):
            if (((i) / (n)) < (diameterreactorcore / diameterreflector)):
                group2production.append([((chi2 / k) * (
                            (nugroup1fission[averageindexaxial][i] * radialfluxonenew[i][0]) + (
                                nugroup2fission[averageindexaxial][i] * radialfluxdistributiongroup2[i][0]) +
                            (nugroup3fission[averageindexaxial][i] * radialfluxdistributiongroup3[i][0]) + (
                                        nugroup4fission[averageindexaxial][i] * radialfluxdistributiongroup4[i][0]) +
                            (nugroup5fission[averageindexaxial][i] * radialfluxdistributiongroup5[i][0]) + (
                                        nugroup6fission[averageindexaxial][i] * radialfluxdistributiongroup6[i][0]) +
                            (nugroup7fission[averageindexaxial][i] * radialfluxdistributiongroup7[i][0]) + (
                                        nugroup8fission[averageindexaxial][i] * radialfluxdistributiongroup8[i][0]))) +
                                         (scattering1to2core * radialfluxonenew[i][0])])
            else:
                group2production.append([(scattering1to2reflector * radialfluxonenew[i][0])])

        radialfluxtwonew = np.linalg.solve(np.array(Agroup2), np.array(group2production))

        for i in range(n):
            if (((i) / (n)) < (diameterreactorcore / diameterreflector)):
                group3production.append([((chi3 / k) * (
                            (nugroup1fission[averageindexaxial][i] * radialfluxonenew[i][0]) + (
                                nugroup2fission[averageindexaxial][i] * radialfluxtwonew[i][0]) +
                            (nugroup3fission[averageindexaxial][i] * radialfluxdistributiongroup3[i][0]) + (
                                        nugroup4fission[averageindexaxial][i] * radialfluxdistributiongroup4[i][0]) +
                            (nugroup5fission[averageindexaxial][i] * radialfluxdistributiongroup5[i][0]) + (
                                        nugroup6fission[averageindexaxial][i] * radialfluxdistributiongroup6[i][0]) +
                            (nugroup7fission[averageindexaxial][i] * radialfluxdistributiongroup7[i][0]) + (
                                        nugroup8fission[averageindexaxial][i] * radialfluxdistributiongroup8[i][0]))) +
                                         (scattering2to3core * radialfluxtwonew[i][0])])
            else:
                group3production.append([(scattering2to3reflector * radialfluxtwonew[i][0])])
        radialfluxthreenew = np.linalg.solve(np.array(Agroup3), np.array(group3production))

        for i in range(n):
            if (((i) / (n)) < (diameterreactorcore / diameterreflector)):
                group4production.append([((chi4 / k) * (
                            (nugroup1fission[averageindexaxial][i] * radialfluxonenew[i][0]) + (
                                nugroup2fission[averageindexaxial][i] * radialfluxtwonew[i][0]) +
                            (nugroup3fission[averageindexaxial][i] * radialfluxthreenew[i][0]) + (
                                        nugroup4fission[averageindexaxial][i] * radialfluxdistributiongroup4[i][0]) +
                            (nugroup5fission[averageindexaxial][i] * radialfluxdistributiongroup5[i][0]) + (
                                        nugroup6fission[averageindexaxial][i] * radialfluxdistributiongroup6[i][0]) +
                            (nugroup7fission[averageindexaxial][i] * radialfluxdistributiongroup7[i][0]) + (
                                        nugroup8fission[averageindexaxial][i] * radialfluxdistributiongroup8[i][0]))) +
                                         (scattering3to4core * radialfluxthreenew[i][0])])
            else:
                group4production.append([(scattering3to4reflector * radialfluxthreenew[i][0])])
        radialfluxfournew = np.linalg.solve(np.array(Agroup4), np.array(group4production))

        for i in range(n):
            if (((i) / (n)) < (diameterreactorcore / diameterreflector)):
                group5production.append([((chi5 / k) * (
                            (nugroup1fission[averageindexaxial][i] * radialfluxonenew[i][0]) + (
                                nugroup2fission[averageindexaxial][i] * radialfluxtwonew[i][0]) +
                            (nugroup3fission[averageindexaxial][i] * radialfluxthreenew[i][0]) + (
                                        nugroup4fission[averageindexaxial][i] * radialfluxfournew[i][0]) +
                            (nugroup5fission[averageindexaxial][i] * radialfluxdistributiongroup5[i][0]) + (
                                        nugroup6fission[averageindexaxial][i] * radialfluxdistributiongroup6[i][0]) +
                            (nugroup7fission[averageindexaxial][i] * radialfluxdistributiongroup7[i][0]) + (
                                        nugroup8fission[averageindexaxial][i] * radialfluxdistributiongroup8[i][0]))) +
                                         (scattering4to5core * radialfluxfournew[i][0])])
            else:
                group5production.append([(scattering4to5reflector * radialfluxfournew[i][0])])
        radialfluxfivenew = np.linalg.solve(np.array(Agroup5), np.array(group5production))

        for i in range(n):
            if (((i) / (n)) < (diameterreactorcore / diameterreflector)):
                group6production.append([((chi6 / k) * (
                            (nugroup1fission[averageindexaxial][i] * radialfluxonenew[i][0]) + (
                                nugroup2fission[averageindexaxial][i] * radialfluxtwonew[i][0]) +
                            (nugroup3fission[averageindexaxial][i] * radialfluxthreenew[i][0]) + (
                                        nugroup4fission[averageindexaxial][i] * radialfluxfournew[i][0]) +
                            (nugroup5fission[averageindexaxial][i] * radialfluxfivenew[i][0]) + (
                                        nugroup6fission[averageindexaxial][i] * radialfluxdistributiongroup6[i][0]) +
                            (nugroup7fission[averageindexaxial][i] * radialfluxdistributiongroup7[i][0]) + (
                                        nugroup8fission[averageindexaxial][i] * radialfluxdistributiongroup8[i][0]))) +
                                         (scattering5to6core * radialfluxfivenew[i][0])])
            else:
                group6production.append([(scattering5to6reflector * radialfluxfivenew[i][0])])
        radialfluxsixnew = np.linalg.solve(np.array(Agroup6), np.array(group6production))

        for i in range(n):
            if (((i) / (n)) < (diameterreactorcore / diameterreflector)):
                group7production.append([((chi7 / k) * (
                            (nugroup1fission[averageindexaxial][i] * radialfluxonenew[i][0]) + (
                                nugroup2fission[averageindexaxial][i] * radialfluxtwonew[i][0]) +
                            (nugroup3fission[averageindexaxial][i] * radialfluxthreenew[i][0]) + (
                                        nugroup4fission[averageindexaxial][i] * radialfluxfournew[i][0]) +
                            (nugroup5fission[averageindexaxial][i] * radialfluxfivenew[i][0]) + (
                                        nugroup6fission[averageindexaxial][i] * radialfluxsixnew[i][0]) +
                            (nugroup7fission[averageindexaxial][i] * radialfluxdistributiongroup7[i][0]) + (
                                        nugroup8fission[averageindexaxial][i] * radialfluxdistributiongroup8[i][0]))) +
                                         (scattering6to7core * radialfluxsixnew[i][0])])
            else:
                group7production.append([(scattering6to7reflector * radialfluxsixnew[i][0])])
        radialfluxsevennew = np.linalg.solve(np.array(Agroup7), np.array(group7production))

        for i in range(n):
            if (((i) / (n)) < (diameterreactorcore / diameterreflector)):
                group8production.append([((chi8 / k) * (
                            (nugroup1fission[averageindexaxial][i] * radialfluxonenew[i][0]) + (
                                nugroup2fission[averageindexaxial][i] * radialfluxtwonew[i][0]) +
                            (nugroup3fission[averageindexaxial][i] * radialfluxthreenew[i][0]) + (
                                        nugroup4fission[averageindexaxial][i] * radialfluxfournew[i][0]) +
                            (nugroup5fission[averageindexaxial][i] * radialfluxfivenew[i][0]) + (
                                        nugroup6fission[averageindexaxial][i] * radialfluxsixnew[i][0]) +
                            (nugroup7fission[averageindexaxial][i] * radialfluxsevennew[i][0]) + (
                                        nugroup8fission[averageindexaxial][i] * radialfluxdistributiongroup8[i][0]))) +
                                         (scattering7to8core * radialfluxsevennew[i][0])])
            else:
                group8production.append([(scattering7to8reflector * radialfluxsevennew[i][0])])
        radialfluxeightnew = np.linalg.solve(np.array(Agroup8), np.array(group8production))

        newfluxonesum = 0
        newfluxtwosum = 0
        oldfluxonesum = 0
        oldfluxtwosum = 0

        newfluxthreesum = 0
        newfluxfoursum = 0
        oldfluxthreesum = 0
        oldfluxfoursum = 0

        newfluxfivesum = 0
        newfluxsixsum = 0
        oldfluxfivesum = 0
        oldfluxsixsum = 0

        newfluxsevensum = 0
        newfluxeightsum = 0
        oldfluxsevensum = 0
        oldfluxeightsum = 0

        for i in range(n):
            newfluxonesum = newfluxonesum + (radialfluxonenew[i][0] * deltar * i)
            newfluxtwosum = newfluxtwosum + (radialfluxtwonew[i][0] * deltar * i)
            oldfluxonesum = oldfluxonesum + (radialfluxdistributiongroup1[i][0] * deltar * i)
            oldfluxtwosum = oldfluxtwosum + (radialfluxdistributiongroup2[i][0] * deltar * i)
            newfluxthreesum = newfluxthreesum + (radialfluxthreenew[i][0] * deltar * i)
            newfluxfoursum = newfluxfoursum + (radialfluxfournew[i][0] * deltar * i)
            oldfluxthreesum = oldfluxthreesum + (radialfluxdistributiongroup3[i][0] * deltar * i)
            oldfluxfoursum = oldfluxfoursum + (radialfluxdistributiongroup4[i][0] * deltar * i)
            newfluxfivesum = newfluxfivesum + (radialfluxfivenew[i][0] * deltar * i)
            newfluxsixsum = newfluxsixsum + (radialfluxsixnew[i][0] * deltar * i)
            oldfluxfivesum = oldfluxfivesum + (radialfluxdistributiongroup5[i][0] * deltar * i)
            oldfluxsixsum = oldfluxsixsum + (radialfluxdistributiongroup6[i][0] * deltar * i)
            newfluxsevensum = newfluxsevensum + (radialfluxsevennew[i][0] * deltar * i)
            newfluxeightsum = newfluxeightsum + (radialfluxeightnew[i][0] * deltar * i)
            oldfluxsevensum = oldfluxsevensum + (radialfluxdistributiongroup7[i][0] * deltar * i)
            oldfluxeightsum = oldfluxeightsum + (radialfluxdistributiongroup8[i][0] * deltar * i)

        knew = k * ((
                                newfluxonesum + newfluxtwosum + newfluxthreesum + newfluxfoursum + newfluxfivesum + newfluxsixsum + newfluxsevensum + newfluxeightsum) / (
                                oldfluxonesum + oldfluxtwosum + oldfluxthreesum + oldfluxfoursum + oldfluxfivesum + oldfluxsixsum + oldfluxsevensum + oldfluxeightsum))

        if (abs(knew - k) < (10 ** (-7))):
            boolean = False
        k = knew
        # print(k)
        radialfluxdistributiongroup1 = radialfluxonenew
        radialfluxdistributiongroup2 = radialfluxtwonew
        radialfluxdistributiongroup3 = radialfluxthreenew
        radialfluxdistributiongroup4 = radialfluxfournew
        radialfluxdistributiongroup5 = radialfluxfivenew
        radialfluxdistributiongroup6 = radialfluxsixnew
        radialfluxdistributiongroup7 = radialfluxsevennew
        radialfluxdistributiongroup8 = radialfluxeightnew

    print(k)
    kradialarray.append(k)
    ratio = []
    ratio2 = []
    for i in range(n):
        ratio.append(radialfluxdistributiongroup1[i][0] / axialfluxdistributiongroup1[i][0])
        ratio2.append(radialfluxdistributiongroup2[i][0] / axialfluxdistributiongroup2[i][0])
    print("------------------------")
    # print(ratio[0]/ratio[len(ratio)-1])
    # print(ratio2[0]/ratio2[len(ratio2) -1])

    if (w % 10 == 0 or w == 0):
        plt.plot(radialaxis, radialfluxdistributiongroup1 * (1 / radialfluxdistributiongroup1[0][0]), label="1radial")
        plt.plot(radialaxis, radialfluxdistributiongroup2 * (1 / radialfluxdistributiongroup1[0][0]), label="2radial")
        plt.plot(radialaxis, radialfluxdistributiongroup3 * (1 / radialfluxdistributiongroup1[0][0]), label="3radial")
        plt.plot(radialaxis, radialfluxdistributiongroup4 * (1 / radialfluxdistributiongroup1[0][0]), label="4radial")
        plt.plot(radialaxis, radialfluxdistributiongroup5 * (1 / radialfluxdistributiongroup1[0][0]), label="5radial")
        plt.plot(radialaxis, radialfluxdistributiongroup6 * (1 / radialfluxdistributiongroup1[0][0]), label="6radial")
        plt.plot(radialaxis, radialfluxdistributiongroup7 * (1 / radialfluxdistributiongroup1[0][0]), label="7radial")
        plt.plot(radialaxis, radialfluxdistributiongroup8 * (1 / radialfluxdistributiongroup1[0][0]), label="8radial")

        plt.xlabel("Radius (cm)")
        plt.ylabel("Noyalized Flux (n/(cm^2 * s))")
        plt.title("Radial Flux Distribution in Core and Reflector")
        plt.legend()
        plt.show()

        plt.plot(axialaxis, axialfluxdistributiongroup1 * (1 / axialfluxdistributiongroup1[0][0]), label='1axial')
        plt.plot(axialaxis, axialfluxdistributiongroup2 * (1 / axialfluxdistributiongroup1[0][0]), label='2axial')
        plt.plot(axialaxis, axialfluxdistributiongroup3 * (1 / axialfluxdistributiongroup1[0][0]), label='3axial')
        plt.plot(axialaxis, axialfluxdistributiongroup4 * (1 / axialfluxdistributiongroup1[0][0]), label='4axial')
        plt.plot(axialaxis, axialfluxdistributiongroup5 * (1 / axialfluxdistributiongroup1[0][0]), label='5axial')
        plt.plot(axialaxis, axialfluxdistributiongroup6 * (1 / axialfluxdistributiongroup1[0][0]), label='6axial')
        plt.plot(axialaxis, axialfluxdistributiongroup7 * (1 / axialfluxdistributiongroup1[0][0]), label='7axial')
        plt.plot(axialaxis, axialfluxdistributiongroup8 * (1 / axialfluxdistributiongroup1[0][0]), label='8axial')

        plt.xlabel("Height (cm)")
        plt.ylabel("Normalized Flux (n/(cm^2 * s))")
        plt.title("Axial Flux Distribution in Core and Reflector")
        plt.legend()
        plt.show()

    # plt.plot(axialacomxis,ratio,label="ratio1")
    # plt.plot(axialaxis,ratio2,label="ratio2")
    # plt.show()

    outputfluxdistribution1 = []
    outputfluxdistribution2 = []
    outputfluxdistribution3 = []
    outputfluxdistribution4 = []
    outputfluxdistribution5 = []
    outputfluxdistribution6 = []
    outputfluxdistribution7 = []
    outputfluxdistribution8 = []

    for i in range(n):
        outputfluxdistribution8.append([])
        outputfluxdistribution7.append([])
        outputfluxdistribution6.append([])
        outputfluxdistribution5.append([])
        outputfluxdistribution4.append([])
        outputfluxdistribution3.append([])
        outputfluxdistribution2.append([])
        outputfluxdistribution1.append([])
        for j in range(n):
            outputfluxdistribution8[i].append(
                (axialfluxdistributiongroup8[i][0] / axialfluxdistributiongroup8[0][0]) * (
                            radialfluxdistributiongroup8[j][0] / radialfluxdistributiongroup3[0][0]))
            outputfluxdistribution7[i].append(
                (axialfluxdistributiongroup7[i][0] / axialfluxdistributiongroup7[0][0]) * (
                            radialfluxdistributiongroup7[j][0] / radialfluxdistributiongroup3[0][0]))
            outputfluxdistribution6[i].append(
                (axialfluxdistributiongroup6[i][0] / axialfluxdistributiongroup6[0][0]) * (
                            radialfluxdistributiongroup6[j][0] / radialfluxdistributiongroup3[0][0]))
            outputfluxdistribution5[i].append(
                (axialfluxdistributiongroup5[i][0] / axialfluxdistributiongroup5[0][0]) * (
                            radialfluxdistributiongroup5[j][0] / radialfluxdistributiongroup3[0][0]))
            outputfluxdistribution4[i].append(
                (axialfluxdistributiongroup4[i][0] / axialfluxdistributiongroup4[0][0]) * (
                            radialfluxdistributiongroup4[j][0] / radialfluxdistributiongroup3[0][0]))
            outputfluxdistribution3[i].append(
                (axialfluxdistributiongroup3[i][0] / axialfluxdistributiongroup3[0][0]) * (
                            radialfluxdistributiongroup3[j][0] / radialfluxdistributiongroup3[0][0]))
            outputfluxdistribution2[i].append(
                (axialfluxdistributiongroup2[i][0] / axialfluxdistributiongroup2[0][0]) * (
                            radialfluxdistributiongroup2[j][0] / radialfluxdistributiongroup3[0][0]))
            outputfluxdistribution1[i].append(
                (axialfluxdistributiongroup1[i][0] / axialfluxdistributiongroup1[0][0]) * (
                            radialfluxdistributiongroup1[j][0] / radialfluxdistributiongroup3[0][0]))

    energyproduced = 0
    for i in range(math.ceil(n * (heightreactorcore / heightreflector))):
        for j in range(math.ceil(n * (diameterreactorcore / diameterreflector))):
            # print(outputfluxdistribution1[i][j])
            energyproduced += outputfluxdistribution1[i][j] * group1fission1[i][
                j] * energyperU235fission * deltax * deltar * (deltar * j * 2 * 3.1415) * 2
            energyproduced += outputfluxdistribution2[i][j] * group2fission2[i][
                j] * energyperU235fission * deltax * deltar * (deltar * j * 2 * 3.1415) * 2
            energyproduced += outputfluxdistribution3[i][j] * group3fission3[i][
                j] * energyperU235fission * deltax * deltar * (deltar * j * 2 * 3.1415) * 2
            energyproduced += outputfluxdistribution4[i][j] * group4fission4[i][
                j] * energyperU235fission * deltax * deltar * (deltar * j * 2 * 3.1415) * 2
            energyproduced += outputfluxdistribution5[i][j] * group5fission5[i][
                j] * energyperU235fission * deltax * deltar * (deltar * j * 2 * 3.1415) * 2
            energyproduced += outputfluxdistribution6[i][j] * group6fission6[i][
                j] * energyperU235fission * deltax * deltar * (deltar * j * 2 * 3.1415) * 2
            energyproduced += outputfluxdistribution7[i][j] * group7fission7[i][
                j] * energyperU235fission * deltax * deltar * (deltar * j * 2 * 3.1415) * 2
            energyproduced += outputfluxdistribution8[i][j] * group8fission8[i][
                j] * energyperU235fission * deltax * deltar * (deltar * j * 2 * 3.1415) * 2

    energyproduced = energyproduced * (1.602 * (10 ** (-13)))

    for i in range(n):
        for j in range(n):
            outputfluxdistribution1[i][j] = outputfluxdistribution1[i][j] * ((200 * (10 ** 6)) / (energyproduced))
            outputfluxdistribution2[i][j] = outputfluxdistribution2[i][j] * ((200 * (10 ** 6)) / (energyproduced))
            outputfluxdistribution3[i][j] = outputfluxdistribution3[i][j] * ((200 * (10 ** 6)) / (energyproduced))
            outputfluxdistribution4[i][j] = outputfluxdistribution4[i][j] * ((200 * (10 ** 6)) / (energyproduced))
            outputfluxdistribution5[i][j] = outputfluxdistribution5[i][j] * ((200 * (10 ** 6)) / (energyproduced))
            outputfluxdistribution6[i][j] = outputfluxdistribution6[i][j] * ((200 * (10 ** 6)) / (energyproduced))
            outputfluxdistribution7[i][j] = outputfluxdistribution7[i][j] * ((200 * (10 ** 6)) / (energyproduced))
            outputfluxdistribution8[i][j] = outputfluxdistribution8[i][j] * ((200 * (10 ** 6)) / (energyproduced))

    # u235 dissapear per cm^3

    for i in range(math.ceil(n * (heightreactorcore / heightreflector))):
        for j in range(math.ceil(n * (diameterreactorcore / diameterreflector))):
            u235disappear = 0
            u238disappear = 0
            pu239disappear = 0
            pu239appear = 0
            g154disappear = 0
            g155disappear = 0
            g156disappear = 0
            g157disappear = 0
            g158disappear = 0
            g160disappear = 0

            u235disappear += outputfluxdistribution1[i][j] * u235a[7] * numberdensityu235[i][j] * (
                        10 ** -24) * timeperiteration
            u235disappear += outputfluxdistribution2[i][j] * u235a[6] * numberdensityu235[i][j] * (
                        10 ** -24) * timeperiteration
            u235disappear += outputfluxdistribution3[i][j] * u235a[5] * numberdensityu235[i][j] * (
                        10 ** -24) * timeperiteration
            u235disappear += outputfluxdistribution4[i][j] * u235a[4] * numberdensityu235[i][j] * (
                        10 ** -24) * timeperiteration
            u235disappear += outputfluxdistribution5[i][j] * u235a[3] * numberdensityu235[i][j] * (
                        10 ** -24) * timeperiteration
            u235disappear += outputfluxdistribution6[i][j] * u235a[2] * numberdensityu235[i][j] * (
                        10 ** -24) * timeperiteration
            u235disappear += outputfluxdistribution7[i][j] * u235a[1] * numberdensityu235[i][j] * (
                        10 ** -24) * timeperiteration
            u235disappear += outputfluxdistribution8[i][j] * u235a[0] * numberdensityu235[i][j] * (
                        10 ** -24) * timeperiteration

            u238disappear += outputfluxdistribution1[i][j] * u238a[7] * numberdensityu238[i][j] * (
                        10 ** -24) * timeperiteration
            u238disappear += outputfluxdistribution2[i][j] * u238a[6] * numberdensityu238[i][j] * (
                        10 ** -24) * timeperiteration
            u238disappear += outputfluxdistribution3[i][j] * u238a[5] * numberdensityu238[i][j] * (
                        10 ** -24) * timeperiteration
            u238disappear += outputfluxdistribution4[i][j] * u238a[4] * numberdensityu238[i][j] * (
                        10 ** -24) * timeperiteration
            u238disappear += outputfluxdistribution5[i][j] * u238a[3] * numberdensityu238[i][j] * (
                        10 ** -24) * timeperiteration
            u238disappear += outputfluxdistribution6[i][j] * u238a[2] * numberdensityu238[i][j] * (
                        10 ** -24) * timeperiteration
            u238disappear += outputfluxdistribution7[i][j] * u238a[1] * numberdensityu238[i][j] * (
                        10 ** -24) * timeperiteration
            u238disappear += outputfluxdistribution8[i][j] * u238a[0] * numberdensityu238[i][j] * (
                        10 ** -24) * timeperiteration

            pu239appear += outputfluxdistribution1[i][j] * (u238a[7] - u238f[7]) * (10 ** -24) * numberdensityu238[i][
                j] * timeperiteration
            pu239appear += outputfluxdistribution2[i][j] * (u238a[6] - u238f[6]) * (10 ** -24) * numberdensityu238[i][
                j] * timeperiteration
            pu239appear += outputfluxdistribution3[i][j] * (u238a[5] - u238f[5]) * (10 ** -24) * numberdensityu238[i][
                j] * timeperiteration
            pu239appear += outputfluxdistribution4[i][j] * (u238a[4] - u238f[4]) * (10 ** -24) * numberdensityu238[i][
                j] * timeperiteration
            pu239appear += outputfluxdistribution5[i][j] * (u238a[3] - u238f[3]) * (10 ** -24) * numberdensityu238[i][
                j] * timeperiteration
            pu239appear += outputfluxdistribution6[i][j] * (u238a[2] - u238f[2]) * (10 ** -24) * numberdensityu238[i][
                j] * timeperiteration
            pu239appear += outputfluxdistribution7[i][j] * (u238a[1] - u238f[1]) * (10 ** -24) * numberdensityu238[i][
                j] * timeperiteration
            pu239appear += outputfluxdistribution8[i][j] * (u238a[0] - u238f[0]) * (10 ** -24) * numberdensityu238[i][
                j] * timeperiteration

            pu239appear -= outputfluxdistribution1[i][j] * pu239c[7] * (10 ** -24) * numberdensitypu239[i][
                j] * timeperiteration
            pu239appear -= outputfluxdistribution2[i][j] * pu239c[6] * (10 ** -24) * numberdensitypu239[i][
                j] * timeperiteration
            pu239appear -= outputfluxdistribution3[i][j] * pu239c[5] * (10 ** -24) * numberdensitypu239[i][
                j] * timeperiteration
            pu239appear -= outputfluxdistribution4[i][j] * pu239c[4] * (10 ** -24) * numberdensitypu239[i][
                j] * timeperiteration
            pu239appear -= outputfluxdistribution5[i][j] * pu239c[3] * (10 ** -24) * numberdensitypu239[i][
                j] * timeperiteration
            pu239appear -= outputfluxdistribution6[i][j] * pu239c[2] * (10 ** -24) * numberdensitypu239[i][
                j] * timeperiteration
            pu239appear -= outputfluxdistribution7[i][j] * pu239c[1] * (10 ** -24) * numberdensitypu239[i][
                j] * timeperiteration
            pu239appear -= outputfluxdistribution8[i][j] * pu239c[0] * (10 ** -24) * numberdensitypu239[i][
                j] * timeperiteration

            g154disappear += outputfluxdistribution1[i][j] * g154c[7] * (10 ** -24) * numberdensityg154[i][
                j] * timeperiteration
            g154disappear += outputfluxdistribution2[i][j] * g154c[6] * (10 ** -24) * numberdensityg154[i][
                j] * timeperiteration
            g154disappear += outputfluxdistribution3[i][j] * g154c[5] * (10 ** -24) * numberdensityg154[i][
                j] * timeperiteration
            g154disappear += outputfluxdistribution4[i][j] * g154c[4] * (10 ** -24) * numberdensityg154[i][
                j] * timeperiteration
            g154disappear += outputfluxdistribution5[i][j] * g154c[3] * (10 ** -24) * numberdensityg154[i][
                j] * timeperiteration
            g154disappear += outputfluxdistribution6[i][j] * g154c[2] * (10 ** -24) * numberdensityg154[i][
                j] * timeperiteration
            g154disappear += outputfluxdistribution7[i][j] * g154c[1] * (10 ** -24) * numberdensityg154[i][
                j] * timeperiteration
            g154disappear += outputfluxdistribution8[i][j] * g154c[0] * (10 ** -24) * numberdensityg154[i][
                j] * timeperiteration

            g155disappear -= outputfluxdistribution1[i][j] * g154c[7] * (10 ** -24) * numberdensityg154[i][
                j] * timeperiteration
            g155disappear -= outputfluxdistribution2[i][j] * g154c[6] * (10 ** -24) * numberdensityg154[i][
                j] * timeperiteration
            g155disappear -= outputfluxdistribution3[i][j] * g154c[5] * (10 ** -24) * numberdensityg154[i][
                j] * timeperiteration
            g155disappear -= outputfluxdistribution4[i][j] * g154c[4] * (10 ** -24) * numberdensityg154[i][
                j] * timeperiteration
            g155disappear -= outputfluxdistribution5[i][j] * g154c[3] * (10 ** -24) * numberdensityg154[i][
                j] * timeperiteration
            g155disappear -= outputfluxdistribution6[i][j] * g154c[2] * (10 ** -24) * numberdensityg154[i][
                j] * timeperiteration
            g155disappear -= outputfluxdistribution7[i][j] * g154c[1] * (10 ** -24) * numberdensityg154[i][
                j] * timeperiteration
            g155disappear -= outputfluxdistribution8[i][j] * g154c[0] * (10 ** -24) * numberdensityg154[i][
                j] * timeperiteration

            g155disappear += outputfluxdistribution1[i][j] * g155c[7] * (10 ** -24) * numberdensityg155[i][
                j] * timeperiteration
            g155disappear += outputfluxdistribution2[i][j] * g155c[6] * (10 ** -24) * numberdensityg155[i][
                j] * timeperiteration
            g155disappear += outputfluxdistribution3[i][j] * g155c[5] * (10 ** -24) * numberdensityg155[i][
                j] * timeperiteration
            g155disappear += outputfluxdistribution4[i][j] * g155c[4] * (10 ** -24) * numberdensityg155[i][
                j] * timeperiteration
            g155disappear += outputfluxdistribution5[i][j] * g155c[3] * (10 ** -24) * numberdensityg155[i][
                j] * timeperiteration
            g155disappear += outputfluxdistribution6[i][j] * g155c[2] * (10 ** -24) * numberdensityg155[i][
                j] * timeperiteration
            g155disappear += outputfluxdistribution7[i][j] * g155c[1] * (10 ** -24) * numberdensityg155[i][
                j] * timeperiteration
            g155disappear += outputfluxdistribution8[i][j] * g155c[0] * (10 ** -24) * numberdensityg155[i][
                j] * timeperiteration

            g156disappear -= outputfluxdistribution1[i][j] * g155c[7] * (10 ** -24) * numberdensityg155[i][
                j] * timeperiteration
            g156disappear -= outputfluxdistribution2[i][j] * g155c[6] * (10 ** -24) * numberdensityg155[i][
                j] * timeperiteration
            g156disappear -= outputfluxdistribution3[i][j] * g155c[5] * (10 ** -24) * numberdensityg155[i][
                j] * timeperiteration
            g156disappear -= outputfluxdistribution4[i][j] * g155c[4] * (10 ** -24) * numberdensityg155[i][
                j] * timeperiteration
            g156disappear -= outputfluxdistribution5[i][j] * g155c[3] * (10 ** -24) * numberdensityg155[i][
                j] * timeperiteration
            g156disappear -= outputfluxdistribution6[i][j] * g155c[2] * (10 ** -24) * numberdensityg155[i][
                j] * timeperiteration
            g156disappear -= outputfluxdistribution7[i][j] * g155c[1] * (10 ** -24) * numberdensityg155[i][
                j] * timeperiteration
            g156disappear -= outputfluxdistribution8[i][j] * g155c[0] * (10 ** -24) * numberdensityg155[i][
                j] * timeperiteration

            g156disappear += outputfluxdistribution1[i][j] * g156c[7] * (10 ** -24) * numberdensityg156[i][
                j] * timeperiteration
            g156disappear += outputfluxdistribution2[i][j] * g156c[6] * (10 ** -24) * numberdensityg156[i][
                j] * timeperiteration
            g156disappear += outputfluxdistribution3[i][j] * g156c[5] * (10 ** -24) * numberdensityg156[i][
                j] * timeperiteration
            g156disappear += outputfluxdistribution4[i][j] * g156c[4] * (10 ** -24) * numberdensityg156[i][
                j] * timeperiteration
            g156disappear += outputfluxdistribution5[i][j] * g156c[3] * (10 ** -24) * numberdensityg156[i][
                j] * timeperiteration
            g156disappear += outputfluxdistribution6[i][j] * g156c[2] * (10 ** -24) * numberdensityg156[i][
                j] * timeperiteration
            g156disappear += outputfluxdistribution7[i][j] * g156c[1] * (10 ** -24) * numberdensityg156[i][
                j] * timeperiteration
            g156disappear += outputfluxdistribution8[i][j] * g156c[0] * (10 ** -24) * numberdensityg156[i][
                j] * timeperiteration

            g157disappear -= outputfluxdistribution1[i][j] * g156c[7] * (10 ** -24) * numberdensityg156[i][
                j] * timeperiteration
            g157disappear -= outputfluxdistribution2[i][j] * g156c[6] * (10 ** -24) * numberdensityg156[i][
                j] * timeperiteration
            g157disappear -= outputfluxdistribution3[i][j] * g156c[5] * (10 ** -24) * numberdensityg156[i][
                j] * timeperiteration
            g157disappear -= outputfluxdistribution4[i][j] * g156c[4] * (10 ** -24) * numberdensityg156[i][
                j] * timeperiteration
            g157disappear -= outputfluxdistribution5[i][j] * g156c[3] * (10 ** -24) * numberdensityg156[i][
                j] * timeperiteration
            g157disappear -= outputfluxdistribution6[i][j] * g156c[2] * (10 ** -24) * numberdensityg156[i][
                j] * timeperiteration
            g157disappear -= outputfluxdistribution7[i][j] * g156c[1] * (10 ** -24) * numberdensityg156[i][
                j] * timeperiteration
            g157disappear -= outputfluxdistribution8[i][j] * g156c[0] * (10 ** -24) * numberdensityg156[i][
                j] * timeperiteration

            g157disappear += outputfluxdistribution1[i][j] * g157c[7] * (10 ** -24) * numberdensityg157[i][
                j] * timeperiteration
            g157disappear += outputfluxdistribution2[i][j] * g157c[6] * (10 ** -24) * numberdensityg157[i][
                j] * timeperiteration
            g157disappear += outputfluxdistribution3[i][j] * g157c[5] * (10 ** -24) * numberdensityg157[i][
                j] * timeperiteration
            g157disappear += outputfluxdistribution4[i][j] * g157c[4] * (10 ** -24) * numberdensityg157[i][
                j] * timeperiteration
            g157disappear += outputfluxdistribution5[i][j] * g157c[3] * (10 ** -24) * numberdensityg157[i][
                j] * timeperiteration
            g157disappear += outputfluxdistribution6[i][j] * g157c[2] * (10 ** -24) * numberdensityg157[i][
                j] * timeperiteration
            g157disappear += outputfluxdistribution7[i][j] * g157c[1] * (10 ** -24) * numberdensityg157[i][
                j] * timeperiteration
            g157disappear += outputfluxdistribution8[i][j] * g157c[0] * (10 ** -24) * numberdensityg157[i][
                j] * timeperiteration

            g158disappear -= outputfluxdistribution1[i][j] * g157c[7] * (10 ** -24) * numberdensityg157[i][
                j] * timeperiteration
            g158disappear -= outputfluxdistribution2[i][j] * g157c[6] * (10 ** -24) * numberdensityg157[i][
                j] * timeperiteration
            g158disappear -= outputfluxdistribution3[i][j] * g157c[5] * (10 ** -24) * numberdensityg157[i][
                j] * timeperiteration
            g158disappear -= outputfluxdistribution4[i][j] * g157c[4] * (10 ** -24) * numberdensityg157[i][
                j] * timeperiteration
            g158disappear -= outputfluxdistribution5[i][j] * g157c[3] * (10 ** -24) * numberdensityg157[i][
                j] * timeperiteration
            g158disappear -= outputfluxdistribution6[i][j] * g157c[2] * (10 ** -24) * numberdensityg157[i][
                j] * timeperiteration
            g158disappear -= outputfluxdistribution7[i][j] * g157c[1] * (10 ** -24) * numberdensityg157[i][
                j] * timeperiteration
            g158disappear -= outputfluxdistribution8[i][j] * g157c[0] * (10 ** -24) * numberdensityg157[i][
                j] * timeperiteration

            g158disappear += outputfluxdistribution1[i][j] * g158c[7] * (10 ** -24) * numberdensityg158[i][
                j] * timeperiteration
            g158disappear += outputfluxdistribution2[i][j] * g158c[6] * (10 ** -24) * numberdensityg158[i][
                j] * timeperiteration
            g158disappear += outputfluxdistribution3[i][j] * g158c[5] * (10 ** -24) * numberdensityg158[i][
                j] * timeperiteration
            g158disappear += outputfluxdistribution4[i][j] * g158c[4] * (10 ** -24) * numberdensityg158[i][
                j] * timeperiteration
            g158disappear += outputfluxdistribution5[i][j] * g158c[3] * (10 ** -24) * numberdensityg158[i][
                j] * timeperiteration
            g158disappear += outputfluxdistribution6[i][j] * g158c[2] * (10 ** -24) * numberdensityg158[i][
                j] * timeperiteration
            g158disappear += outputfluxdistribution7[i][j] * g158c[1] * (10 ** -24) * numberdensityg158[i][
                j] * timeperiteration
            g158disappear += outputfluxdistribution8[i][j] * g158c[0] * (10 ** -24) * numberdensityg158[i][
                j] * timeperiteration

            g160disappear += outputfluxdistribution1[i][j] * g160c[7] * (10 ** -24) * numberdensityg160[i][
                j] * timeperiteration
            g160disappear += outputfluxdistribution2[i][j] * g160c[6] * (10 ** -24) * numberdensityg160[i][
                j] * timeperiteration
            g160disappear += outputfluxdistribution3[i][j] * g160c[5] * (10 ** -24) * numberdensityg160[i][
                j] * timeperiteration
            g160disappear += outputfluxdistribution4[i][j] * g160c[4] * (10 ** -24) * numberdensityg160[i][
                j] * timeperiteration
            g160disappear += outputfluxdistribution5[i][j] * g160c[3] * (10 ** -24) * numberdensityg160[i][
                j] * timeperiteration
            g160disappear += outputfluxdistribution6[i][j] * g160c[2] * (10 ** -24) * numberdensityg160[i][
                j] * timeperiteration
            g160disappear += outputfluxdistribution7[i][j] * g160c[1] * (10 ** -24) * numberdensityg160[i][
                j] * timeperiteration
            g160disappear += outputfluxdistribution8[i][j] * g160c[0] * (10 ** -24) * numberdensityg160[i][
                j] * timeperiteration

            numberdensityu235[i][j] -= u235disappear
            numberdensityu238[i][j] -= u238disappear
            numberdensitypu239[i][j] += pu239appear
            numberdensityg154[i][j] -= g154disappear
            numberdensityg155[i][j] -= g155disappear
            numberdensityg156[i][j] -= g156disappear
            numberdensityg157[i][j] -= g157disappear
            numberdensityg158[i][j] -= g158disappear
            numberdensityg160[i][j] -= g160disappear
            if (numberdensitypu239[i][j] < 0):
                numberdensitypu239[i][j] = 0
            if (numberdensityu235[i][j] < 0):
                numberdensityu235[i][j] = 0
            if (numberdensityu238[i][j] < 0):
                numberdensityu238[i][j] = 0
            if (numberdensityg154[i][j] < 0):
                numberdensityg154[i][j] = 0
            if (numberdensityg155[i][j] < 0):
                numberdensityg155[i][j] = 0
            if (numberdensityg156[i][j] < 0):
                numberdensityg156[i][j] = 0
            if (numberdensityg157[i][j] < 0):
                numberdensityg157[i][j] = 0
            if (numberdensityg158[i][j] < 0):
                numberdensityg158[i][j] = 0
            if (numberdensityg160[i][j] < 0):
                numberdensityg160[i][j] = 0

plt.plot(timearray, kaxialarray, label="axial")
plt.plot(timearray, kradialarray, label="radial")
plt.legend()
plt.show()


def printerfunction(twodarray, group):
    fig, ax = plt.subplots(figsize=(6, 6))
    im = ax.imshow(twodarray, cmap='hot', extent=[0, diameterreflector / 2, heightreflector / 2, 0])
    cbar = ax.figure.colorbar(im, ax=ax, shrink=0.8)

    ax.set_title("Group " + str(group) + " Flux Distribution", size=10)
    plt.xlabel("Radius (cm)")
    plt.ylabel("Height (cm)")
    fig.tight_layout()
    plt.show()


printerfunction(outputfluxdistribution1, 1)
printerfunction(outputfluxdistribution2, 2)
printerfunction(outputfluxdistribution3, 3)
printerfunction(outputfluxdistribution4, 4)
printerfunction(outputfluxdistribution5, 5)
printerfunction(outputfluxdistribution6, 6)
printerfunction(outputfluxdistribution7, 7)
printerfunction(outputfluxdistribution8, 8)
