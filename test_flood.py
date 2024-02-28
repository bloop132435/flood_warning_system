# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit tests for the flood module, tests for tasks 2B-C"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import *
import random

# Build list of stations
stations = build_station_list()
update_water_levels(stations)

def test_stations_level_over_threshold():
    # test at different tolerances
    for tol in [random.uniform(0,10) for i in range(1000)]:
        
        high_stations = stations_level_over_threshold(stations,tol)
        if len(high_stations) == 0:
            continue

        # check that list is ordered by water level
        for i in range(len(high_stations)-1):
            assert high_stations[i].relative_water_level() >= high_stations[i+1].relative_water_level()

        # check that lowest water level is list is higher than tolerance
        assert high_stations[-1].relative_water_level() >= tol

def test_stations_highest_rel_level():
    
    for dummy in range(1000):
        # create random set of stations
        station_group = []
        while len(station_group) < random.randint(1, len(stations)):
            random_station = random.choice(stations)
            if random_station not in station_group:
                station_group.append(random_station)

        N = random.randint(1, len(station_group))
        high_stations = stations_highest_rel_level(station_group, N)

        # check that list is at most N long
        assert len(high_stations) <= N
        # check that list is ordered by water level
        for i in range(len(high_stations)-1):
            assert high_stations[i].relative_water_level() >= high_stations[i+1].relative_water_level()
        
        
