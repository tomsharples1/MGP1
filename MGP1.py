import math
import numpy as np

# Constants
p = 1.225  # Air density (kg/m^3)
Cd = 0.5  # Drag coefficient
A =  0.001 #frontal area (m^2)
Cl = 1.5  # Lift coefficient
phi = math.radians(30)  # Launch angle (converted to radians)
m = 0.8  # Mass of javelin (kg)
g = 9.80665  # Acceleration due to gravity (m/s^2)

def runge_kutta(f, v0, t0, t_end, h):

    t = t0
    v = v0
    t_values = [t0]
    v_values = [v0]

    while t < t_end:
        k1 = h * f(t, v)
        k2 = h * f(t + 0.5 * h, v + 0.5 * k1)
        k3 = h * f(t + 0.5 * h, v + 0.5 * k2)
        k4 = h * f(t + h, v + k3)

        v = v + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t = t + h

        t_values.append(t)
        v_values.append(v)
        
    distance = 0  
    for i in range(len(v_values)):
        distance += v_values[i] * t_values[i]


    return distance


# Define your differential equation function f(t, y)
def f_x(t, v_x):
    D = 0.5 * p * Cd * A 
    L = 0.5 * p * Cl * A 
    k=1
    return -D * math.cos(phi) * v_x**2 - L * math.sin(phi) * v_x - k*v_x

# Initial conditions
v0 = 30.0
t0 = 0
t_end = 3.3
h = 0.05
phi = math.radians(30)



p =1.225
Cd = 0.001
A= 0.5
Cl= 1.5
phi = math.radians(30)
k = 1
m = 0.8 
g = 9.80665

D = 0.5*p*Cd*A
L = 0.5*p*Cl*A

def f_y(t, v_y):
    D = 0.5 * p * Cd * A * v_y**2
    L = 0.5 * p * Cl * A * v_y**2
    return -D * math.sin(phi) + L * math.cos(phi) - m * g 


print(runge_kutta(f_y, 30*math.sin(phi), 0, 3.3, 0.01))
