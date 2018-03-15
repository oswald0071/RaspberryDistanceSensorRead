from os import environ

from DistanceConfiguration import Config
from Mock.DistanceService import Launcher

if __name__ == '__main__':
    Config.load_from_path('config.ini')
    Config.print_config()
    host = environ.get('SERVER_HOST', 'localhost')
    port = int(environ.get('SERVER_PORT', '5001'))
    Launcher().start(host, port)

