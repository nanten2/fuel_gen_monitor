#!/bin/bash
cd /home/amigos/fuel_generator_monitor
date >> "makegraphlog.txt"
python3 /home/amigos/fuel_generator_monitor/fuel_graph24h.py 1>> "makegraphlog.txt" 2>> "makegraphlog.txt"
python3 /home/amigos/fuel_generator_monitor/fuel_graph120h.py 2>> "makegraphlog.txt"
python3 /home/amigos/fuel_generator_monitor/fuel_graph14days.py 2>> "makegraphlog.txt"

