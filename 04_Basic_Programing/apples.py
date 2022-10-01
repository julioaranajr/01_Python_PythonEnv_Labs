# Knowing that 5 apples equals to 1 KG
# Input the amount of apples
# Ask if the weight needs to be in (k)KG or (l)lbs
# Calculate the weight of the apples

APPLES_PER_KG = 5
KG_PER_LB = 0.45359237

apples = int(input("enter number of apples: "))
unit = input("does the weight need to be in Kg (k) or lbs (l)? ")

if unit == "k":
    weight = apples / APPLES_PER_KG
    print(f"the weight of the apples is {weight} kg") 
elif unit == "l":
    weight = apples * APPLES_PER_KG * KG_PER_LB
    print(f"the weight of the apples is {weight} lbs") 
else:
    print("wrong input")