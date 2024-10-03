import math

#Write a program to explore the properties of a few elementary Particles.
class Particle: #le classi sempre in MAIUSC
    #def del costruttore
    def __init__(self, mass, charge =0, name = None, momentum =0):
        self.mass = mass #in Mev
        self.charge = charge #in unità di e
        self.name = name #nome 
        self.momentum = momentum #impulso in MeV/c

    def energy(self):
        return math.sqrt(self.momentum**2 + self.mass**2)

class Electron(Particle):
    def __init__(self , momentum = 0): #perchè il momento deve essere =0?
        Particle.__init__(self, 0.511, 'e-', 'elettrone', momentum)


el = Electron(momentum= 10)
print("L'energia del  {} è {}".format(el.name, el.energy()))


    

