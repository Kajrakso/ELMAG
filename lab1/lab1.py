import matplotlib.pyplot as plt
import numpy as np

N = 330 # [] antall viklinger
I0 = 0.9 # [A] strøm
mu_0 = 4.0*np.pi*1e-7 # [H/m] permeabilitet i tomt rom
R = 0.07 # [m] radius
x0 = 0.000 # [m] sentrum av spolen

a_range = np.array([R/2, R, 2*R])       # liste med a-verdier

def png_plot(xb, Bb, xe, Be, title, a=0):
    # Plot resultatene
    plt.plot(xb, Bb, label='Beregnet')
    plt.plot(xe, Be, '.', label='Måledata')
    # plt.plot(xe, Be - stoy_avg, '.', label='Måledata - støy')
    plt.xlabel('Avstand fra senter av spolen (m)')
    plt.ylabel('Magnetfelt (Gauss)')
    plt.legend()
    plt.title(title)
    plt.savefig(f'{title}.png')
    plt.show()
    

def plot_mag_field(B_field_function, x_range: np.ndarray, title, a_range: list = []):
    if len(a_range) == 0:
        plt.plot(x_range, B_field_function(x_range))
    else:
        for a in a_range:
            plt.plot(x_range, B_field_function(x_range, a), label=f"a = {a}")
            plt.legend()

    plt.title(title)
    plt.ylabel("B [gauss]")
    plt.xlabel("Avstand fra senter av spolene [m]")
    plt.show()


def B_felt_kort_spole(x):
    prefaktor = N*mu_0*I0/(2*R)
    return prefaktor*(1.0 + (x/R)**2)**(-1.5)


# FUNCTIONS
def B_field_short(x):
    """Kort spole. Returnerer i T"""
    return (mu_0 * N*I0/(2*R) * (1+x**2/R**2)**(-3/2) )

def B_field_Helmholtz(x, a):
    return B_field_short(x-a/2) + B_field_short(x+a/2)

def B_field_Anti_Helmholtz(x, a):
    return B_field_short(x-a/2) - B_field_short(x+a/2)


def run3():
    filnavn = 'lab1_data.csv'
    title = "run3"
    cols = (6, 7)
    max_row = 304

    data = np.loadtxt(filnavn, delimiter=';', skiprows=1, max_rows=max_row, usecols=cols)
    xe = data[:, 0] - x0 # posisjon, sentrert rundt x0
    Be = 10**6*data[:, 1] # måledata
    a = a_range[2] 
    
    # Beregn B-feltet
    xb = np.linspace(np.min(xe), np.max(xe), 100) # flere datapunkter
    
    # Bb = B_felt_kort_spole(xb)*1e4 # beregnet B-felt (Gauss)
    Bb = B_field_Helmholtz(xb, a)*1e4 # beregnet B-felt (Gauss)
    
    return filnavn, xe, Be, xb, Bb, a, title

def run4():
    filnavn = 'lab1_data.csv'
    title = "run4"
    cols = (10, 11)
    max_row = 304

    data = np.loadtxt(filnavn, delimiter=';', skiprows=1, max_rows=max_row, usecols=cols)
    xe = data[:, 0] - x0 # posisjon, sentrert rundt x0
    Be = 10**6*data[:, 1] # måledata
    a = a_range[2] 
    
    # Beregn B-feltet
    xb = np.linspace(np.min(xe), np.max(xe), 100) # flere datapunkter
    
    # Bb = B_felt_kort_spole(xb)*1e4 # beregnet B-felt (Gauss)
    Bb = -B_field_Anti_Helmholtz(xb, a)*1e4 # beregnet B-felt (Gauss)
    
    return filnavn, xe, Be, xb, Bb, a, title

def run5():
    filnavn = 'lab1_data.csv'
    title = "run5"
    cols = (14, 15)
    max_row = 304

    data = np.loadtxt(filnavn, delimiter=';', skiprows=1, max_rows=max_row, usecols=cols)
    xe = data[:, 0] - x0 # posisjon, sentrert rundt x0
    Be = 10**6*data[:, 1] # måledata
    a = a_range[1] 

    # Beregn B-feltet
    xb = np.linspace(np.min(xe), np.max(xe), 100) # flere datapunkter
    
    # Bb = B_felt_kort_spole(xb)*1e4 # beregnet B-felt (Gauss)
    Bb = B_field_Helmholtz(xb, a)*1e4 # beregnet B-felt (Gauss)
    
    return filnavn, xe, Be, xb, Bb, a, title

def run6():
    filnavn = 'lab1_data.csv'
    title = "run6"
    cols = (18, 19)
    max_row = 302

    data = np.loadtxt(filnavn, delimiter=';', skiprows=1, max_rows=max_row, usecols=cols)
    xe = data[:, 0] - x0 # posisjon, sentrert rundt x0
    Be = 10**6*data[:, 1] # måledata
    a = a_range[1] 

    # Beregn B-feltet
    xb = np.linspace(np.min(xe), np.max(xe), 100) # flere datapunkter
    
    # Bb = B_felt_kort_spole(xb)*1e4 # beregnet B-felt (Gauss)
    Bb = -B_field_Anti_Helmholtz(xb, a)*1e4 # beregnet B-felt (Gauss)
    
    return filnavn, xe, Be, xb, Bb, a, title

def run7():
    filnavn = 'lab1_data.csv'
    title = "run7"
    cols = (22, 23)

    data = np.loadtxt(filnavn, delimiter=';', skiprows=1, max_rows=357, usecols=cols)
    xe = data[:, 0] - x0 # posisjon, sentrert rundt x0
    Be = 10**6*data[:, 1] # måledata
    a = a_range[0] 

    # Beregn B-feltet
    xb = np.linspace(np.min(xe), np.max(xe), 100) # flere datapunkter
    
    # Bb = B_felt_kort_spole(xb)*1e4 # beregnet B-felt (Gauss)
    Bb = B_field_Helmholtz(xb, a)*1e4 # beregnet B-felt (Gauss)
    
    return filnavn, xe, Be, xb, Bb, a, title

def run8():
    filnavn = 'lab1_data.csv'
    title = "run8"
    cols = (26, 27)
    max_row = 357

    data = np.loadtxt(filnavn, delimiter=';', skiprows=1, max_rows=max_row, usecols=cols)
    xe = data[:, 0] - x0 # posisjon, sentrert rundt x0
    Be = 10**6*data[:, 1] # måledata
    a = a_range[0] 

    # Beregn B-feltet
    xb = np.linspace(np.min(xe), np.max(xe), 100) # flere datapunkter
    
    # Bb = B_felt_kort_spole(xb)*1e4 # beregnet B-felt (Gauss)
    Bb = -B_field_Anti_Helmholtz(xb, a)*1e4 # beregnet B-felt (Gauss)
    
    return filnavn, xe, Be, xb, Bb, a, title


def main():
    filnavn, xe,Be, xb, Bb,a, title = run8()

    # STØY
    background_stoy = 10**6*np.loadtxt('testsampling spole i ro.csv', delimiter=';', skiprows=1, usecols=(3))
    stoy_avg = np.mean(background_stoy)

    png_plot(xb,Bb,xe,Be,title,a)


if (__name__ == '__main__'):
    main()
    