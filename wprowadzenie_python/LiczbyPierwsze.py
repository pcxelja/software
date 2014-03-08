#!/usr/bin/env python

def is_prime(n)
	k = 2
	while k < n:
		if n % k == 0:
			print n
			return False
		k += 1
	return True

n = int(raw_input("Podaj ile liczb wygenerowac: "))


