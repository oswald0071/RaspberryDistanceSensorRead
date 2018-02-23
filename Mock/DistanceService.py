from flask import Flask, json
import configparser
from DistanceConfiguration import Config

app = Flask(__name__)

class Launcher:
    @staticmethod
    def start(host, port):
        app.run(host, port)


@app.route('/')
def hello_world():
    return 'Distance Controller Module'


@app.route('/distance/x')
def get_x_distance():
    return json.dumps({'distance' : Config.x_echo})


@app.route('/distance/z')
def get_z_distance():
    return json.dumps({'distance' : Config.z_echo})


@app.route('/distance')
def getdistance():
    return json.dumps({'distance_x' : Config.x_trigger, 'distance_z' : Config.z_echo})
