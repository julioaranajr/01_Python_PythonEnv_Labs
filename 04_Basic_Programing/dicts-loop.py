distance_from_sun = {
    "Mercury": 0.4,
    "Venus": 0.7,
    "Earth": 1,
    "Mars": 1.5
}

for planet in distance_from_sun:
    print(planet + " --> " + str(distance_from_sun[planet]))

for planet, distance in distance_from_sun.items():
    print(planet + " --> " + str(distance))
