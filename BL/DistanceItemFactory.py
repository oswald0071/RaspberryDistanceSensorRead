import DistanceConfiguration
from BL import DistanceItem


def get_init_distance_items():
    config_items = DistanceConfiguration.instance.distance_items
    distances = []
    i = 1
    for item in config_items:
        x = DistanceItem.DistanceItem(item)
        i += 1
        distances.append(x)
    return distances
