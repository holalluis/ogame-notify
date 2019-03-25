#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
  CALCUL PRODUCTIVITAT: TEMPS DE VOL, CONSUM COMBUSTIBLE I BENEFICIS
  farming: sondes vs naus de càrrega
  formules: https://ogame.fandom.com/es/wiki/F%C3%B3rmulas#Tiempo_de_Vuelo

  TODO: calcular amortitzacio
  TODO: equivalencia naus petites grans o espionatge
'''
import math  as m
import ogame as o
o.motor_c = 9 #motor combustión: augmenta velocitat PC i GC
o.motor_i = 6 #motor impulso: augmenta velocitat PC a partir del nivell 5
o.tec_hip = 6 #tecnologia hiperespacio: augmenta 5% càrrega

#inputs
boti = 212e3/2 #botí possible
s1   = 438 #sistema sortida
s2   = 414 #sistema arribada

flotes=[
  #o.Sondes(60),
  o.NausPC(16),
  #o.NausGC(2),
]
#simulacions
for f in flotes:
  f.viatge(s1,s2,boti) 
