from typing import List
from .station import MonitoringStation

def stations_level_over_threshold(stations:List[MonitoringStation], tol: float)->List[MonitoringStation]:
    """(2B) create a tuple list of stations with relative water levels above tol"""
    pruned_stations = [s for s in stations if s.relative_water_level() != None]
    sorted_stations = sorted(pruned_stations,key=lambda x: -1 * (x.relative_water_level() or 0))
    for i in range(len(sorted_stations)):
        if (sorted_stations[i].relative_water_level() or 0) < tol:
            return sorted_stations[:i]
    return sorted_stations

def stations_highest_rel_level(stations:List[MonitoringStation], N:int)->List[MonitoringStation]:
    pruned_stations = [s for s in stations if s.relative_water_level() != None]
    sorted_stations = sorted(pruned_stations,key=lambda x: -1 * (x.relative_water_level() or 0))
    return sorted_stations[:N]
