import math
from datetime import datetime
current_date_and_time = datetime.now().strftime ('%Y-%m-%d')

#print statement
print('This program is to compute the volume of space inside a tire ')
print()
# user input
width_tire = int(input('Enter the width of the tire in mm: '))
aspect_ratio = int(input('Enter the aspect ratio of the tire: '))
diameter_wheel = int(input('Enter the diameter of the wheel in inches: '))

#formula for volume of space
volume = float((math.pi * (width_tire ** 2) * aspect_ratio * ((width_tire * aspect_ratio) + (2540 * diameter_wheel))) / 10000000)
volume = round(volume, 1)
#print statement 

print(f'The approximate volume is {volume}')
print()

#txt file
with open("volumes.txt", "at") as volumes_file:
    print(f"{current_date_and_time},{width_tire},{aspect_ratio},{diameter_wheel},{volume}", file=volumes_file)


#extra for week2 asking the user if they want to buy
question = input("Would you like to buy tires with the dimensions that you entered? y/n :  ")
if question.lower() == 'y':
    number = input("Could you put in your phone number so we can reach out when your order is ready? ")
    with open("volumes.txt", "at") as volumes_file:
        print(f"The phone number is: {number}" , file=volumes_file)
if question.lower() == 'n':
    print("Let us know if you're ever interested! ")

print()
# extra input for feedback
review = input('Would you say you liked this program? y/n : ')
if review.lower() == 'y' :
    positive = input("Tell us what you liked about it: ")
    print("Thanks for enjoying! ")
if review.lower() == 'n' :
    negative = input("Tell us what we can do better: ")
    print("Sorry to hear that! We will be better the next time! ")


