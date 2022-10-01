temperature = int(input("What's the temperature ?"))

if temperature > 30:
    print("It's too hot for me")
elif temperature > 20:
    print("It's perfect, nice weather")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's freezing")
print("I stay at home, today")