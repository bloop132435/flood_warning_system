from floodsystem.geo import *
from floodsystem.stationdata import *
from floodsystem.station import *

def compact_repr(stat):
    return stat.name

def run():
    """Requirements for Task 1F"""

    stations = build_station_list()
    sorted_stations = inconsistent_typical_range_stations(stations)
    print(f"Inconsistent Stations: {sorted([compact_repr(s) for s in sorted_stations])}")


if __name__ == '__main__':
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
