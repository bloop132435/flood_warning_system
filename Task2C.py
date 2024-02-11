from floodsystem.geo import *
from floodsystem.stationdata import *
from floodsystem.station import *
from floodsystem.flood import stations_highest_rel_level

def compact_repr(stat:MonitoringStation)->str:
    return stat.name + ", " + str(stat.relative_water_level()) + "\n"

def run():
    """Requirements for Task 2C"""

    # Build list of stations
    stations = build_station_list()
    
    # Fetch river levels for each station
    update_water_levels(stations)

    # Print 10 rivers with highest relative water levels
    print("".join([compact_repr(s) for s in stations_highest_rel_level(stations,10)]))


if __name__ == '__main__':
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
