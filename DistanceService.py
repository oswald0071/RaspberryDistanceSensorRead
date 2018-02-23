import json
from flask import Flask
from os import environ
import struct

from Distance.DistanceItem import DistanceItem

app = Flask(__name__)
distanceX = DistanceItem()
distanceX.initialize()


@app.route('/')
def hello_world():
    return 'Distance Controller Module'


@app.route('/dist/x')
def getXdistance():
    return json.dumps({'distance' : distanceX.getDistance()})
