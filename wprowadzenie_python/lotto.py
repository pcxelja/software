#!/usr/bin/env python
from random import randint
lista = []
def lotto():
	a = randint(1,49)
	if a not in lista:
		lista.append(a)
	else:
		lotto()
for x in range(6):
	lotto()
print lista
