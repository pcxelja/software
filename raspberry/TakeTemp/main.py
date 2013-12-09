#!/usr/bin/env python

import os

path = "/sys/bus/w1/devices/"
czujnik_1 = "28-000004631ea4/w1_slave"

def take_temp(path, czujnik):
	u"zwraca wartosc temperatury z czujnika [C]"
	czujnik = os.path.join(path + czujnik)

