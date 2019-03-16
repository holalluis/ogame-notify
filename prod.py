#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
  CALCUL TEMPS DE VOL I CONSUM COMBUSTIBLE
  calcular productivitat farming amb sondes vs farming amb naus de càrrega
  formules: https://ogame.fandom.com/es/wiki/F%C3%B3rmulas#Tiempo_de_Vuelo

  TODO: calcular amortitzacio
  TODO: equivalencia naus petites grans o espionatge

'''
import math as m

#inputs
s1      = 438 #sistema sortida
s2      = 391 #sistema arribada
motor_c = 5   #motor combustión
motor_i = 3   #motor impulso (no implementat de moment)

#classe cost
class Cost:
  def __init__(self, metal, cristal, deuterio):
    self.metal    = metal
    self.cristal  = cristal
    self.deuterio = deuterio

  def __str__(self):
    return "[%d,%d,%d]" % (self.metal, self.cristal, self.deuterio)

  #cost unitats absolutes ratio 3:2:1
  def absolut(self):
    return 3*self.deuterio + 2*self.cristal + 1*self.metal

#classe flota
class Naus:
  def __init__(self, numero, carrega, velocitat, consum, cost):
    self.numero    = int(numero)    #quantitat de naus
    self.carrega   = int(carrega)   #carrega que pot portar 1 nau
    self.velocitat = int(velocitat) #velocitat base
    self.consum    = consum         #consum 1 nau
    self.cost      = cost           #cost 1 nau

  def __str__(self):
    return "Naus: %d | Càrrega: %d (%d) | Velocitat: %d | Consum: %.1f | Cost: %s (%d uabs)" % (
      self.numero,
      self.carrega,
      self.numero*self.carrega,
      self.velocitat,
      self.consum,
      self.cost,
      self.numero*self.cost.absolut()
    )

  #temps de vol entre 2 sistemes s1 s2
  def temps_de_vol(self, percent, s1, s2):
    vel = self.velocitat
    dis = distancia(s1,s2)
    return 10+35e3/percent*m.sqrt(1e3*dis/(vel+0.10*vel*motor_c))

  #consum combustible entre 2 sistemes s1 s2
  def combustible(self, percent, s1, s2):
    voltes = 1
    consum = self.consum
    n      = self.numero
    return 1+n*voltes*consum*distancia(s1,s2)/35e3*m.pow(percent/100+1,2)

  #productivitat: recursos per hora
  def productivitat(self,perc,s1,s2):
    bote   = self.numero*self.carrega            #boti total viatge
    bote  -= round(self.combustible(perc,s1,s2)) #resta combustible
    segons = self.temps_de_vol(perc,s1,s2)       #segons totals viatge
    cost   = self.numero*self.cost.absolut()     #inversió
    return bote/segons/cost*3600 #kunitats/h
    
  def viatge(self,s1,s2):
    print("[+] Viatge ",s1,"-->",s2,"| Distancia:",distancia(s1,s2))
    print(self)
    #10% 20% 30% ... 100%
    for perc in range(100,101,10):
      segons = round(self.temps_de_vol(perc, s1, s2)/2)
      hh     = m.floor(segons/3600)
      mm     = m.floor(segons/60)%60
      ss     = segons%60
      hh_f   = str(hh) if hh>=10 else "0"+str(hh) #format string
      mm_f   = str(mm) if mm>=10 else "0"+str(mm) #format string
      ss_f   = str(ss) if ss>=10 else "0"+str(ss) #format string
      comb   = round(self.combustible(perc,s1,s2))
      prod   = self.productivitat(perc,s1,s2)
      print(
        "Velocitat",(str(perc) if perc==100 else " "+str(perc))+"%:",hh_f+":"+mm_f+':'+ss_f,
        "| Fuel:",comb,
        "| Prod:",prod)
    print()
    return prod

#classes que hereden de naus
class Sondes(Naus):
  def __init__(self, numero):
    Naus.__init__(self, numero, 5, 100000000, 0.8, Cost(0,1000,0) )
class NausPC(Naus):
  def __init__(self, numero):
    Naus.__init__(self, numero, 5000, 5000, 8, Cost(2000,2000,0) )
class CazaL(Naus):
  def __init__(self, numero):
    Naus.__init__(self, numero, 50, 12500, 16, Cost(3000,1000,0) )

#calcular distancia entre 2 sistemes s1 s2
def distancia(s1,s2):
  return 2700+95*abs(s1-s2)

#---------------------------------------------------------

#simula flotes
flotes=[
  Sondes(50),
  NausPC(10),
  CazaL(10),
];
for flota in flotes: flota.viatge(s1,s2) 