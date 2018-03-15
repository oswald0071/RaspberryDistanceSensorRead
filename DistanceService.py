import socket
import fcntl
import struct

from DistanceConfiguration import Config
from Service.DistanceService import Launcher


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

if __name__ == '__main__':
    Config.load_from_path('config.ini')
    Config.print_config()
    host = get_ip_address('wlan0')
    port = Config.instance.port
    print('Host: ' + str(host) + ' Port: ' + str(port))
    Launcher.start(host, port)
