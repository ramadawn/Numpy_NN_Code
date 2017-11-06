from datetime import datetime
import numpy as np
import copy

#----------Prepare Data--------------

date = []
latitude = []
longitude = []
magnitude = []
counter = 0

with open("database.csv", "r") as file:
    file.readline() # skip first

    for line in file:
        elements = line.split(',')
        try:
            date.append(datetime.strptime(f"{elements[0]} {elements[1]}","%m/%d/%Y %H:%M:%S"))
            latitude.append(float(elements[2]))
            longitude.append(float(elements[3]))
            magnitude.append(float(elements[8]))
        except ValueError:
            pass
        
date_np = np.array(date)
lat_np = np.array(latitude)
long_np = np.array(longitude)
mag_np = np.array(magnitude)

data_size = len(date)

#----------convert lat/long from degrees to radians----------------------------------------------------   
    
    
 #vectorsX, vectorsY = Dataset.vectorize(date, latitude, longitude), magnitude.reshape((data_size, 1))
rad_lat = np.deg2rad(lat_np)
rad_long = np.deg2rad(long_np)

#----------Calculating the geographic midpiont  http://www.geomidpoint.com/calculation.html--------------

x = np.cos(rad_lat) * np.cos(rad_long)
y = np.cos(rad_lat) * np.sin(rad_long)
z = np.sin(rad_lat)

min_data = min(date_np)
max_data = max(date_np)
delta = max_data - min_data

normalized_date = np.float32([(d - min_data).total_seconds() / delta.total_seconds() for d in date_np])

#combining longitude, latitude and date arrays

def concat(x, y, z):
    return x, y, z



vector_array_tuple = np.concatenate(concat(x, y, z) + normalized_date,)

print(vector_array_tuple.shape())

#vector_array_tuple.reshape((4, len(date))).swapaxes(0,1)
print(vector_array_tuple)


#double = [2 * place for place in test_list]


#np.concatenate(Dataset.normalize_cord(latitude, longitude) + (Dataset.normalize_date(date),)).reshape((4, len(date))).swapaxes(0, 1)
