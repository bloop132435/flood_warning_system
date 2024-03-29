from floodsystem.geo import *
from floodsystem.stationdata import *
from floodsystem.station import *
from floodsystem.flood import stations_level_over_threshold

def compact_repr(stat:MonitoringStation)->str:
    return stat.name + ", " + str(stat.relative_water_level()) + "\n"

def run():
    """Requirements for Task 2B"""

    # Build list of stations
    stations = build_station_list()
    
    # Fetch river levels for each station
    update_water_levels(stations)

    # Print stations with a relative level above 0.8
    print("".join([compact_repr(s) for s in stations_level_over_threshold(stations,0.8)]))


if __name__ == '__main__':
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
