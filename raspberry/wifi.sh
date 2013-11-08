#!/bin/bash
mkdir /var/network
sudo ifdown wlan0
sudo ifup wlan0

#dodanie do autostartu:
#update-rc.d wifi.sh defaults 100

#do WPA potrzebujesz pakiet wpa_supplicant:
#najpierw generujesz sobie plik z hasłem do AP:

#wpa_passphrase nazwa-ssida hasło >moj-ap.conf

#To coś wygeneruje plik z zakodowanym hasłem.

#Potem zazwyczaj wystarczy:
#wpa_supplicant -Dwext -iwlan0 -c moj-ap.conf

