# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the analysis module, tests for task 2F"""


from floodsystem.analysis import *
import numpy
import matplotlib.dates

def test_polyfit():
    # test up to quintic
    for p in range(5):
        x = numpy.linspace(0,20,2000)
        y = numpy.array([a**(p+1) for a in x])

        poly, d0 = polyfit(matplotlib.dates.num2date(x), y, 10)
        y_test = poly(x)
        assert (numpy.round(y,3) == numpy.round(y_test,3)).all()