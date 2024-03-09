#!/bin/bash

xfce4-terminal -e "./bruteforce.sh    0 2000" &
xfce4-terminal -e "./bruteforce.sh 2001 4000" &
xfce4-terminal -e "./bruteforce.sh 4001 6000" &
xfce4-terminal -e "./bruteforce.sh 6001 8000" &
xfce4-terminal -e "./bruteforce.sh 8001 9999" &