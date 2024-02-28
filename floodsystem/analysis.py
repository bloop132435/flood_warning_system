# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import numpy as np
import matplotlib
import datetime
from .station import MonitoringStation
from .datafetcher import fetch_measure_levels

def polyfit(dates:list, levels:list, p:int)->tuple:
    """(2F) find order p polynomial of best fit of given water levels and dates"""
    x = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(x - x[0], np.array(levels), p)
    poly = np.poly1d(p_coeff)

    return (poly, x[0])

def flood_metric(stat: MonitoringStation,
                         look_back: datetime.timedelta = datetime.timedelta(days=3),
                         look_ahead: datetime.timedelta = datetime.timedelta(days=1),
                         poly_order: int = 3) -> float:
    rwl = stat.relative_water_level()
    rwl = rwl if rwl is not None else -1
    # if rwl < 0:
    #     rwl = -2
    # return rwl


    if not stat.typical_range_consistent():
        print(stat.name + ' irregular range')
        return -1
    if rwl <= 1:
        print(stat.name + ' within range')
        return max(rwl,0)
    try:
        dates, levels = fetch_measure_levels(stat.measure_id, dt=look_back)
    except:
        print(stat.name + ' error with website')
        return -1
    if len(dates)==0:
        return -1
    best_fit = polyfit(dates, levels, poly_order)
    poly = best_fit[0]
    value_at_la = poly(look_back.days + look_ahead.days)
    print(stat.name)
    wl = stat.relative_water_level(value_at_la)
    wl = wl if wl is not None else -1
    return max(wl,0)

def flood_category(stat: MonitoringStation,
                         look_back: datetime.timedelta = datetime.timedelta(days=3),
                         look_ahead: datetime.timedelta = datetime.timedelta(days=1),
                         poly_order: int = 3) -> str:
    x = flood_metric(stat,look_back,look_ahead,poly_order)
    if x <= 1:
        return 'Low'
    if x <= 2:
        return 'Moderate'
    if x <= 3:
        return 'High'
    return 'Severe'
