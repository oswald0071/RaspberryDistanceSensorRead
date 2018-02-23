from flask import Flask, json
import configparser

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

print(config['HOSTING']['Port'])
xEcho = config['DistanceX']['Echo']
xTrigger = config['DistanceX']['Trigger']
yEcho = config['DistanceY']['Echo']
yTrigger = config['DistanceY']['Trigger']
print({'xEcho': xEcho, 'xTrigger': xTrigger, 'yEcho': yEcho, 'yTrigger': yTrigger})


class Launcher:
    @staticmethod
    def start(host, port):
        app.run(host, port)


@app.route('/')
def hello_world():
    return 'Distance Controller Module'


@app.route('/distance/x')
def get_x_distance():
    return json.dumps({'distance' : xEcho})


@app.route('/distance/z')
def get_z_distance():
    return json.dumps({'distance' : 14})


@app.route('/distance')
def getdistance():
    return json.dumps({'distance_x' : 12, 'distance_z' : 14})
