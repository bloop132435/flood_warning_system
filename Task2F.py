# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit


def run():

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    high_stations = stations_highest_rel_level(stations,5)

    dt = 2
    tt = datetime.timedelta(days=dt)
    for s in high_stations:
        dates, levels = fetch_measure_levels(s.measure_id, dt=tt)
        plot_water_level_with_fit(s,dates,levels,4)
            



if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
