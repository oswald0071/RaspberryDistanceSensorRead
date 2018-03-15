from flask import Flask, json

from DistanceConfiguration import Config

app = Flask(__name__)


class Launcher:
    @staticmethod
    def start(host, port):
        app.run(host, port)


@app.route('/')
def root():
    return 'Distance Controller Module'


@app.route('/distance')
def get_distance():
    distances = []
    i = 1
    for item in Config.instance.distance_items:
        x = Print(item.name, i)
        i += 1
        distances.append(x.__dict__)

    return json.dumps(distances)


class Print:
    id = ''
    distance = 0

    def __init__(self, id, distance):
        super().__init__()
        self.id = id
        self.distance = distance
