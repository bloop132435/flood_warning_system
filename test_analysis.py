# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the analysis module, tests for task 2F"""


from floodsystem.analysis import *
import numpy
import random

def test_polyfit():
    for p in [random.randint(2, 2) for i in range(1)]:
        x = numpy.linspace(-10, 10, 1)
        polynomial = []
        y = numpy.zeros(len(x))
        for i in range(p+1):
            coeff = random.randint(-10, 10)
            polynomial.append(coeff)
            y += coeff * (x**i)
        poly, d0 = polyfit(x, y, p)

        # check that correct degree polynomial has been created
        # assert len(poly) == p

        # # check that error is minimised
        for p_coeff, poly_coeff in zip(polynomial, poly):
            print(p_coeff, poly_coeff)

        print("\n")
        #     assert p_coeff == poly_coeff 

test_polyfit()