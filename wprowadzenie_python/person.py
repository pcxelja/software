#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  person.py
#  
#  Copyright 2013 Pawel Grygorowicz <pcxelja@F80Q>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

class Person:
	def __init__(self, name, job = None, pay = 0):
		self.name = name
		self.job = job
		self.pay = pay


	def lastName(self):
		return self.name.split()[-1]
	
	def giveRaise(self, percent):
		self.pay = int(self.pay * (1 + (percent)))

if __name__ == "__main__":
	bob = Person('Robet Zielony')
	anna = Person('Anna Czerwona', job = 'programista', pay = 1000)
	print(bob.name, bob.pay)
	print(anna.name, anna.pay)
	print(bob.lastName(), anna.lastName())
	anna.giveRaise(0.1)
	print(anna.pay)

