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
    # metrics = [flood_metric(s) for s in stations]
    warnings = [flood_category(s) for s in stations]
    d = dict()
    for w,stat in zip(warnings,stations):
        if w in d:
            d[w]+=1
        else:
            d[w] = 1
        if w == 'Severe':
            print(stat.name)
    print(d)
    plt.bar(d.keys(),d.values())
    plt.show()
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
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
