from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def compact_repr(stat):
    return (stat[0].name,stat[0].town,stat[1])
def run():
    """Requirements for Task 1B"""
    
    # Build list of stations
    stations = build_station_list()
   
    # Get list of stations ordered by distance from Cambridge
    sorted_stations = stations_by_distance(stations,(52.2053, 0.1218))

    # Print 10 closest and furthest stations from sorted_stations
    print(f"10 closest stations to (52.2053, 0.1218): {[compact_repr(s) for s in sorted_stations[:10]]}\n")
    print(f"10 furthest stations to (52.2053, 0.1218): {[compact_repr(s) for s in sorted_stations[-10:]]}\n")

if __name__ == '__main__':
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
