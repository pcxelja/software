#!/usr/bin/env python
import string
cyfry = ('zero','jeden','dwa','trzy','cztery','piec','szczesc','siedem','osiem','dziewiec')
ciag = raw_input('Podaj ciag cyfr: ')
for x in ciag:
	if x not in string.digits: continue
	print cyfry[int(x)]


