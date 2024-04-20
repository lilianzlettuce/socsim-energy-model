import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

# Global vars
solar_constant = 1368 # W/m^2, averaged over a year
solar_constant_avg = solar_constant / 4

class System:
    def __init__(
            self, 
            long, 
            lat,
            albedo,
            zenith,
            azimuth,
            elevation) -> None:
        self.long = long
        self.lat = lat
        self.albedo = albedo

    def __init__(
            self, 
            long, 
            lat,
            albedo) -> None:
        self.long = long
        self.lat = lat
        self.albedo = albedo
        self.zenith = lat
        self.azimuth = None

    def calc_air_mass(self) -> float:
        self.air_mass = 1 / math.cos(math.radians(self.zenith))
        return self.air_mass

    def calc_direct_beam(self) -> float:
        self.direct_beam = solar_constant_avg 
        self.direct_beam *= math.cos(math.radians(self.zenith))
        self.direct_beam *= (1 - self.albedo)
        return self.direct_beam
    
    def calc_diffuse(self) -> float:
        self.diffuse = 10
        return self.diffuse

    def calc_total_insolation(self) -> float:
        self.total_insolation = self.calc_direct_beam() + self.calc_diffuse()
        return self.total_insolation

    def show(self) -> None:
        print('Long: ' + str(self.long))
        print('Lat: ' + str(self.lat))
        print('Insolation: ' + str(self.total_insolation))
        print()

for i in range(0, 11):
    lat = 90 / 10 * i
    energy_model = System(2, lat, 0.3)
    energy_model.calc_total_insolation()
    energy_model.show()

energy_model = System(2, 34, 0.3)
energy_model.calc_total_insolation()
energy_model.show()

energy_model = System(-90, -78, 0.3)
energy_model.calc_total_insolation()
energy_model.show()

energy_model = System(0, 0, 0.3)
energy_model.calc_total_insolation()
energy_model.show()

energy_model = System(45, 45, 0.3)
energy_model.calc_total_insolation()
energy_model.show()