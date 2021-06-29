from custom_functions.calc_funs import calc_cirle, calc_inhoud

# params voor de cirkel
diameter = float(input("Insert diameter:\n"))


# params voor de inhoud
lengte = float(input('Geef lengte\n'))
breedte = float(input('Geef breedte\n'))
hoogte = float(input('Geef hoogte\n'))

result_cirkel = calc_cirle(diameter)

result_inhoud = calc_inhoud(lengte, breedte, hoogte)

print(f"cirkel is: {result_cirkel}, inhoud is: {result_inhoud}")