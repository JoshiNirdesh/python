weight = int( input("Weight: "))
unit = input("K(Kg)or (L)Lbs")

if unit.lower()=='l':
    print("Weight in kg is ", str(weight/2.5))
elif unit.lower()=='k':
    print("Weight in lbs is ", str(weight*2.5))