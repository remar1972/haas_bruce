import math

def calc_cirle(diameter):
    """
    This function calculates the radius of a circle

    params:
    diameter
    """
    radius = diameter / 2
    oppervlakte_cirkel = math.pow(radius, 2) * math.pi
    return round(oppervlakte_cirkel, 3)

def calc_inhoud(lengte, breedte, hoogte):
    '''
    Met deze functie kun je de inhoud bepalen

    params:
    * lengte (float/int)
    * breedte (float/int)
    * hoogte (float/int)
    '''

    inhoud = lengte * breedte * hoogte

    return inhoud