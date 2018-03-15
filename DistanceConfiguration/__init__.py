import configparser

from DistanceConfiguration.DistanceConfigItem import DistanceModel


class Config:
    distance_items = []
    port = -1


instance = Config()


def load_from_path(path):
    config = configparser.ConfigParser()
    config.read(path)
    instance.port = config.getint('HOSTING', 'Port')
    distance_item_names = str(config['Distance']['Items']).split(',')
    print(distance_item_names)
    for item in distance_item_names:
        print(item)
        x = DistanceModel()
        x.name = item
        x.echo = config.getint(item, 'Echo')
        x.trigger = config.getint(item, 'Trigger')
        instance.distance_items.append(x)


def print_config():
    for item in instance.distance_items:
        print('Name: ' + str(item.name) + ' Echo: ' + str(item.echo) + ' Trigger: ' + str(item.trigger))
