import time
import RPi.GPIO as gpio

from DistanceConfiguration import DistanceConfigItem


max_wait_time_sec = 1


class DistanceItem:
    name = ''
    echo = -1
    trigger = -1

    def __init__(self, config_item: DistanceConfigItem) -> None:
        super().__init__()
        self.name = config_item.name
        self.echo = config_item.echo
        self.trigger = config_item.trigger
        # TODO: open the port
        print('Initialize distance-sensor on ' + str(self))
        gpio.setmode(gpio.BCM)
        gpio.setup(self.trigger, gpio.OUT)
        gpio.setup(self.echo, gpio.IN)
        gpio.output(self.trigger, False)
        time.sleep(0.5)
        print('port initialized')

    def get_distance(self) -> int:
        print('get distance from ' + str(self))
        gpio.output(self.trigger, True)
        time.sleep(0.00001)
        gpio.output(self.trigger, False)

        start = time.time()
        while gpio.input(self.echo) == 0:
            start = time.time()

        max_time = time.time() + max_wait_time_sec

        timeout_reached = False
        while gpio.input(self.echo) == 1:
            if time.time() > max_time:
                timeout_reached = True
                print('WARNING wait timeout reached!')
                break
            stop = time.time()

        passed_time = stop - start

        distance = -1
        if not timeout_reached:
            distance = round(passed_time * 34000 / 2, 2)
        print('measured distance: ' + str(distance))
        return distance

    def __str__(self) -> str:
        return 'Echo: ' + str(self.echo)\
               + ' Trigger: ' + str(self.trigger)

