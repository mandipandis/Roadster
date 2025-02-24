import numpy as np
from scipy import interpolate
from scipy.integrate import quad

def load_route(route):
    """ 
    Get speed data from route .npz-file. Example usage:

      distance_km, speed_kmph = load_route('speed_anna.npz')
    
    The route file should contain two arrays, distance_km and 
    speed_kmph, of equal length with position (in km) and speed 
    (in km/h) along route. Those two arrays are returned by this 
    convenience function.
    """
    # Read data from npz file
    if not route.endswith('.npz'):
        route = f'{route}.npz' 
    data = np.load(route)
    distance_km = data['distance_km']
    speed_kmph = data['speed_kmph']    
    return distance_km, speed_kmph

def save_route(route, distance_km, speed_kmph):
    """ 
    Write speed data to route file. Example usage:

      save_route('speed_olof.npz', distance_km, speed_kmph)
    
    Parameters have same meaning as for load_route
    """ 
    np.savez(route, distance_km=distance_km, speed_kmph=speed_kmph)

### PART 1A ###
def consumption(v):
    c = 546.8*v**-1 + 50.31 + 0.2584*v + 0.008210*v**2
    return c

speed_kmph = np.linspace(1., 200., 1000)
consumption_Whpkm = consumption(speed_kmph)

print(consumption_Whpkm)

### PART 1B ###
def velocity(x, route):
    # ALREADY IMPLEMENTED!
    """
    Interpolates data in given route file, and evaluates the function
    in x
    """
    # Load data
    distance_km, speed_kmph = load_route(route)
    # Check input ok?
    assert np.all(x>=0), 'x must be non-negative'
    assert np.all(x<=distance_km[-1]), 'x must be smaller than route length'
    # Interpolate
    v = interpolate.pchip_interpolate(distance_km, speed_kmph,x)
    return v

### PART 2A ###
#funk. i integralen
def myFunc(x, route):
    return 1/velocity(x,route)

def trapets(func, x0, xn, n, route):
    h = (xn - x0) / n  # Steglängd
    x_values = np.linspace(x0 + h, xn - h, n - 1)  
    f_values = func(x_values, route)
    integration = (func(x0, route) + func(xn, route) + 2 * np.sum(f_values)) * (h / 2)
    
    return integration

def time_to_destination(x, route, n):
    return trapets(myFunc, 0, x, n, route)

route_anna = 'speed_anna.npz'
route_elsa = 'speed_elsa.npz'
distance_anna, _ = load_route(route_anna)
distance_elsa, _ = load_route(route_elsa)
x_max_anna = max(distance_anna)
x_max_elsa = max(distance_elsa)
n_values = [10, 50, 100, 500, 1000, 5000]
print("Restid i timmar för olika n-värden:")
for n in n_values:
    time_anna = time_to_destination(x_max_anna, route_anna, n)
    time_elsa = time_to_destination(x_max_elsa, route_elsa, n)
    print(f"n = {n}: Anna = {time_anna:.2f} h , Elsa = {time_elsa:.2f} h")

### PART 2B ###
def consumptionFunc(s, route):
    v_s = velocity(s, route)  # Hastighet vid sträcka s
    return consumption(v_s)

def total_consumption(x, route, n=1000):
    distance_km, _ = load_route(route)
    return trapets(consumptionFunc, 0, x, n, route)

print("Elförbrukning i Wh för olika n-värden:")
for n in n_values:
    anna = total_consumption(x_max_anna, 'speed_anna.npz', n)
    elsa = total_consumption(x_max_elsa, 'speed_elsa.npz', n)
    print(f"n = {n}: Anna = {anna:.2f} Wh, Elsa = {elsa:.2f} Wh")

### PART 3A ###
def distance(T, route): 
    distance_km, _ = load_route(route)
    v_mean = np.mean(velocity(distance_km, route))
    x_n = v_mean * T  #Startvärde
    for i in range(1000):
        f_x = time_to_destination(x_n, route, 10000000) - T
        df_x = myFunc(x_n, route)
        x_next = x_n - f_x / df_x #Newton

        #Kolla om litet värde
        if np.abs(x_next - x_n) < 10e-10:
            return x_next
        
        x_n = x_next

    return None 

T = 0.5 
anna = distance(T, 'speed_anna.npz')
elsa = distance(T, 'speed_elsa.npz')

print(f"Sträcka efter {T} timmar:")
print(f"Anna: {anna:} km")
print(f"Elsa: {elsa:} km")

### PART 3B ###
def reach(C, route):
    distance_km, _ = load_route(route)

    #Startvärde
    avg_consumption = np.mean(consumptionFunc(distance_km, route))  
    x = min(C / avg_consumption, max(distance_km))    

    for _ in range(1000):
        f_x = total_consumption(x, route, 1000000) - C
        df_x = consumptionFunc(x, route)
        x_next = x - f_x / df_x #Newton
        x_next = max(0, min(x_next, max(distance_km)))
        if np.abs(x_next - x) < 10e-4:
            return x_next
        
        x = x_next 
    return max(distance_km)

C = 10000
anna = reach(C, 'speed_anna.npz')
elsa = reach(C, 'speed_elsa.npz')

print(f"Sträcka med {C} Wh:")
print(f"Anna: {anna:} km")
print(f"Elsa: {elsa:} km")
