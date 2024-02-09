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





"""big pendel coordinate assignment"""
ys_B =np.array([y_berechnung_big_pendel(t*dt) for t in range(262,438)])
xs_B = np.array([i for i in range(0,176)])

"""big pendel coordinate assignment 2"""
ys_B2 =np.array([y_berechnung_big_pendel(t*dt) for t in range(262,438)])
xs_B2 = np.array([i for i in range(278,454)])

"""big pendel coordinate assignment 3"""
ys_B3 =np.array([y_berechnung_big_pendel(t*dt) for t in range(262,438)])
xs_B3 = np.array([i for i in range(556,732)])




"""small pendel coordinate assignment"""
ys_S = np.array([y_berechnung_small_pendel(t*dt) for t in range(0,102)])
xs_S = np.array([i for i in range(175,277)])

"""small pendel coordinate assignment2"""
ys_S2 = np.array([y_berechnung_small_pendel(t*dt) for t in range(0,102)])
xs_S2 = np.array([i for i in range(454,556)])

"""small pendel coordinate assignment3"""
ys_S3 = np.array([y_berechnung_small_pendel(t*dt) for t in range(0,102)])
xs_S3 = np.array([i for i in range(732,834)])



"""creating subplots"""
fig, axs = plt.subplots(3)
fig.suptitle('Pendel calculations')

"""Plot based on Function"""
axs[0].plot(xs,ys)

"""Plots seperated based on long Pendel and short Pendel"""
axs[1].plot(xs_BP, ys_BP) #Long Pendel
axs[1].plot(xs_SP, ys_SP) #Short Pendel


"""Plot combination of the combination of single waves"""
axs[2].plot(xs_B,ys_B) #First positive Curve
axs[2].plot(xs_S, ys_S) #First negative Curve
axs[2].plot(xs_B2,ys_B2) #Second positive Curve
axs[2].plot(xs_S2, ys_S2) #Second negative Curve
axs[2].plot(xs_B3,ys_B3) #Third positive Curve
axs[2].plot(xs_S3, ys_S3) #Third negative Curve


"""show plots"""
plt.show()
