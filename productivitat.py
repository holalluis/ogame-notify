#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
  CALCUL PRODUCTIVITAT: TEMPS DE VOL, CONSUM COMBUSTIBLE I BENEFICIS
  farming: sondes vs naus de càrrega
  formules: https://ogame.fandom.com/es/wiki/F%C3%B3rmulas#Tiempo_de_Vuelo
  TODO: calcular amortitzacio
  TODO: equivalencia naus petites grans o espionatge
'''
import ogame as o
kkk       = 200       # recursos (k) al planeta
s1        = 438       # sistema sortida
s2        = 414       # sistema arribada
o.motor_c = 14        # motor combustión (velocitat)
o.motor_i = 9         # motor impulso (velocitat)
o.tec_hip = 10        # tecnologia hiperespacio (càrrega)
boti      = kkk*1e3/2 # botí màxim (50%)

#flotes per simular
flotes=[
  o.NausPC(),
  o.Sondes(600),
  #o.NausGC(2),
]

#simulacions
for f in flotes: f.viatge(s1,s2,boti)
