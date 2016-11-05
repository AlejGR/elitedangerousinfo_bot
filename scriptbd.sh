#!/bin/sh
rm /home/ubuntu/workspace/systems.json
wget -c https://eddb.io/archive/v4/systems.json
python3 scriptdb.py
echo Tarea completada