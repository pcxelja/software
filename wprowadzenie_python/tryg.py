#!/usr/bin/env python
from math import * #badanie hsg
kat = input ("Podaj wielkosc kata w stopniach: ")
print "%+5.3f" % sin(radians(kat))
print "%+3.5f" % cos(radians(kat))
if radians(kat) % (pi/2) == 0:
	print "Nie ma takiego tangensa"
else:
	print "%+5.3f" % tan(radians(kat))
if radians(kat) % (pi) == 0:
	print "nie ma takiego cotamgensa"
else:
	print "%+5.3f" % (1/tan(radians(kat)))
