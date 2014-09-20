#!/bin/bash
################################
echo "  --------------------------------------------" >> error.txt
date >> error.txt
echo "  ----------------------------------------------------------------------------------------"
echo "	Archiwizacja danych "
echo -e "	autor: pcxelja"
echo -e " 	ver1.0 2014.09.19"
echo "# ------------------------------------------- #"
echo "# .................. Menu ................... #"
echo "# ------------------------------------------- #"

echo "...... Dysk HDD1024GB ......"
echo "	1. rdiff-backup HDD1024GB"
echo "# ------------------------------------------- #"
echo "...... Dysk HDD250GB ......"
echo "	2. rdiff-backup HDD250GB"
echo "# ------------------------------------------- #"
echo "Wybrales: " 
read A;

echo "# ------------------------------------------- #"

date > error.txt

case "$A" in
	
	"1")  
	echo "#### rdiff-backup 1024GB ####"
	date >> /media/1024GB/backup/data.txt
	echo "process rdiff..."
	rdiff-backup --force ~/rdiff /media/1024GB/rdiff/ 2>> error.txt
	echo "process backup..."
	rdiff-backup --force ~/backup /media/1024GB/backup/ 2>> error.txt
	
	cat error.txt
	;;

	"2")  
	echo "#### rdiff-backup 250GB ####"
	date >> /media/1024GB/backup/data.txt
	echo "process rdiff..."
	rdiff-backup --force ~/rdiff /media/250GB/rdiff/ 2>> error.txt
	echo "process backup..."
	rdiff-backup --force ~/backup /media/250GB/backup/ 2>> error.txt
	
	cat error.txt
	;;
	
  *) echo "Bledna wartosc..."
esac
