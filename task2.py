import math
import scipy.constants as constants

#Write a program to explore the properties of a few elementary Particles.
class Particle: #le classi sempre in MAIUSC
    #def del costruttore
    def __init__(self, mass, charge =0, name = None, momentum =0):
        self.mass = mass #in Mev
        self.charge = charge #in unità di e
        self.name = name #nome 
        self.momentum = momentum #impulso in MeV/c

    def energy(self):
        return math.sqrt(self.momentum**2 + (self.mass*constants.c)**2)*constants.c #MeV
    
    def velocity(self):
        return (self.momentum*constants.c**2)/ self.energy()

class Electron(Particle):
    def __init__(self , momentum = 0): #perchè il momento deve essere =0?
        Particle.__init__(self, 0.511, 'e-', 'elettrone', momentum)

class Proton(Particle):
    def __init__(self, momentum = 0):
        Particle.__init__(self, 981, 'e+','protone', momentum)

el = Electron(momentum= 10)
pt = Proton(momentum = 10)
print("L'energia del  {} è {}. La sua velocità {}".format(el.name, el.energy(), el.velocity()))
print("L'energia del  {} è {}. La sua velocità {}".format(pt.name, pt.energy(),pt.velocity()))


    

