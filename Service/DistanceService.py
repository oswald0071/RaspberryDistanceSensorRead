from flask import Flask, json

from Distance.DistanceItem import DistanceItem
from DistanceConfiguration import Config

app = Flask(__name__)

distanceX = DistanceItem()

#distanceZ = DistanceItem()
#distanceZ.trig = int(Config.z_trigger)
#distanceZ.echo = int(Config.z_echo)
#distanceZ.initialize()

distanceItems = []

class Launcher:
    @staticmethod
    def start(host, port):
        for item in Config.distanceItems:
            x = DistanceItem()
            x.name = item.name
            x.echo = item.echo
            x.trigger = item.trigger
        x.initialize()
        distanceItems.append(x)
        app.run(host, port)


@app.route('/')
def hello_world():
    return 'Distance Controller Module'


@app.route('/distance')
def get_distance():
    distances = []
    for item in distanceItems:
        x = Print(item.name, item.getDistance())
        distances.append(x.__dict__)

    return json.dumps(distances)


class Print:
    id = ''
    distance = 0

    def __init__(self, id, distance):
        self.id = id
        self.distance = distance
