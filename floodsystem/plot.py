from .station import MonitoringStation
import matplotlib.pyplot as plt

def plot_water_levels(station: MonitoringStation,dates: list, levels: list):
    plt.plot(dates,levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title(f"{station.name} water level data")
    plt.axhline(y=station.typical_range[0], color='r', linestyle='-')
    plt.axhline(y=station.typical_range[1], color='r', linestyle='-')
    plt.tight_layout(rect=[0, 0.09, 1, 0.95])
    plt.xticks(rotation=45)
    plt.show()
