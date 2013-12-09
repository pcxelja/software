#!/usr/bin/env python
class FileInfo(dict):
	u"przechowuje metadane pliku" #1
	def __init__(self, filename=None): #2,3,4
	dict.__init__(self)
	self["plik"] = filename

