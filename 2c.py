import roadster
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

### Väljer att göra empirisk undersökning av noggranhetsordningen på integral 1 (fråga 2A) ###

# 1 Räknar ut integrationsfelet för en serie beräkningar där antalet delintervall n dubbleras successivt

#funk. i integralen
def myFunc(x, route):
    return 1/roadster.velocity(x,route)

#trapetsmetoden för att beräkna integral
def trapets(func, x0, xn, n, route):
    h = (xn - x0) / n  # Steglängd
    x_values = np.linspace(x0 + h, xn - h, n - 1)  
    f_values = func(x_values, route)
    integration = (func(x0, route) + func(xn, route) + 2 * np.sum(f_values)) * (h / 2)
    
    return integration

# n = antalet delintervall
n_start = 100
n_values = [n_start*2**i for i in range(16)]  #skapar en lista där n dubbleras
route_anna = 'speed_anna.npz'
distance_anna, _ = roadster.load_route(route_anna)
x_max_anna = max(distance_anna)

# använder värdet för det störst n (sista) som analytiska värde
# tar abs(analytiska värdet - integral_value) för att få feluppskattning
integral_values = [trapets(myFunc, 0, x_max_anna, n, 'speed_anna.npz') for n in n_values]  #integralvärdena
error_estimation = [abs(integral_values[-1] - i) for i in integral_values]      #feluppskattning/integrationsfel

for e, n in zip(error_estimation, n_values):
    print(f"n = {n}: feluppskattning = {e:.4f}")


# 2 Plottar integrationsfelet som funktion av antalet delintervall n (plotta i log-skala)

plt.loglog(n_values, error_estimation, label='feluppskattning', color='blue')

#hjälplinjer O(h) (kommer från ET(h2)/ET(h))
help_lines = np.linspace(min(n_values), max(n_values), 100)
plt.loglog(help_lines, 10/help_lines, '--', label='noggranhetsordning 1', color='red')

#hjälplinjer O(h^2)
help_lines = np.linspace(min(n_values), max(n_values), 100)
plt.loglog(help_lines, 100000/help_lines**2, '--', label='noggranhetsordning 2', color='green')



plt.xlabel('antal delintervall n')
plt.ylabel('feluppskattning')
plt.legend()
plt.show()


# 3 Stämmer den empiriskt bestämda noggrannhetsordningen med teorin för trapetsmetoden

# Teoretiska noggranhetsordningen för trapetsmetoden p = 2
# Empiriska = 2 (den passar kurvan bäst)
# Ja det stämmer
