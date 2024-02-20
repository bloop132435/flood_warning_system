# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels

def run():

    # Build list of stations
    stations = build_station_list()

    # Identify 5 stations with highest water levels
    high_stations = stations_highest_rel_level(stations, 5)

    # Create plots of water levels of high_stations for past 10 days
    for station in high_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=10))
        plot_water_levels(high_stations, dates, levels)
        plt.show()       


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
