from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def compact_repr(stat):
    return stat[0].name

def run():
    """Requirements for Task 1C"""

    stations = build_station_list()
    sorted_stations = stations_within_radius(stations,(52.2053, 0.1218),10)
    print(f"Stations within 10km of Cambridge City Center: {sorted([compact_repr(s) for s in sorted_stations])}")


if __name__ == '__main__':
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
