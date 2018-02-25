# RaspberryDistanceSensorRead
Read a raspberry GPIO Distance Sensor via python script

# Preconditions
python plugin configparser
```
pip install configparser
```

# Installation
Simply clone this repo

# Configuration
In the config.ini-File you can set the following settings:
```
[HOSTING]
Port = 5001

[Distance]
Items = DistanceX,DistanceZ

[DistanceX]
Echo = 17
Trigger = 27

[DistanceZ]
Echo = 3
Trigger = 5
```

# Starting
```
python DistanceService.py
```

# Development
Intellij with python plugin

# Contributions
desired

# License
MIT