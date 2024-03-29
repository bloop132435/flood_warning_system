# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""
from typing import Optional,List


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self) -> bool:
        """(1F boolean method checking typical high/low range data for consistency of class)"""
        if self.typical_range is None:
            return False
        if self.typical_range[0] >= self.typical_range[1]:
            return False
        return True

    def relative_water_level(self,level:float=-1.0) -> Optional[float]:
        """(2B float method returning latest water level as fraction of typical range, returns none if inconsistent typical range)"""
        if not self.typical_range_consistent():
            return None
        if level == -1.0:
            if self.latest_level is None:
                return None
            return (self.latest_level - self.typical_range[0])/(self.typical_range[1] - self.typical_range[0])
        else:
            return (level - self.typical_range[0])/(self.typical_range[1] - self.typical_range[0])


def inconsistent_typical_range_stations(stations: List[MonitoringStation]) -> List[MonitoringStation]:
    """(1F) Filters a list of stations, returns list of inconsistent stations"""
    return [stat for stat in stations if not stat.typical_range_consistent()]
