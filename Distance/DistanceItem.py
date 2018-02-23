import time
import RPi.GPIO as gpio


class DistanceItem:
    trig = 17
    echo = 27

    def initialize(self):
        gpio.setmode(gpio.BCM)

        print("Messung startet")
        #print("")

        gpio.setup(self.trig, gpio.OUT)
        gpio.setup(self.echo, gpio.IN)

        gpio.output(self.trig,False)

        time.sleep(0.5)

    def getDistance(self):

        gpio.output(self.trig,True)
        time.sleep(0.00001)
        gpio.output(self.trig,False)

        while gpio.input(self.echo) == 0:
            start = time.time()

        while gpio.input(self.echo) == 1:
            stop = time.time()
    
        vergangeneZeit = stop-start

        entfernung = round(vergangeneZeit*34000/2, 2)
        print(entfernung)
        return entfernung
