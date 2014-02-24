import urllib
import re
import time

www = urllib.urlopen('http://www.meteoprog.pl/pl/weather/Wroclaw/')
www_tekst = www.read()

wyrazenie = '<meta property="og:description" content="(.+?)" />'
pogoda = re.findall(wyrazenie, www_tekst)
 
wyrazenie2 = 'd</span><span class="colorNoBold">(.+?)</span>'
wschodzachod = re.findall(wyrazenie2, www_tekst)
 
print time.strftime("%Y-%m-%d, %H:%M:%S")
print '=' * 20
print pogoda[0]
print u'Wsch\u00f3d S\u0142o\u0144ca:', wschodzachod[0]
print u'Zach\u00f3d S\u0142o\u0144ca:', wschodzachod[1]
