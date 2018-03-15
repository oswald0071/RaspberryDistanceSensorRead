import socket
import os

import DistanceConfiguration
from Service import DistanceService


def get_ip_address():
    gw = os.popen("ip -4 route show default").read().split()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((gw[2], 0))
    return s.getsockname()[0]


if __name__ == '__main__':
    DistanceConfiguration.load_from_path('config.ini')
    DistanceConfiguration.print_config()
    host = get_ip_address()
    port = DistanceConfiguration.instance.port
    print('Host: ' + str(host) + ' Port: ' + str(port))
    DistanceService.instance.start(host, port)
