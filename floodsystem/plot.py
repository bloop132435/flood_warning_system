# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains functions related to the plotting of water levels over time
"""

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from .station import MonitoringStation
from .analysis import polyfit

def plot_water_levels(station:MonitoringStation, dates:list, levels:list, show:bool = True):
    plt.plot(dates,levels,".")

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title(f"{station.name} water level data")
    plt.axhline(y=station.typical_range[0], color='r', linestyle='-')
    plt.axhline(y=station.typical_range[1], color='r', linestyle='-')
    plt.tight_layout(rect=[0, 0.09, 1, 0.95])
    plt.xticks(rotation=45)
    if show:
        plt.show()

def plot_water_level_with_fit(station:MonitoringStation, dates:list, levels:list, p:int):

    x = matplotlib.dates.date2num(dates)
    best_fit = polyfit(dates, levels, p)
    poly = best_fit[0]

    x1 = np.linspace(x[0], x[-1], 100)

    plot_water_levels(station, dates, levels,show=False)
    plt.plot(x1, poly(x1 - best_fit[1]))
    plt.show()
