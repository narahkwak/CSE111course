#Team Activity for week 3
from datetime import datetime

def main():
    #get the user input #and call other functions
    gender = input("What is your gender?  ")
    birthdate = input("What is your birthdate? (YYYY-MM-DD):  ")
    weight = int(input("What is your weight in pounds?  "))
    height = int(input("What is your height in inches?  "))

    age = compute_age(birthdate)
    weight = kg_from_lb(weight)
    height = cm_from_in(height)

    bmi = body_mass_index(weight, height)
    bmr = basal_metabolic_rate(gender, weight, height, age)

    print(f"age = {age}, weight = {weight:.1f}kg, height = {height:.1f}cm, BMI = {bmi:.1f}, BMR = {bmr:.0f}kcal per day")

def compute_age(birth):
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()
    years = today.year - birthday.year
    if birthday.month > today.month or (birthday.month == today.month and birthday.day > today.day): 
        years -= 1
    return years


def kg_from_lb(lb):
    #1 lb = 0.45359237 kg
    kg = float(lb * 0.45359237)
    return kg

def cm_from_in(inch): 
    # 1 in = 2.54 cm
    cm = float(inch * 2.54)
    return cm

def body_mass_index(weight, height):
    bmi = float((10000 * weight) / height ** 2)
    return bmi

def basal_metabolic_rate(gender, weight, height, age):
    if gender.lower() == "woman":
        bmr = float(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age))
        return bmr
    elif gender.lower() == "man":
        bmr = float(88.362 + (13.398 * weight) + (4.799 * height) - (5.677 * age))
        return bmr
    
main()