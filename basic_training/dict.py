from turtle import distance

distance_from_sun = {
    # KEY = VALUE
    "Mercury": {
        "moons": 0,
        "atmosphere": False
    },
    "Venus": {
        "moons": 0,
        "atmosphere": True
    },
    "Earth": {
        "moons": 1,
        "atmosphere": True
    },
    "Mars": 1.5
}

print(distance_from_sun["Earth"]["atmosphere"])