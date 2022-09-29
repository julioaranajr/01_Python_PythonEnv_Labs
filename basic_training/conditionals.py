# Conditional for temperature

temperature = int(input("What's the temperature ?"))

if temperature > 35:
    print("It's too hot")
elif temperature > 20:
    print("It's perfect")
elif temperature > 15:
    print("It's a bit cold")
else:
    print("It's freezing")