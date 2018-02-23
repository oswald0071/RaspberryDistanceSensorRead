from flask import Flask, json

from Distance.DistanceItem import DistanceItem
from DistanceConfiguration import Config

app = Flask(__name__)

distanceX = DistanceItem()

#distanceZ = DistanceItem()
#distanceZ.trig = int(Config.z_trigger)
#distanceZ.echo = int(Config.z_echo)
#distanceZ.initialize()


class Launcher:
    @staticmethod
    def start(host, port):
        distanceX.trig = int(Config.x_trigger)
        distanceX.echo = int(Config.x_echo)
        distanceX.initialize()
        app.run(host, port)


@app.route('/')
def hello_world():
    return 'Distance Controller Module'


@app.route('/distance/x')
def get_x_distance():
    return json.dumps({'distance' : distanceX.getDistance()})


#@app.route('/distance/z')
#def get_z_distance():
#    return json.dumps({'distance' : distanceZ.getDistance()})


@app.route('/distance')
def getdistance():
    return json.dumps({'distance_x' : distanceX.getDistance()}) #, 'distance_z' : distanceZ.getDistance()
