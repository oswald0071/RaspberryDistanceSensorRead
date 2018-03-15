from flask import Flask, json
from BL import DistanceItemFactory

app = Flask(__name__)


class Service:
    distance_items = object()

    def start(self, host, port):
        self.distance_items = DistanceItemFactory.get_init_distance_items()
        app.run(host, port)


instance = Service()


@app.route('/')
def hello_world():
    return 'Distance Controller Module'


@app.route('/distance')
def get_distance():
    distances = []
    for item in instance.distance_items:
        x = Print(item.name, item.get_distance())
        distances.append(x.__dict__)

    return json.dumps(distances)


class Print:
    id = ''
    distance = 0

    def __init__(self, id, distance):
        self.id = id
        self.distance = distance
