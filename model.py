import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Global vars
solar_constant = 1368 # W/m^2, averaged over a year

class System:
    def __init__(self, long, lat) -> None:
        self.long = long
        self.lat = lat
    
    def get_angle(self) -> int:
        self.angle = self.long

    def show(self) -> None:
        print ('Long: ' + str(self.long))
        print ('Lat: ' + str(self.lat))
        print ('Angle: ' + str(self.angle))
        #print ('Test: ' + str(self.test))

energy_model = System(2, 34)
energy_model.get_angle()

energy_model.show()