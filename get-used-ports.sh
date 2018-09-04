#!/usr/bin/env bash

# find ./ -iname "*.tunnel*" -exec egrep ^MON {​‌​} \; |sort | sed -r 's/^MON.*?\=//g'

echo "Allocated Monitor Ports:" | tee -a ./allocated-ports.txt

find . -iname "*.tunnel" -exec egrep "^MONITOR" {} \; | sed -r 's/^MON.*?=//g' | sort  | tee -a ./allocated-ports.txt



sleep 20
