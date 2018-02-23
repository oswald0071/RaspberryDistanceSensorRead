import time
import RPi.GPIO as gpio


class DistanceItem:
    trig = 17
    echo = 27

    def initialize(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(self._trig, gpio.OUT)
        gpio.setup(self._echo, gpio.IN)
        gpio.output(self._trig,False)
        print('Messung auf GPIO ' + str(self._gpioPort) + ' started.')
        time.sleep(0.5)

    def getDistance(self):
        print('Begin measurement.')
        gpio.output(self._trig,True)
        time.sleep(0.00001)
        gpio.output(self._trig,False)

        while gpio.input(self._echo) == 0:
            start = time.time()

        while gpio.input(self._echo) == 1:
            stop = time.time()

        timeleft = stop-start

        distance = round(timeleft*34000/2, 2)
        print('Measured Distance: ' + str(distance))
        return distance
