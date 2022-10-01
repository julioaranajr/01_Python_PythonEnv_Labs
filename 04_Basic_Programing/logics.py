# example of print logical ops
a = 1
b = 2
c = 3

# AND 
print(a > c  and b < c)
# false or true 

# OR
print( a > b or c < b )
#false or true

# It can also be combined using 'and'/'or'
Mercury = 1
Venus = 2
Earth = 3
print(Venus > Mercury and Venus < Earth)  # and == both condition needs to be True

print(Venus > Mercury or Mercury > Earth)  # or == at least one condition needs to be True

# You can also use the not operator
print(Venus > Earth)   # returns False
print(not Venus > Earth) # returns True