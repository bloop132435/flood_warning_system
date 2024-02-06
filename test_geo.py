# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the geo module, tests for tasks 1B-E"""

from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river, rivers_by_station_number
from floodsystem.stationdata import build_station_list
import random

# Build list of stations
stations = build_station_list()

# List of random uk coordinates
random_uk_coords =  [(random.uniform(50, 58),random.uniform(-10, 2)) for i in range(100)]


def test_stations_by_distance():
    
    for p in random_uk_coords:
        sorted_stations = stations_by_distance(stations, p)
        for i in range(len(sorted_stations)):
            
            # check that list is ordered
            if i > 0:
                assert sorted_stations[i][1] >= sorted_stations[i-1][1]
    

def test_stations_within_radius():

    for x in random_uk_coords:
        r = random.uniform(1, 300) # choose a random radius between 1 and 300km
        filtered_stations = stations_within_radius(stations, x, r)

        # check that retuned stations are within radius
        for station in filtered_stations:
            assert station[1] <= r


def test_rivers_with_station():

    for dummy in range(100):
        # Create a random set of stations
        station_group = []
        while len(station_group) < random.randint(1, len(stations)):
            random_station = random.choice(stations)
            if random_station not in station_group:
                station_group.append(random_station)
        
        river_group = rivers_with_station(station_group)

        all_rivers_included = True
        
        for river in river_group:
            river_included = False
            for station in station_group:
                
                # check for rivers not monitored by station group
                if river == station.river:
                    river_included = True
                
                # check for stations not monitoring river from river_group
                if station.river not in river_group:
                    all_rivers_included = False

            assert river_included
        
        assert all_rivers_included
     

def test_stations_by_river():
    
    river_dictionary = stations_by_river(stations)

    for key in river_dictionary:
        river_totally_monitored = True

        # check for stations not monitoring river
        for station in river_dictionary[key]:
            if station.river != key:
                river_totally_monitored = False
        
        assert river_totally_monitored


def test_rivers_by_station_number():

    for dummy in range(100):

        # create a random set of stations
        station_group = []
        while len(station_group) < random.randint(1, len(stations)):
            random_station = random.choice(stations)
            if random_station not in station_group:
                station_group.append(random_station)
        
        # choose a random number up to number of rivers being monitored by station_group
        N = random.randint(1, len(stations_by_river(station_group)))
        rivers = rivers_by_station_number(station_group, N)     

        same_counter = 0
        for i in range(len(rivers)):
            # check that rivers have been sorted from most to least stations
            if i > 0:
                assert rivers[i][1] <= rivers[i-1][1]
                    
                if rivers[i][1] == rivers[i-1][1]:
                    same_counter += 1
        
        # check that function returned the N+s most stations
        assert len(rivers) - same_counter <= N