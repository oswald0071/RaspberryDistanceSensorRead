import configparser

config = configparser.ConfigParser()
config.read('config.ini')

x_echo = config['DistanceX']['Echo']
x_trigger = config['DistanceX']['Trigger']
z_echo = config['DistanceZ']['Echo']
z_trigger = config['DistanceZ']['Trigger']
