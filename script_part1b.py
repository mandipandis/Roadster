<<<<<<< HEAD
import matplotlib.pyplot as plt
import roadster
#help (roadster . load_route )



distance_km, speed_kmph = roadster.load_route('speed_anna.npz')

v = roadster.velocity(0,'speed_anna')

plt.plot(distance_km, speed_kmph, "ro")
distance_km, speed_kmph = roadster.load_route('speed_elsa.npz')
plt.plot(distance_km,speed_kmph, "bo")

plt.show()
=======
import matplotlib.pyplot as plt
import roadster
#help (roadster . load_route )


distance_km, speed_kmph = roadster.load_route('speed_anna.npz')

v = roadster.velocity(0,'speed_anna')

plt.plot(distance_km, speed_kmph, "ro")
distance_km, speed_kmph = roadster.load_route('speed_elsa.npz')
plt.plot(distance_km,speed_kmph, "bo")

plt.show()
>>>>>>> 6f37f59dfee53125b2790495168c201354c9b800
