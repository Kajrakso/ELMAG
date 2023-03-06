import numpy as np
# Oppgave 11

# a)
d = 0.200e-2       # m, diameter
I = 1.00           # A, strøm
rho = 8.92*100**3  # g cm^-3, massetetthet
Mm = 63.5          # g mol^-1, molvekt kobber
NA = 6.022e23      # mol^-1,  Avogrado
e = 1.602e-19      # C, elementærladning

n = rho/Mm*NA
print(f'{n=:.2e}')
v_d = (4*I*Mm)/(e*np.pi*d**2*rho*NA)    # drift velocity

print("a)")
print(f'{v_d=:.2e}')


# b)
L = 10.0            # m, lengde
rho = 1.72e-8       # ohm m, kopperresistivitet


J = 4*I/(np.pi*d**2)        # A m^-2, strømningstetthet
R = 4*rho*L/(np.pi*d**2)    # ohm, resistans
E = rho*J           # V m^-1, elektrisk felt 

print("\nb)")
print(f'{J=:.2e}')
print(f'{R=:.2e}')
print(f'{E=:.2e}')

# Oppgave 13
x1 = 264/67
x2 = -123/67
 
x3 = -276/67
 
x4 = 111/67
 
x5 = 12/67

x = [x1,x2,x3,x4,x5]

for i, xi in enumerate(x):
    print(f'x_{i+1} = {xi:.2f}')


# Oppgave 13 b)
R = 100
C = 10e-6
tau = R*C
t = -tau*np.log(0.001)
print(f'{t=:.2e}')
