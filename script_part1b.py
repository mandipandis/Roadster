import numpy as np
import matplotlib.pyplot as plt
import roadster
from roadster import velocity 

#distance_km, speed_kmph = roadster.load_route('speed_elsa.npz')
#plt.plot(distance_km, speed_kmph, "ro")
distance_km, speed_kmph = roadster.load_route('speed_anna.npz')
plt.plot(distance_km,speed_kmph, "bo")

x_fine = np.linspace(min(distance_km), max(distance_km), 1000)
v_interpolated = [velocity(x, 'speed_anna') for x in x_fine] #från gpt- den gör en lista typ men måste försöka fatta
plt.plot(x_fine, v_interpolated, label='Interpolerad funktion', color='green')

plt.xlabel('Sträcka [km]')
plt.ylabel('Hastighet [km/h]')
plt.legend()
plt.show()