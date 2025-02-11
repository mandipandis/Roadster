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
def f(x, route):
    return 1/velocity(x,route)

def trapets(x0, xn, n, route): #x0- startvärde, xn-slutvärde, n-delintervaller
    h = (xn - x0) / n
    integration = f(x0, route) + f(xn, route)
    for i in range(1, n):
        k = x0 + i * h
        integration += 2 * f(k, route)
    integration *= h / 2
    
    return integration

### PART 2A ###
def time_to_destination(route, n = 1000):
    distance_km, speed_kmph = load_route(route)
    return trapets(0, max(distance_km), n, route)

route_anna = 'speed_anna.npz'
route_elsa = 'speed_elsa.npz'
n_values = [10, 50, 100, 500, 1000, 5000]

print("Restid i timmar för olika n-värden:")
for n in n_values:
    time_anna = time_to_destination(route_anna, n)
    time_elsa = time_to_destination(route_elsa, n)
    print(f"n={n}: Anna = {time_anna:.2f} h, Elsa = {time_elsa:.2f} h")


### PART 2B ###
def total_consumption(x, route, n):
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    raise NotImplementedError('total_consumption not implemented yet!')

### PART 3A ###
def distance(T, route): 
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    raise NotImplementedError('distance not implemented yet!')

### PART 3B ###
def reach(C, route):
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    raise NotImplementedError('reach not implemented yet!')