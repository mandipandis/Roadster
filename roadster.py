import numpy as np
from scipy import interpolate

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

#funk. i integralen
def myFunc(x, route):
    return 1/velocity(x,route)

def trapets(func, x0, xn, n, route): #x0- startvärde, xn-slutvärde, n-delintervaller
    h = (xn - x0) / n
    integration = func(x0, route) + func(xn, route)
    for i in range(1, n):
        k = x0 + i * h
        integration += 2 * func(k, route)
    integration *= h / 2
    
    return integration


### PART 2A ###
def time_to_destination(x, route, n):
    return trapets(myFunc, 0, x, n, route)

route_anna = 'speed_anna.npz'
route_elsa = 'speed_elsa.npz'
n_values = [10, 50, 100, 500, 1000, 5000]

distance_anna, _ = load_route(route_anna)
distance_elsa, _ = load_route(route_elsa)
x_max_anna = max(distance_anna)
x_max_elsa = max(distance_elsa)

print("Restid i timmar för olika n-värden:")
for n in n_values:
    time_anna = time_to_destination(x_max_anna, route_anna, n)
    time_elsa = time_to_destination(x_max_elsa, route_elsa, n)
    print(f"n = {n}: Anna = {time_anna:.2f} h , Elsa = {time_elsa:.2f} h")


### PART 2B ###
def c(v):
    return 1 / v

def myOtherFunc(x, route):
    return c(velocity(x,route))

def total_consumption(x, route, n=1000):
    distance_km, _ = load_route(route)
    return trapets(myOtherFunc, 0, max(distance_km), n, route)

### PART 3A ###
def distance(T, route): 
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    raise NotImplementedError('distance not implemented yet!')

### PART 3B ###
def reach(C, route):
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    raise NotImplementedError('reach not implemented yet!')