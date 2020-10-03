from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import numpy as np

#rootgrp = Dataset("gpw_v4_population_density_rev11_2pt5_min.nc", "r", format="NETCDF4")
f = Dataset("gpw_v4_basic_demographic_characteristics_rev11_bt_2010_cntm_2pt5_min.nc", "r", format="NETCDF4_CLASSIC")

#f = Dataset("gpw_v4_basic_demographic_characteristics_rev11_bt_2010_cntm_1_deg.nc", "r", format="NETCDF4_CLASSIC")

#Demographic = f.variables["Basic Demographic Characteristics, v4.10 (2010): Both, Count, 1 degree"][:]
print(f.variables.keys())
Demographic = f.variables["Basic Demographic Characteristics, v4.10 (2010): Both, Count, 2.5 arc-minutes"][:]
Longitude = f.variables["longitude"][:] #90
Latitude = f.variables["latitude"][:] #180
print(Longitude)
print(Latitude)

print(type(Demographic))

m = Basemap()
m.drawcoastlines()

a = Demographic[3]
i = 0
for lon in a:
    j=0
    for lat in lon:
        if (lat > 10):
            m.plot(Longitude[j],Latitude[i], marker = 'o', c='r', markersize=lat/500000, alpha=0.8, latlon=False)
        j+=1
    i+=1

plt.show()

quit()


print(rootgrp.variables.keys())


for x in range(30):

    population = np.array(rootgrp.variables['Basic Demographic Characteristics, v4.10 (2010): Both, Count, 2.5 arc-minutes'], dtype=type(rootgrp.variables))

    lat = np.array(rootgrp.variables['latitude'], dtype=type(rootgrp.variables))
    lon = np.array(rootgrp.variables['longitude'], dtype=type(rootgrp.variables))

    print(lat)
    print(lon)
    print('population: ', population[0][0])

    save = population[0][0]/10000

    i = 0
    y = 0
    for la in lat[::100]:
        for lo in lon[::100]:
            if (population[y][i] != "--"):
                m.plot(lo,la, marker = 'o', c='r', markersize=population[y][i]/10000, alpha=0.8, latlon=False)
                print('youpi',x, population[y][i])
            y+=1
        i+=1
        y=0


#plt.show()