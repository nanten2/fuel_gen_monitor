#!/bin/bash
cd /home/amigos/fuel_generator_monitor
date >> "makegraphlog.txt"
python3 /home/amigos/fuel_generator_monitor/fuel24_v2.py 1>> "makegraphlog.txt" 2>> "makegraphlog.txt"
python3 /home/amigos/fuel_generator_monitor/fuel120_v3.py 2>> "makegraphlog.txt"
python3 /home/amigos/fuel_generator_monitor/fuel14day.py 2>> "makegraphlog.txt"
python3 /home/amigos/fuel_generator_monitor/Generator24_v2.py 2>> "makegraphlog.txt"
python3 /home/amigos/fuel_generator_monitor/Generator120_v2.py 2>> "makegraphlog.txt"
