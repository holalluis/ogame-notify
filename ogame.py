
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
    return 3*self.deuterio+2*self.cristal+1*self.metal

#classe nau
class Nau:
  def __init__(self, carrega, velocitat, consum, cost):
    self.carrega   = int(carrega)   #carrega que pot portar
    self.velocitat = int(velocitat) #velocitat base
    self.consum    = consum         #consum fuel
    self.cost      = cost           #cost (objecte)

#classe coordenades
class Lloc:
  def __init__(self, gal,sis,pla):
    self.gal = gal #galaxia
    self.sis = sis #sistema
    self.pla = pla #planeta
  def distancia(self,lloc):
    #mateixa galaixa, mateix sistema
    #TODO
    #mateixa galaxia, diferent sistema
    #TODO
    #diferent galaxia
    #TODO
    return 0
