from flask import Flask, json
import configparser

from Distance.DistanceItem import DistanceItem
from DistanceConfiguration import Config

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('config.ini')

distanceX = DistanceItem()
distanceX.trig = Config.x_trigger
distanceX.echo = Config.x_echo
distanceX.initialize()

distanceZ = DistanceItem()
distanceZ.trig = Config.z_trigger
distanceZ.echo = Config.z_echo
distanceZ.initialize()


def start(self, host, port):
    self.app.run(host, port)


@app.route('/')
def hello_world():
    return 'Distance Controller Module'


@app.route('/distance/x')
def get_x_distance():
    return json.dumps({'distance' : distanceX.getDistance()})


@app.route('/distance/z')
def get_z_distance():
    return json.dumps({'distance' : distanceZ.getDistance()})


@app.route('/distance')
def getdistance():
    return json.dumps({'distance_x' : distanceX.getDistance(), 'distance_z' : distanceZ.getDistance()})
