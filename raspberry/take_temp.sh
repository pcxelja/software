#!/bin/bash

DATAdlaLINKSA=`date +%Y/%m/%d`
LINK_TEMP="http://www.wunderground.com/history/airport/EPWA/$DATAdlaLINKSA/DailyHistory.html?format=1"

# weryfikacja czy załadowany jest moduł
lsmod | grep w1_therm > /dev/null 2>/dev/null
if [ $? = 0 ]
then
        echo ok >/dev/null
else
        sudo modprobe w1_gpio
        sudo modprobe w1_therm
fi

TEMPczujnik=`cat "/sys/bus/w1/devices/28-000004631ea4/w1_slave"  | grep "t=" | cut -d "=" -f 2`
echo "scale=2;  $TEMPczujnik / 100" | bc
TEMPWAW=`links -width 150 -dump $LINK_TEMP | tail -1 | cut -d "," -f 2`
echo "scale=2; $TEMPWAW * 10" | bc
