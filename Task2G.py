# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import flood_metric, flood_category
import matplotlib.pyplot as plt

def run():

    # Build list of stations
    stations = build_station_list()
    stations = sorted(stations,key=lambda s:s.name)
    update_water_levels(stations)
    warnings = [flood_category(s) for s in stations]

    d = {"Low":[], "Moderate":[], "High":[], "Severe":[]}
    for w,stat in zip(warnings,stations):
        d[w].append(stat)

    print(len(d["Moderate"]), "moderate stations:", [s.name for s in d["Moderate"]])
    print(len(d["High"]), "high stations:", [s.name for s in d["High"]])
    print(len(d["Severe"]), "severe stations:", [s.name for s in d["Severe"]])
    
    plt.bar(d.keys(),[len(arr) for arr in d.values()])
    plt.show()

    # for s in d["Severe"]:
    #     dates, levels = fetch_measure_levels(s.measure_id, dt=datetime.timedelta(3))
    #     plot_water_level_with_fit(s,dates,levels,3)

    # # FOR TESTING PURPOSES:
    # m = 1
    # stat = 0
    # for met,s in zip(metrics,stations):
    #     if met < m:
    #         m = met
    #         stat = s
    # print(m)
    # print(stat)
    # plt.hist(metrics,bins=100)
    # plt.yscale('log')
    # plt.show()


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
