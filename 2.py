# BMI Calculator Program

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
    
def bmi_calculator():
    print("BMI Calculator")
    
    weight = float(input("Enter weigth in Kilogram: "))
    height = float(input("Enter height in meter: "))
    
    bmi = calculate_bmi(weight,height)
    category = bmi_category(bmi)
    
    print(f"your BMI is {bmi:.2f}")
    print(f"you are categorized as {category}")
    
bmi_calculator()