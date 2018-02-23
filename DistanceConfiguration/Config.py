import configparser

config = configparser.ConfigParser()
config.read('config.ini')

port = config['HOSTING']['Port']
x_echo = config['DistanceX']['Echo']
x_trigger = config['DistanceX']['Trigger']
z_echo = config['DistanceZ']['Echo']
z_trigger = config['DistanceZ']['Trigger']
