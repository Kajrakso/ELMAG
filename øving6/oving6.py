import numpy as np
import scipy.constants

# Oppgave 9a
K = 10
d = 7.5e-9
V = 85e-3

print(f'Kapasitans per areal: {K*scipy.constants.epsilon_0/d*10**(-4):.2e} F/cm^2')
print(f'E-felt: {V/d:.2e}')


# Oppgave 10
K1 = 3.40
K2 = 1
d = 4.5e-3
l = 12e-2
V = 18

C = (K1+K2)*scipy.constants.epsilon_0*l**2/(4*d)

print(f'Kapasitans = {C:.2e} F')


U = 0.5*C*V**2
print(f"Energi U = {U:.2e} J")

# c)
U0 = 0.5*scipy.constants.epsilon_0*l**2*V**2/d

print(f'Energi - plexi: {U0:.2e} J')
