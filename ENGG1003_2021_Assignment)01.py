"""
    Tasks:
     - Import csv file
     - Plot lat vs long
     -
    """

# Imports
import statistics
import math
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime as dt

# Variables
filepath = "C://Users//Jay//Downloads//track.csv"

# Function storage


def setup(filepath):
    """Imports CSV file at specified path and returns columns

    Args:
        filepath (string): Path to csv file
    Rtns:
        time (list): Time data as an arra
        lat (list): Latitude data as an array
        lon (list): Longnitude data as an array
        ele (list): Elevation data as an array
    """
    data = pd.read_csv(filepath)
    time = data["time"]
    lat = data["lat"]
    lon = data["lon"]
    ele = data["ele"]
    return(time, lat, lon, ele)


def plot_lat_lon(lat, lon, debug):
    """Plots Lat vs Lon using matplotlib

    Args:
        lat (list): Lat data as an array
        lon (list): Lon data as an array
    """
    if(debug):
        plt.plot(lat, lon)
        plt.title("Lat vs Lon")
        plt.xlabel("Lat values")
        plt.ylabel("Long values")
        plt.show()


def calculate_time_deta(time, debug):
    """Calculate time deltas and plot results (Task something)

    Args:
        time (list): List of times for each GPS point
        debug (bool): Boolean val for whether to output or not
    Rtns:
        tv (list): Array of time deltas, if needed later
    """
    tv = []
    time
    for i in range(len(time) - 1):
        val = time[i]
        val2 = time[i + 1]
        n_val = dt.strptime(val, "%Y-%m-%d %H:%M:%S+00:00")
        n_val2 = dt.strptime(val2, "%Y-%m-%d %H:%M:%S+00:00")
        td = (n_val2 - n_val).seconds
        if(debug):
            if(td > 1):
                print("ERROR!")
        tv.append(td)
    return(tv)


def haversine(lat_val, next_lat_val, lon_val, next_lon_val):
    delta_lat = next_lat_val - lat_val
    delta_lon = next_lon_val - lon_val
    a = math.sin(delta_lat / 2)**2 + math.cos(lat_val) * \
        math.cos(next_lat_val)*math.sin(delta_lon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = 6371 * 1000 * c
    return(d)


def calculate_delta_distance(lat_data, lon_data, debug):
    """Calculate the delta distance between GPS points using the haversine method

    Args:
        lat_data (list): List of latitude data
        lon_data (list): List of longnitude data
        debug (bool): Boolean variable for whether to output or not
    """
    dd = []
    for i in range(len(time) - 1):
        lat_val = lat[i]
        next_lat_val = lat[i + 1]
        lon_val = lon[i]
        next_lon_val = lon[i + 1]
        dd.append(haversine(lat_val, next_lat_val, lon_val, next_lon_val))
    return(dd)


def calculate_speed(delta_time, delta_distance, debug):
    """Calculate speed by dividing delta distance / delta time

    Args:
        delta_time (list): Array of delta time values
        delta_distance (list): Array of delta distance values
        debug (bool): Whether output if required or not
    """
    speed_values = []
    for i in range(len(delta_time) - 1):
        speed = delta_distance[i] / delta_time[i + 1]
        speed_values.append(speed)
    return(speed_values)


def calculate_delta_elevation(elevation_data, debug):
    """Calculate the change in elevation data

    Args:
        elevation_data (list): Elevation data as an array
        debug (bool): Boolean value for whether output is required or not

    Rtns:
        delta_ele (list): Delta elevation data as an array
    """
    delta_ele = []
    for i in range(len(elevation_data) - 1):
        ele_val = elevation_data[i]
        next_ele_val = elevation_data[i + 1]
        delta_elevation = next_ele_val - ele_val
        delta_ele.append(delta_elevation)
    return(delta_ele)


def calculate_power_and_plot(delta_elevation, debug):
    """Calculate power using E = mgH and return it in an array. Also plot if needed.

    Args:
        delta_elevation (list): Delta elevation as an array
        debug (bool): Boolean value for whether to print or not
    """
    power_no_downhill = []
    power_all = []
    for i in range(len(delta_elevation)):
        mass = 100
        g = 9.81
        del_ele = delta_elevation[i]
        power = mass * g * del_ele
        if(power > 0):
            power_no_downhill.append(power)
        power_all.append(power)
    return(power_no_downhill, power_all)


def calulate_average_power(power_no_downhill):
    """Calculate the average power output of the rider. Print if required.

    Args:
        power_no_downhill (list): Power output of rider with no downhill entries.
    Rtns:
        average (float): Average power output of rider to 3dp
    """
    average = statistics.mean(power_no_downhill)
    return(average)


# Required code
debug = False

time, lat, lon, ele = setup(filepath)
plot_lat_lon(lat, lon, debug)
delta_time = calculate_time_deta(time, debug)
delta_distance = calculate_delta_distance(lat, lon, debug)
speed = calculate_delta_distance(lat, lon, debug)
delta_elevation = calculate_delta_elevation(ele, debug)
power_no_downhill, power_all = calculate_power_and_plot(delta_elevation, debug)
average = calulate_average_power(power_no_downhill)

# Testing

stdev = math.sqrt(statistics.variance(power_all))

# print(stdev)

print(time[0])
print(type(time[0]))
