#!/bin/bash
################################

echo "# ------------------------------------------- #"

#date >> diff.txt
rsync -Havz --delete ~/temp ~/temp2
diff -r ~/temp ~/temp2/temp
