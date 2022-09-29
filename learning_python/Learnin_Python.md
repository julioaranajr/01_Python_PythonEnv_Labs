# Learning Python

### Prepare pyenv

```sh
PYTHON_VERSION="3.10.5"

brew install pyenv
pyenv install $PYTHON_VERSION
pyenv global $PYTHON_VERSION
```

Open your `.zshrc` file and add the lines below at the end of the file.

```sh
code ~/.zshrc
```

**or**, use `vi`

```sh
vi ~/.zshrc
```

Copy and paste the following lines:

```
# Python - pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi
```

You should now close your terminal `exit` and re-open it.

Check python and pip

```sh
which python
which pip
```

## Some Utilities of pyenv

List of existing version installed on your mac:
```sh
pyenv versions
```

Set a new version of python on your mac:
```sh
pyenv global $PYTHON_VERSION
```

### Your First Python Program

Create a new file

```sh
vi hello.py
```

Edit your file with

```py
print("Hello World")
```

Run your script with

```sh
python hello.py
```

### Variables

```py
apples = 20             # type integer
price = 19.95           # type float
is_fruit = True         # type boolean
first_name = "Ethan"    # type String
print(apples)
print(price)
```

### Receiving Input

```py
apples = input("How many apples do you have ?")

print("You have " + apples + " apples!")
```

### Type Conversion

```py
date = input("Enter the year you were born? ")
# input will return a string
age = 2021 - int(date)  # convert the variable to an integer before doing the arithmetic

print(age)
```

### Strings

```py
planet_name = 'jupiter'

print(planet_name.upper()) # Only returns a new string
print(planet_name)

print(planet_name.find('t')) # returns the index of the character

# print(planet_name.replace('x', 9))  # does not exists, nothing happens
print(planet_name.replace('t', "T"))  # returns a new string
print(planet_name)

# Another way to check if string exists
print("ter" in planet_name)
```

### Arithmetic Operators

```py
# classics: +, -, *, /
print(10 / 3)

print(10 // 3)

# Try finding the differences between / and //

# Modulus
print(10 % 3)

# Exponent
print(10 ** 3)

# Increment with augmented assignment operator
x = 10
x += 7      # It's the same as x = x + 7
```

### Operator Precedence

```py
# Precedence is the same as in Maths
x = 10 + 3 * 2
print(x)

# Python can also use parentheses
x = (10 + 3) * 2
print(x)
```

### Comparison Operators

```py
x = 5 > 8  # creates a boolean value
print(x)

# Also have <, >=, <= or == (equality)
# Can also have not equal to using !

x = 5 != 8  # 5 is not equal to 8
print(x)
```

### Logical Operators

```py
# It can also be combined using 'and'/'or'
Mercury = 1
Venus = 2
Earth = 3
print(Venus > Mercury and Venus < Earth)  # and == both condition needs to be True

print(Venus > Mercury or Mercury > Earth)  # or == at least one condition needs to be True

# You can also use the not operator
print(Venus > Earth)   # returns False
print(not Venus > Earth) # returns True
```

### If Statements

```py
temperature = 25

# Python only uses indentation
if temperature > 30:
    print("It's too hot for me")   # note on the quotes
    print("Drink more water")
elif temperature > 20:
    print("It's alright")
elif temperature > 10:
    print("It's a bit cold")
else:
    print ("It's freezing")
print("Done")
```

### Exercise

- Knowing that 5 apples equals to 1 kg:
- Input the amount of apples
- Ask if weight needs to be in (k)kg or (l)lbs
- Calculate the weight of all apples

### Example Solution

```py
apple_weight = 1 / 5
apples = input("Amount of apples: ")
unit = input("(K)g or (L)bs: ")

if (unit.upper() == "K"):
    total = apple_weight * float(apples)
    print("Weight in Kgs: " + str(total))
elif(unit.upper() == "L"):
    total = (apple_weight * 0.45) * float(apples)
    print("Weight in Lbs: " + str(total))
else:
    print("Please specify (K)g or (L)bs only")
```

## Dictionaries

```py
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
```

## Loop through dictionaries

```py
distance_from_sun = {
    "Mercury": 0.4,
    "Venus": 0.7,
    "Earth": 1,
    "Mars": 1.5
}

# iterate through the keys
for planet in distance_from_sun:
    print(planet + " --> " + str(distance_from_sun[planet]))

# iterate through the item with key, value pair
for planet, distance in distance_from_sun.items():
    print(planet + " --> " + str(distance))
```

Working with Functions

```py
from datetime import datetime

def calculate_age(date):
    age = datetime.now().year - int(date)
    print(age)
    return age

born_year = input("Enter the year you were born? ")

print(calculate_age(born_year))
```
Another Example:
```py
def check_numbers(a, b):
    if a > b:
        return a
    else:
        return b

proceed = "y"

while(proceed == "y"):
    number_1 = int(input("Please provide your first number: "))
    number_2 = int(input("Please provide your second number:"))

    result = check_numbers(number_1, number_2)

    print(result)
    proceed = input("Continue: y or n: ")
```