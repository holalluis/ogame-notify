#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
  productivitat atacs ogame
'''
import math as m

#variables globals
motor_c = 0   #motor combustión: augmenta velocitat PC i GC
motor_i = 0   #motor impulso: augmenta velocitat PC a partir del nivell 5
tec_hip = 0   #tecnologia hiperespacio: augmenta 5% càrrega

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
      self.carrega_real(),
      self.numero*self.carrega_real(),
      self.velocitat_real(),
      self.consum,
      self.cost,
      self.numero*self.cost.absolut()
    )

  def velocitat_real(self): return self.velocitat*(1+0.1*motor_c)
  def carrega_real(self):   return round(self.carrega*(1+0.05*tec_hip))

  #temps de vol entre 2 sistemes s1 s2
  def temps_de_vol(self,percent,s1,s2):
    vel = self.velocitat_real()
    dis = distancia(s1,s2)
    return 10+35e3/percent*m.sqrt(1e3*dis/vel)

  #consum combustible entre 2 sistemes s1 s2
  def combustible(self,percent,s1,s2):
    voltes = 1
    consum = self.consum
    n      = self.numero
    return 1+n*voltes*consum*distancia(s1,s2)/35e3*m.pow(percent/100+1,2)

  #productivitat: recursos per segon
  def productivitat(self,perc,s1,s2,boti):
    carrega = self.numero*self.carrega_real()     #carrega possible
    boti    = min(boti,carrega)                   #minim entre boti i carrega
    boti   -= round(self.combustible(perc,s1,s2)) #resta combustible
    segons  = self.temps_de_vol(perc,s1,s2)       #segons totals viatge
    return boti/segons #unitats/s

  #calcula productivitat viatge entre sistema s1 i s2
  def viatge(self,s1,s2,boti):
    boti=int(boti)
    print("[+] Viatge ",s1,"-->",s2,"| Distancia:",distancia(s1,s2),"| Botí:",boti)
    naus_suggerides = m.ceil(boti/self.carrega_real())

    if naus_suggerides != self.numero: print("Naus suggerides:",naus_suggerides)

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
      prod   = self.productivitat(perc,s1,s2,boti)
      print(
        "Velocitat",(str(perc) if perc==100 else " "+str(perc))+"%:",hh_f+":"+mm_f+':'+ss_f,
        "| Fuel:",comb,
        "| Prod:",prod)
    print()

    if(naus_suggerides!=self.numero):
      self.numero=naus_suggerides
      self.viatge(s1,s2,boti)

    return prod
#-------------------------------------------------------------

#classes pels tipus de naus
#-------------------------------------------------------------
class Sondes(Naus):
  def __init__(self,n):
    Naus.__init__(self,n,    5,  1e8, 0.8, Cost(   0,1000,0) )
#-------------------------------------------------------------
class NausPC(Naus):
  def __init__(self,n):
    Naus.__init__(self,n,  5e3,  1e4,   8, Cost(2000,2000,0) )
  def velocitat_real(self):
    return self.velocitat*(1+0.2*motor_i)
#-------------------------------------------------------------
class NausGC(Naus):
  def __init__(self,n):
    Naus.__init__(self,n, 25e3, 7500,  40, Cost(6000,6000,0) )
#-------------------------------------------------------------

#calcular distancia entre 2 sistemes s1 s2
def distancia(s1,s2):
  return 2700+95*abs(s1-s2)
