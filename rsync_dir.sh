#!/bin/bash
path="/home/amigos/fuel_generator_monitor"
date >> $path/rsync_log.txt
rsync -av -e ssh --bwlimit=100 pi@172.20.0.84:/home/pi/GeneratorMonitor/data /home/amigos/fuel_generator_monitor/Generator_data/ >>$path/rsync_log.txt 2>>$path/rsync_log.txt
rsync -av -e ssh --bwlimit=100 pi@172.20.0.84:/home/pi/FuelMonitor/data /home/amigos/fuel_generator_monitor/Fuel_data/ >>$path/rsync_log.txt 2>>$path/rsync_log.txt
