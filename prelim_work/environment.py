import thermo
import numpy as np

class environmentThermo:
    """
    should help with connecting to thermo API to get properties
    note from Sartaaj: more functions can be added if needed - that's why I think this is best as an "environment"
    """
    def __init__(self, mass_array, componentNames):
        """
        Takes mass_array = [m1, m2, ..., mN], where mN is mass of nth component in mixture
        componentNames -> list of strings of component names - example: ['methanol', 'ethanol', 'butanol', ...]
        """
        self.mass_array = mass_array
        self.componentNames = componentNames
        self.total_mass = np.sum(mass_array) #sums mass of pure components [m1, m2, ..., mN] -> returns real number R
        self.mass_frac = [x/self.total_mass for x in self.mass_array] #returns array of mass fractions of each component

    def thermophysicalProperties(self):
        """
        returns thermophysical properties [density, viscosity, thermal cond., heat capacity] of mixture object defined in __init__
        returned units: [kg/m3, Pa*s, W/mK, J/kgK]
        """
        m = thermo.Mixture(self.componentNames, ws = self.mass_frac)
        return [m.rho, m.mu, m.k, m.Cp]

    def FOM(self):
        """
        computes FOM(y); y = [rho, mu, k, Cp]
        FOM(y) = (k = 0 -> 3) Π(y_k ^ p_k), where p_k are the values in FOM array
        """
        fom_array = [0.2, -0.4, 0.2, 2]
        thermoProperties = self.thermophysicalProperties()

        return np.prod(np.power(thermoProperties[:4], fom_array[:4]))
