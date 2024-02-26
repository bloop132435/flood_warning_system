# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import numpy as np
import matplotlib
import datetime
from .station import MonitoringStation
from .datafetcher import fetch_measure_levels

def polyfit(dates:list, levels:list, p:int)->tuple:

    x = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(x - x[0], levels, p)
    poly = np.poly1d(p_coeff)

    return (poly, x[0])

def flood_metric(stat: MonitoringStation,
                         look_back: datetime.timedelta = datetime.timedelta(days=3),
                         look_ahead: datetime.timedelta = datetime.timedelta(days=1),
                         poly_order: int = 1) -> float:
    # rwl = stat.relative_water_level()
    # rwl = rwl if rwl is not None else -1
    # if rwl < 0:
    #     rwl = -2
    # return rwl


    if not stat.typical_range_consistent():
        return -1
    dates, levels = fetch_measure_levels(stat.measure_id, dt=look_back)
    if len(dates)==0:
        return -1
    best_fit = polyfit(dates, levels, poly_order)
    poly = best_fit[0]
    value_at_la = poly(look_back.days + look_ahead.days)
    print(stat.name)
    return value_at_la/stat.typical_range[1]
