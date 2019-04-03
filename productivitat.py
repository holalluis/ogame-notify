#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ogame as o
'''
  CALCUL PRODUCTIVITAT: TEMPS DE VOL, CONSUM COMBUSTIBLE I BENEFICIS
  farming: sondes vs naus de càrrega
  formules: https://ogame.fandom.com/es/wiki/F%C3%B3rmulas#Tiempo_de_Vuelo
  TODO: calcular amortitzacio
  TODO: equivalencia naus petites grans o espionatge
'''
kkk       = 446  #recursos (k) al planeta
s1        = 438  #sistema sortida
s2        = 414  #sistema arribada
o.motor_c = 10   #motor combustión (velocitat)
o.motor_i = 7    #motor impulso (velocitat)
o.tec_hip = 7    #tecnologia hiperespacio (càrrega)
boti = kkk*1e3/2 #botí màxim (50%)

#flotes per simular
flotes=[
  o.NausPC(),
  #o.Sondes(), #o.NausGC(2),
]

botins=[60, 100, 120, 150, 180, 200]

#simulacions
for f in flotes: f.viatge(s1,s2,boti) 
