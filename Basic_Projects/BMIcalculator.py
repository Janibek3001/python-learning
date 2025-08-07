def Calculate():
    height = float(input("Enter your height (in meters): "))
    weight = float(input("Enter your weight (in kg): "))
    result = weight/pow(height, 2)
    validator(result)

def validator(r):
    if r < 18.5:
        print("Light weight")
    elif 18.5 < r < 24.5:
        print("Normal weight")
    elif 24.5 < r < 30:
        print("Extra weight")
    else:
        print("Obese")
        
Calculate()