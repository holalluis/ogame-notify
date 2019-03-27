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

#inputs
boti = 78e3/2 #botí possible
s1   = 438 #sistema sortida
s2   = 414 #sistema arribada

o.motor_c = 10 #motor combustión (velocitat)
o.motor_i = 7  #motor impulso (velocitat)
o.tec_hip = 7  #tecnologia hiperespacio (càrrega)

#flotes per simular
flotes=[
  o.NausPC(),
  o.Sondes(), #o.NausGC(2),
]

#simulacions
for f in flotes:
  f.viatge(s1,s2,boti) 
