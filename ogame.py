
#classe cost
class Cost:
  def __init__(self, metal, cristal, deuterio):
    self.metal    = metal
    self.cristal  = cristal
    self.deuterio = deuterio
  def __str__(self):
    return "[%d,%d,%d]" % (self.metal, self.cristal, self.deuterio)

#classe nau
class Nau:
  def __init__(self, nom, carrega, velocitat, consum, cost):
    self.carrega   = int(carrega)   #carrega que pot portar
    self.velocitat = int(velocitat) #velocitat base
    self.consum    = consum         #consum fuel
    self.cost      = cost           #cost (objecte)
