from flask import Flask, json
import configparser

from Distance.DistanceItem import DistanceItem

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('config.ini')

distanceX = DistanceItem()
distanceX.trig = config['DistanceX']['Trigger'];
distanceX.echo = config['DistanceX']['Echo']
distanceX.initialize()

distanceZ = DistanceItem()
distanceZ.trig = config['DistanceZ']['Trigger'];
distanceZ.echo = config['DistanceZ']['Echo']
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
