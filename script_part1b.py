import matplotlib.pyplot as plt
import roadster
#help (roadster . load_route )


distance_km, speed_kmph = roadster.load_route('speed_anna.npz')

v = roadster.velocity(0,'speed_anna')

plt.plot(distance_km, speed_kmph, "ro")
distance_km, speed_kmph = roadster.load_route('speed_elsa.npz')
plt.plot(distance_km,speed_kmph, "bo")

plt.show()
