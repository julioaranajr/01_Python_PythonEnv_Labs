# Write a program that asks for a temperature in degrees Celsius 
# and writes that temperature in degrees Fahrenheit. 
# Remember that the relationship between degrees Celsius (C) and degrees Fahrenheit (F) 
# is as follows: F = 1.8 * C + 32

def main():
    print("App to Convert Degrees -CELSIUS- TO -FAHRENHEIT-")
    celsius = float(input("Type a temperature in degrees Celsius: "))

    fahrenheit = 1.8 * celsius + 32

    print(f"{celsius} ºC son {fahrenheit} ºF")


if __name__ == "__main__":
    main()