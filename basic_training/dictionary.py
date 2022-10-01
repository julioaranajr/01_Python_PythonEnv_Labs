distance_from_sun = {
    "Mercury": 0.4,
    "Venus": 0.7,
    "Earth": 1,
    "Mars": 1.5
}

my_dict = {
    "Mercury" : 
        { 
            "moons" : 0,
            "atmosphere": False 
        },
    "Venus" :
        { 
            "moons" : 0,
            "atmosphere": True
        },
    "Earth" :
        { 
            "moons" : 1,
            "atmosphere": True
        },
    "Mars" : 
        { 
            "moons" : 2,
            "atmosphere": True
        },
}


print(distance_from_sun["Mercury"])
print(distance_from_sun["Earth"])