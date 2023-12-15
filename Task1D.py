from floodsystem.geo import *
from floodsystem.stationdata import build_station_list

def compact_repr(stat):
    return stat[0].name

def run():
    """Requirements for Task 1D"""

    stations = build_station_list()
    rivers = rivers_with_station(stations)
    print(f"{len(rivers)} rivers have stations, first 10: {sorted(list(rivers))[:10]}")

    dct = stations_by_river(stations)
    print(f"River Aire has the following stations: {sorted(stat.name for stat in dct['River Aire'])}")
    print(f"River Cam has the following stations: {sorted(stat.name for stat in dct['River Cam'])}")
    print(f"River Thames has the following stations: {sorted(stat.name for stat in dct['River Thames'])}")


if __name__ == '__main__':
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
