age = float(input("Please enter your age?  "))
max_heart = int(220 - age)
heart_rate1 = int( 0.65 * max_heart) 
heart_rate2 = int( 0.85 * max_heart)

print(f'When you exercise to strengthen your heart, you should keep your heart rate between {heart_rate1} and {heart_rate2} beats per minute')
