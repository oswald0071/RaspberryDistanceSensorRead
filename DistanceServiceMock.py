from os import environ

from Mock.DistanceService import Launcher

if __name__ == '__main__':
    host = environ.get('SERVER_HOST', 'localhost')
    port = int(environ.get('SERVER_PORT', '5001'))
    Launcher().start(host, port)

