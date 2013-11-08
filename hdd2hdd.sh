#!/bin/bash
################################
#echo '################################ ' >> error.txt
#date >> error.txt
echo '################################ ' >> error.txt
echo "  ----------------------------------------------------------------------------------------"
echo "	Synchronizacja danych miedzy hdd "
echo -e "	autor: Pawel Grygorowicz"
echo -e " 	ver1.3 2012.02.04"
echo "  --------------------------------------------"
echo "... Menu ..."
echo "1. df"
echo "2. fdisk -l"
echo "3. mount "
echo "  --------------------------------------------"
echo "31. unmount "
echo "  --------------------------------------------"
echo " ############### HDD250GB ###############"
echo "4. rsync hdd1000GB"
echo "41. scp2hdd hdd1000GB"
echo "  --------------------------------------------"
echo "42. diff rsync&scp hdd1000GB"
echo "  --------------------------------------------"
echo "43. rdiff-backup hdd1000GB"
echo "  --------------------------------------------"
echo "44. diff rdiff_backup&scp hdd1000GB"
echo "  --------------------------------------------"
echo "45. diff rdiff-backup&rsync"
echo "  --------------------------------------------"
echo " ############### HDD1000GB ###############"
echo "5. rsync hdd1000GB"
echo "51. scp2hdd hdd1000GB"
echo "  --------------------------------------------"
echo "52. diff rsync&scp hdd1000GB"
echo "  --------------------------------------------"
echo "53. rdiff-backup hdd1000GB"
echo "  --------------------------------------------"
echo "54. diff rdiff_backup&scp hdd1000GB"
echo "  --------------------------------------------"
echo "55. diff rdiff-backup&rsync"
echo "  --------------------------------------------"
echo " ############### HDD160GB ###############"
echo "6. scp2hdd hdd160GB"
echo "  --------------------------------------------"
echo " ############### pcxelja ###############"
echo "7. rsync hdd1000GB"
echo "71. scp hdd1000GB"
echo "7. rdiff-backup hdd1000GB"
echo "  --------------------------------------------"
echo " ############### vocadi ###############"
echo "8. video hdd1000GB"
echo "81. video hdd250GB"
echo "  --------------------------------------------"
#echo "8. rdiff-backup hdd1000GB"
#echo "  --------------------------------------------"
#echo "9. rdiff-backup hdd250GB"
#echo "  --------------------------------------------"
echo "Wybrales: "
read A;

case "$A" in
	
	"1")  
	df;;
	
	"2")  
	sudo fdisk -l;;
	
	"3")  
	sudo mount /dev/sdc1 /media/hdd250GB
	sudo mount /dev/sda1 /media/hdd160GB
	sudo mount /dev/sdd1 /media/hdd1000GB 
	;;
	
	"31")  
	sudo umount /media/hdd250GB
	sudo umount /media/hdd160GB
	sudo umount /media/hdd1000GB 
	;;
	
#   ------------- HDD_250GB -------------
	
	"4")
	echo "rsync ..."
	sudo rsync -avvhze --delete /home/vocadi/backup/asus-k5/cyfra_drop /media/hdd250GB/backup_rsync
	sudo rsync -avvhze --delete /home/vocadi/backup/asus-k5/Dropbox /media/hdd250GB/backup_rsync
	sudo rsync -avvhze --delete /home/vocadi/backup/asus-k5/cyfra /media/hdd250GB/backup_rsync
	;;
	
	"41")
	sudo scp -r /home/vocadi/backup/asus-k5/Dropbox /media/hdd250GB/backup_scp
	sudo scp -r /home/vocadi/backup/asus-k5/cyfra /media/hdd250GB/backup_scp
	sudo scp -r /home/vocadi/backup/asus-k5/cyfra_drop /media/hdd250GB/backup_scp
	;;
	
	"42")
	date > diff_52_hdd250GB.txt
	diff -r /media/hdd250GB/backup_rsync/ /media/hdd250GB/backup_scp/ >> diff_52_hdd250GB.txt
	;;
	
	"43")
	sudo rdiff-backup /home/vocadi/backup/asus-k5/Dropbox /media/hdd250GB/backup_rdiff/Dropbox
	sudo rdiff-backup /home/vocadi/backup/asus-k5/cyfra /media/hdd250GB/backup_rdiff/cyfra
	sudo rdiff-backup /home/vocadi/backup/asus-k5/cyfra_drop /media/hdd250GB/backup_rdiff/cyfra_drop
	;;
	
	"44")
	date > diff_54_hdd250GB.txt
	diff -r /media/hdd250GB/backup_rsync/ /media/hdd250GB/backup_rdiff/ >> diff_54_hdd250GB.txt
	;;
	
	"45")
	diff -r diff_54_hdd250GB.txt diff_52_hdd250GB.txt
	;;
	
#	"4")	
#	echo "rsync ..."
	#date >> pcxelja@192.168.0.2:backup/rsync/ #2>> data.txt
	#rsync -avvhze --delete /home/vocadi/backup/asus-k5/Dropbox /media/hdd250GB/backup 2>> error.txt
#	rsync -avvhze --delete /home/vocadi/backup/asus-k5/cyfra_drop /media/hdd250GB/backup #2>> error.txt
#	;;
	
#	"41")
#	sudo scp -r /home/vocadi/backup/asus-k5/Dropbox /media/hdd250GB/backup/Dropbox
#	sudo scp -r /home/vocadi/backup/asus-k5/cyfra /media/hdd250GB/backup/cyfra
#	sudo scp -r /home/vocadi/backup/asus-k5/cyfra_drop /media/hdd250GB/backup/cyfra_drop
#	;;

#   ------------- HDD_1000GB -------------	
	"5")
	echo "rsync ..."
	sudo rsync -avvhze --delete /home/vocadi/backup/asus-k5/cyfra_drop /media/hdd1000GB/backup_rsync
	sudo rsync -avvhze --delete /home/vocadi/backup/asus-k5/Dropbox /media/hdd1000GB/backup_rsync
	sudo rsync -avvhze --delete /home/vocadi/backup/asus-k5/cyfra /media/hdd1000GB/backup_rsync
	;;
	
	"51")
	sudo scp -r /home/vocadi/backup/asus-k5/Dropbox /media/hdd1000GB/backup_scp
	sudo scp -r /home/vocadi/backup/asus-k5/cyfra /media/hdd1000GB/backup_scp
	sudo scp -r /home/vocadi/backup/asus-k5/cyfra_drop /media/hdd1000GB/backup_scp
	;;
	
	"52")
	date > diff_52_hdd1000GB.txt
	diff -r /media/hdd1000GB/backup_rsync/ /media/hdd1000GB/backup_scp/ >> diff_52_hdd1000GB.txt
	;;
	
	"53")
	sudo rdiff-backup /home/vocadi/backup/asus-k5/Dropbox /media/hdd1000GB/backup_rdiff/Dropbox
	sudo rdiff-backup /home/vocadi/backup/asus-k5/cyfra /media/hdd1000GB/backup_rdiff/cyfra
	sudo rdiff-backup /home/vocadi/backup/asus-k5/cyfra_drop /media/hdd1000GB/backup_rdiff/cyfra_drop
	;;
	
	"54")
	date > diff_54_hdd1000GB.txt
	sudo diff -r /media/hdd1000GB/backup_rsync/ /media/hdd1000GB/backup_rdiff/ >> diff_54_hdd1000GB.txt
	;;
	
	"55")
	diff -r diff_54_hdd1000GB.txt diff_52_hdd1000GB.txt
	;;

#   ------------- HDD_160GB -------------	
	
	"6")
	sudo scp -r /home/vocadi/backup/asus-k5/Dropbox /media/hdd160GB/backup/Dropbox
	sudo scp -r /home/vocadi/backup/asus-k5/cyfra /media/hdd160GB/backup/cyfra
	sudo scp -r /home/vocadi/backup/asus-k5/cyfra_drop /media/hdd160GB/backup/cyfra_drop
	;;

#   ------------- pcxelja -------------	
  
	"7")  
	echo " backup hdd_1000GB"
	rdiff-backup ~/backup/rdiff_backup /media/hdd1000GB/pcxelja/rdiff_backup
	scp -r ~/backup/scp /media/hdd1000GB/pcxelja/scp
	rsync -avvhze --delete ~/backup/rsync /media/hdd1000GB/pcxelja/rsync
	;;
	
	"71")  
	echo " backup hdd_250GB"
	scp -r ~/backup/scp /media/hdd250GB/pcxelja/scp	
	;;
	
	"72")  
	echo " backup hdd_160GB"
	scp -r ~/backup/scp /media/hdd160GB/pcxelja/scp	
	;;

#   ------------- video -------------	
	
	"8")  
	echo "video hdd1000GB"
	sudo scp -r /home/vocadi/backup/video /media/hdd1000GB/
	;;
	
	"81")  
	echo "video hdd250GB"
	sudo scp -r /home/vocadi/backup/video /media/hdd250GB/
	;;
 
#	"8")
#	sudo rdiff-backup /home/vocadi/backup/asus-k5/cyfra /media/hdd1000GB/backup/cyfra/ 2>> error.txt
#	cat error.txt
#	sudo rdiff-backup /home/vocadi/backup/asus-k5/cyfra_drop /media/hdd1000GB/backup/cyfra_drop/ 2>> error.txt
#	cat error.txt
#	sudo rdiff-backup /home/vocadi/backup/asus-k5/Dropbox /media/hdd1000GB/backup/Dropbox/ 2>> error.txt
#	cat error.txt
#	rdiff-backup /home/pcxelja/backup/pcxelja /media/hdd1000GB/backup/pcxelja/ 2>> error.txt
#	cat error.txt
#	sudo rdiff-backup /home/vocadi/backup/video /media/hdd1000GB/backup/video/ 2>> error.txt
#	cat error.txt
	
	#sudo rdiff-backup /home/vocadi/backup/asus-k5/cyfra /media/hdd250GB/backup/ #2>> error.txt
	#sudo rdiff-backup /home/vocadi/backup/asus-k5/cyfra_drop /media/hdd250GB/backup/ #2>> error.txt
	#sudo rdiff-backup /home/vocadi/backup/asus-k5/Dropbox /media/hdd250GB/backup/ #2>> error.txt
#	;;
	
#	"9")
#	sudo rdiff-backup /home/vocadi/backup/asus-k5/cyfra /media/hdd250GB/backup/cyfra/ 2>> error.txt
#	sudo rdiff-backup /home/vocadi/backup/asus-k5/cyfra_drop /media/hdd250GB/backup/cyfra_drop/ 2>> error.txt
#	cat error.txt
#	sudo rdiff-backup /home/vocadi/backup/asus-k5/Dropbox /media/hdd250GB/backup/Dropbox/ 2>> error.txt
#	cat error.txt
#	rdiff-backup /home/pcxelja/backup/pcxelja /media/hdd250GB/backup/pcxelja/ 2>> error.txt
#	cat error.txt
#	sudo rdiff-backup /home/vocadi/backup/video /media/hdd250GB/backup/video/ 2>> error.txt
#	cat error.txt
	
	#sudo rdiff-backup /home/vocadi/backup/asus-k5/cyfra /media/hdd250GB/backup/ #2>> error.txt
	#sudo rdiff-backup /home/vocadi/backup/asus-k5/cyfra_drop /media/hdd250GB/backup/ #2>> error.txt
	#sudo rdiff-backup /home/vocadi/backup/asus-k5/Dropbox /media/hdd250GB/backup/ #2>> error.txt
#	;;
  
  *) echo "Bledna wartosc..."
esac
