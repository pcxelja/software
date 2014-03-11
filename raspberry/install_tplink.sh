#sudo su -
#wget http://raspishop.pl/downloads/8188eu.ko-raspbian -O /lib/modules/`uname -r`/kernel/drivers/net/wireless/8188eu.ko
sudo depmod -a
sed -i 's/^exit 0/modprobe 8188eu\nexit 0/' /etc/rc.local
reboot
