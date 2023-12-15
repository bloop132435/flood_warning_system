from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def compact_repr(stat):
    return (stat[0].name,stat[0].town,stat[1])
def run():
    """Requirements for Task 1B"""

    stations = build_station_list()
    sorted_stations = stations_by_distance(stations,(52.2053, 0.1218))

    print(f"10 closest stations to (52.2053, 0.1218): {[compact_repr(s) for s in sorted_stations[:10]]}\n")
    print(f"10 farthest/furthest??? stations to (52.2053, 0.1218): {[compact_repr(s) for s in sorted_stations[-10:]]}\n")

if __name__ == '__main__':
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
