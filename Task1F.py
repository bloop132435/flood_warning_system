from floodsystem.geo import *
from floodsystem.stationdata import *
from floodsystem.station import *

def compact_repr(stat):
    return stat.name

def run():
    """Requirements for Task 1F"""

    # Build list of stations
    stations = build_station_list()
    # Filter list of stations to have only stations with inconsistent data
    sorted_stations = inconsistent_typical_range_stations(stations)
    # Print alphabetically ordered filtered list
    print(f"Inconsistent Stations: {sorted([compact_repr(s) for s in sorted_stations])}")


if __name__ == '__main__':
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
