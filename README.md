# RaspberryDistanceSensorRead
Read a raspberry GPIO Distance Sensor via python script

# Installation
Simply clone this repo

# Configuration
In the config.ini-File you can set the following settings:
```
[HOSTING]
Port = 5001

[Distance]
Items = DistanceX,DistanceY

[DistanceX]
Echo = 17
Trigger = 27

[DistanceY]
Echo = 3
Trigger = 5
```

# Starting
```
python DistanceService.py
```

# Contributions
desired