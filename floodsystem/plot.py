# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module di"""
import matplotlib.pyplot as plt
from floodsystem.station import MonitoringStation
from datetime import datetime
from typing import List

def plot_water_levels(station:MonitoringStation, dates:List[datetime], levels:List[float]):
    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(MonitoringStation.town)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    
    plt.show()
