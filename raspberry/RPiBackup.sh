#!/bin/bash
sudo /etc/init.d/lighttpd stop
#sudo /etc/init.d/noip stop
sudo /etc/init.d/shairport stop
sudo /etc/init.d/cron stop
sudo dd if=/dev/mmcblk0 of=/Sciezka_do_kopii_zapasowej.img
#sudo /etc/init.d/cron start
#sudo /etc/init.d/lighttpd start
#sudo /etc/init.d/noip start
#sudo /etc/init.d/shairport start

