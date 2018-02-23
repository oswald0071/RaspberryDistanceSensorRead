import configparser
import json

from DistanceConfiguration.DistanceModel import DistanceModel

config = configparser.ConfigParser()
config.read('config.ini')

port = config.getint('HOSTING', 'Port')

distanceItemNames = str(config['Distance']['Items']).split(',')
print(distanceItemNames)
distanceItems = []
for item in distanceItemNames:
    print(item)
    x = DistanceModel()
    x.name = item
    x.echo = config[item]['Echo']
    x.trigger = config[item]['Trigger']
    distanceItems.append(x)

