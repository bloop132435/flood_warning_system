# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the geo module, tests for tasks 1B-E"""

from floodsystem.geo import haversine, haversine_distance, stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river, rivers_by_station_number
from floodsystem.stationdata import build_station_list
import random

def test_stations_by_distance():
    
    # Build list of stations
    stations = build_station_list()
    
    random_uk_coords =  [(random.uniform(50, 58),random.uniform(-10, 2,)) for i in range(1000)]

    for p in random_uk_coords:
        sorted_stations = stations_by_distance(stations, p)
        for i in range(len(sorted_stations)):
            if i > 0:
                assert sorted_stations[i][1] >= sorted_stations[i-1][1]
    

# def test_stations_within_radius:

# def test_rivers_with_station:

# def test_stations_by_river:

# def test_rivers_by_station_number:
