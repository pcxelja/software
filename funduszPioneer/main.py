#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 23-03-2013

@author: pcxelja
'''


#print "Pionner - analiza 5-letniego fudnuszu inwestycyjnego"
#print "autor: Pawel Grygorowicz"
#print "v1.3 2013.03.23"


#from Gnuplot import *
import Gnuplot
#import Numeric
#from Numeric import *
from numpy import *

g = Gnuplot.Gnuplot()

Dane = array([[20090615, 80, 29.2, 2.74, 2.74, 77.60, 28.32],
                [20090708, 80, 27.2, 2.941, 5.681, 149.86, 26.38],
                [20090813, 80, 32.58, 2.455, 8.136, 257.10, 31.60],
                [20090914, 80, 32.97, 2.426, 10.562, 337.77, 31.98],
                [20091014, 80, 35.28, 2.268, 12.830, 439.04, 34.22],
                [20091120, 80, 35.12, 2.278, 15.108, 514.73, 34.07],
                [20091214, 80, 35.68, 2.242, 17.350, 600.48, 34.61],
                [20100119, 80, 37.46, 2.136, 19.486, 708.12, 36.34],
                [20100212, 80, 34.53, 2.317, 21.803, 730.12, 33.49],
                [20100323, 80, 37.42, 2.138, 23.941, 869.06, 36.30],
                [20100413, 80, 37.82, 2.115, 26.056, 955.99, 36.69],
                [20100527, 150, 37.14, 4.039, 30.095, 1084.32, 36.03],
                [20100629, 150, 36.88, 4.067, 34.162, 1221.97, 35.77],
                [20100715, 150, 36.81, 4.075, 38.237, 1365.44, 35.71],
                [20100811, 150, 37.19, 4.033, 42.270, 1524.68, 36.07],
                [20100920, 150, 38.16, 3.931, 46.201, 1710.36, 37.02],
                [20101022, 150, 38.87, 3.859, 50.060, 1887.26, 37.70],
                [20101117, 150, 39.32, 3.815, 53.875, 2054.79, 38.14],
                [20101215, 150, 39.73, 3.775, 57.650, 2221.83, 38.54],
                [20110121, 150, 39.45, 3.802, 61.452, 2351.77, 38.27],
                [20110209, 150, 38.74, 3.872, 65.324, 2454.88, 37.58],
                [20110317, 150, 38.61, 3.885, 69.209, 2591.88, 37.45],
                [20110420, 150, 39.47, 3.800, 73.009, 2795.51, 38.29],
                [20110516, 150, 37.74, 3.975, 76.984, 2818.38, 36.61],
                [20110624, 150, 37.08, 4.045, 81.029, 2818.38, 35.97],
                [20110720, 150, 35.32, 4.247, 85.276, 2921.56, 34.26],
                [20110818, 150, 26.35, 5.693, 90.969, 2325.17, 25.56],
                [20110914, 150, 24.66, 6.083, 97.052, 2321.48, 23.92],
                [20111007, 150, 25.48, 5.887, 102.939, 2544.65, 24.72],
                [20111118, 150, 24.10, 6.224, 109.163, 2552.23, 23.38],
                [20111118, 150, 24.10, 6.224, 109.163, 2552.23, 23.38],
                [20111222, 150, 22.61, 6.634, 115.797, 2539.43, 21.93],
                [20120111, 150, 22.80, 6.579, 122.376, 2706.96, 22.12],
                [20120210, 150, 25.23, 5.945, 128.321, 3140.01, 24.47],
                [20120210, 150, 25.23, 5.945, 128.321, 3140.01, 24.47],
                [20120312, 150, 24.98, 6.005, 134.326, 3254.72, 24.23],
                [20120411, 150, 24.33, 6.165, 140.491, 3315.59, 23.60],
                [20120523, 150, 22.61, 6.634, 147.125, 3226.45, 21.93],
                [20120605, 150, 22.65, 6.623, 153.748, 3377.84, 21.97],
                [20120706, 50, 23.44, 2.133, 155.881, 3544.73, 22.74],
                [20120802, 50, 23.12, 2.163, 158.044, 3593.73, 22.43],
                [20120902, 50, 24.74, 2.021, 160.065, 3841.56, 24.00],
                [20121002, 50, 25.27, 1.979, 162.044, 3971.70, 24.51],
                [20121116, 50, 24.69, 2.025, 164.069, 3929.45, 23.95],
                [20121213, 50, 26.37, 1.896, 165.665, 4245.38, 25.58],
                [20130114, 70, 26.89, 2.603, 168.588, 4396.25, 26.08],
                [20130207, 70, 26.38, 2.654, 171.222, 4381.57, 25.59],
                [20130307, 70, 26.32, 2.660, 173.882, 4439.21, 26.32],
                [20130405, 70, 25.07, 2.792, 176.674, 4296.71, 24.32],
                [20130522, 70, 25.77, 2.716, 179.390, 4484.75, 25.00],
                [20130610, 70, 26.92, 2.600, 181.990, 4751.76, 26.11],
                [20130702, 70, 25.41, 2.755, 184.745, 4553.96, 24.65],
                [20130805, 70, 26.84, 2.608, 187.353, 4893.66, 26.12],
                [20130916, 70, 27.24, 2.570, 189.923, 5032.96, 26.50],
                [20131014, 70, 29.03, 2.411, 192.334, 5433.44, 28.25],
                [20131107, 70, 29.23, 2.395, 194.729, 5538.09, 28.44],
                [20131206, 70, 28.53, 2.454, 197.183, 5473.80, 28.53],
                [20140115, 70, 28.12, 2.489, 199.672, 5463.03, 27.36],
                [20140211, 70, 29.14, 2.402, 202.074, 5728.80, 28.35],
                [20140312, 70, 26.57, 2.635, 204.709, 5291.73, 25.85],
                [20140408, 70, 28.38, 2.467, 207.176, 5720.13, 27.61],
                [20140513, 70, 27.24, 2.570, 209.746, 5558.27, 26.50],
                [20140606, 70, 28.45, 2.460, 212.206, 5873.86, 27.68],
                [20140710, 70, 27.26, 2.568, 214.774, 5695,81, 26.52]])
                
DataWyceny = Dane[:,0]
skladka = Dane[:,1]
CenaNabyciaJendostki = Dane[:,2]
LiczbaJednUczestn = Dane[:,3]
LiczbaJednPoTran = Dane[:,4]
WartoscKonta = Dane[:,5]
WartoscAkcjiNetto = Dane[:,6]

ilosc_skladek = Dane.size/7 #Dane.size - ilosc elementow macierzy

print "Ilosc skladek: ", ilosc_skladek
#print "Skladka", skladka

#stowrzenie macierzy zerowej
suma_wplat = array(zeros((ilosc_skladek,1)))

#print "Suma wplat ", suma_wplat

for x in range(0,ilosc_skladek):
    if x == 1:
        suma_wplat[x,0] = skladka[x]        
    else:
        suma_wplat[x,0] = suma_wplat[x - 1,0] + skladka[x]

# Wykres  porownania wartosci konta oraz sum wplat na fundusz
g('set terminal png')
g('set output "/home/pcxelja/wykres1.png"')
g('set xlabel "Data wyceny"')
g('set ylabel "Wartosc [zl]"')
g('set title "Porownanie wartosci konta oraz sum wplat na fundusz"')
g('set grid')
g.plot(suma_wplat,WartoscKonta)
g('unset output')


g('set terminal png')
g('set output "/home/pcxelja/wykres2.png"')
g('set xlabel "Data wyceny"')
g('set ylabel "Wartosc [zl]"')
g('set title "Porownanie akcji netto oraz ceny nabycia jendostki"')
g('set grid')
g.plot(WartoscAkcjiNetto,CenaNabyciaJendostki)
g('unset output')
