from floodsystem.geo import *
from floodsystem.stationdata import build_station_list

def compact_repr(stat):
    return stat[0].name

def run():
    """Requirements for Task 1E"""

    # Build list of stations
    stations = build_station_list()
    # Print the rivers with the N+s most monitoring stations (s = number of rivers with same amount of monitoring stations as Nth river)
    print("N=9", rivers_by_station_number(stations,9))


if __name__ == '__main__':
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
