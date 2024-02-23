# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import numpy as np
import matplotlib

def polyfit(dates:list, levels:list, p:int)->tuple:
    
    x = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(x - x[0], levels, p)
    poly = np.poly1d(p_coeff)

    return (poly, x[0])