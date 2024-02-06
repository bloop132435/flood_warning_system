# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

import math
from .utils import sorted_by_key  # noqa
from typing import Tuple,List,Set,Dict
from .station import MonitoringStation


def haversine(x:float)->float:
    return math.sin(x/2)**2

def haversine_distance(x_deg:Tuple[float,float],y_deg:Tuple[float,float])->float:
    """Calculates the distance between x (tuple of lat and long) and y (tuple of lat and long) in km"""
    x = (x_deg[0] / (180) * math.pi, x_deg[1] / (180) * math.pi)
    y = (y_deg[0] / (180) * math.pi, y_deg[1] / (180) * math.pi)
    EARTH_RADIUS = 6378.14
    a = haversine(y[0]-x[0])
    b = math.cos(x[0]) * math.cos(y[0]) * haversine(y[1]-x[1])
    inv = math.asin(math.sqrt(a + b))
    return 2 * EARTH_RADIUS * inv

def stations_by_distance(stations:List[MonitoringStation],p:Tuple[float,float])->List[Tuple[MonitoringStation,float]]:
    """(1B) Sorts a list of monitoring stations by their distance from a geographic coordinate p"""
    stat_dist = [(s,haversine_distance(s.coord,p)) for s in stations]
    sorted_arr = sorted_by_key(stat_dist,1)
    return sorted_arr

def stations_within_radius(stations:List[MonitoringStation], center:Tuple[float,float], r:float)->List[Tuple[MonitoringStation,float]]:
    """(1C) Filters and alphabetically sorts a list of monitoring stations to within a radius r of a geographic coordinate x"""
    sorted_arr = stations_by_distance(stations,center)
    for i in range(len(sorted_arr)):
        if sorted_arr[i][1] > r:
            return sorted_arr[:i]
    return sorted_arr

def rivers_with_station(stations:List[MonitoringStation])->Set[str]:
    """(1D) Creates a set of rivers monitored by given monitoring stations, without duplicate entries"""
    return set([stat.river for stat in stations])

def stations_by_river(stations:List[MonitoringStation])->Dict[str,List[MonitoringStation]]:
    """(1D) Maps each given river to a list of the monitoring stations monitoring it"""
    d = dict()
    for river in rivers_with_station(stations):
        d[river] = list()
    for stat in stations:
        d[stat.river].append(stat)
    return d

def rivers_by_station_number(stations:List[MonitoringStation], N:int)-> List[Tuple[str,int]]:
    """(1E) Creates a list of at most N+s rivers with the most monitoring stations, where s is the number of rivers with the same amount of monitoring stations as the Nth entry"""
    dct = stations_by_river(stations)
    arr = [(river,len(x)) for river,x in dct.items()]
    arr = sorted_by_key(arr,1,reverse=True)
    num = arr[N-1][1]
    for i in range(len(arr)):
        if arr[i][1] < num:
            return arr[:i]
    return arr
