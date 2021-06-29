import math

def calc_cirle(diameter):
    """
    This function calculates the circle

    params:
    diameter
    """
    radius = diameter / 2
    oppervlakte_cirkel = math.pow(radius, 2) * math.pi
    return round(oppervlakte_cirkel, 3)