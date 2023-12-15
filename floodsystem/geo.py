# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

import math
from .utils import sorted_by_key  # noqa


def haversine(x):
    return math.sin(x/2)**2

def haversine_distance(x_deg,y_deg):
    """Calculates the distance between x (tuple of lat and long) and y (tuple of lat and long) in km"""
    x = (x_deg[0] / (180) * math.pi, x_deg[1] / (180) * math.pi)
    y = (y_deg[0] / (180) * math.pi, y_deg[1] / (180) * math.pi)
    EARTH_RADIUS = 6378.14
    a = haversine(y[0]-x[0])
    b = math.cos(x[0]) * math.cos(y[0]) * haversine(y[1]-x[1])
    inv = math.asin(math.sqrt(a + b))
    return 2 * EARTH_RADIUS * inv

def stations_by_distance(stations,p):
    stat_dist = [(s,haversine_distance(s.coord,p)) for s in stations]
    sorted_arr = sorted_by_key(stat_dist,1)
    return sorted_arr

def stations_within_radius(stations, center, r):
    sorted_arr = stations_by_distance(stations,center)
    for i in range(len(sorted_arr)):
        if sorted_arr[i][1] > r:
            return sorted_arr[:i]
    return sorted_arr

def rivers_with_station(stations):
    return set([stat.river for stat in stations])

def stations_by_river(stations):
    d = dict()
    for river in rivers_with_station(stations):
        d[river] = list()
    for stat in stations:
        d[stat.river].append(stat)
    return d
