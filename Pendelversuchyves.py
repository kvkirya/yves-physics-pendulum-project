import numpy as np
import matplotlib.pyplot as plt

"""Defining Variables"""
g = 9.81 #anziehungskraft
phi_0 =np.pi/4
r_1 = 0.3 #Länge Pendel 1
r_2 = 0.1 #Länge Pendel 2
t = 0 #Zeit
dt = 0.1 #delta Zeit
w1 = np.pi*np.sqrt(g/r_1) #berechnung für omega 1
w2 = np.pi*np.sqrt(g/r_2) #berechnung für omega 2
T = np.pi * (np.sqrt(r_1/g)+np.sqrt(r_2/g)) #gesamtperiode
T_1 = np.pi*np.sqrt(r_1/g) # erster Teil der gesammtperiode

y_max = r_1 * np.cos(phi_0) #Amplitude des ersten Pendels
y_max2 = r_2 * np.cos(phi_0) #Amplitude Pendel 2
dt = 0.001 #delta Zeit


"""Writing the Function to calculate y at timestamp t"""
def y_berechnung(t):
    """Function to calculate y at time t"""
    y = y_max * np.cos(w1*t)
    if y > 0:
        return y
    else:
        return y_max2 * np.cos(w2*t+np.pi/2)



"""Function for calculation of the big Pendel swinging alone"""
def y_berechnung_big_pendel(t):
    y = y_max*np.cos(w1*t)
    return y

"""Function for calculation of the small Pendel swinging alone"""
def y_berechnung_small_pendel(t):
    y = y_max2*np.cos(w2*t+np.pi/2)
    return y



"""function coordinate assignment"""
ys =np.array([y_berechnung(t*dt) for t in range(1000)])
xs = np.array([i for i in range(1000)])

"""big pendel coordinate assignment full pendel"""
ys_BP =np.array([y_berechnung_big_pendel(t*dt) for t in range(0,1000)])
xs_BP = np.array([i for i in range(0,1000)])

"""small pendel coordinate assignment full pendel"""
ys_SP = np.array([y_berechnung_small_pendel(t*dt) for t in range(0,1000)])
xs_SP = np.array([i for i in range(0,1000)])



"""Plot based on Function"""
plt.subplot(121)
plt.plot(xs,ys)
plt.xlabel("plot based on function")

"""Plots seperated based on long Pendel and short Pendel"""
plt.subplot(122)
plt.plot(xs_BP, ys_BP) #Long Pendel
plt.plot(xs_SP, ys_SP) #Short Pendel
plt.xlabel("Plot seperating both long and short Pendel swing")

"""show plots"""
plt.suptitle("Pendel calculations")
plt.show()
