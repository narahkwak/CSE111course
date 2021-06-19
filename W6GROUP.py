def main():
    print("The Rosenberg self-esteem scale is a self-esteem measure developed by the sociologist Morris Rosenberg in 1965")
    print("It is still used in social-science research today.")
    print("To complete the measure, a person completes a survey that contains the following ten statements.")

    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")

    answers = question()
    scoreing()

    print("A score below 15 may indicate problematic low self-esteem.") 


def question():
    print("1. I feel that I am a person of worth, at least on an equal plane with others. ")
    one = input("Enter D, d, a, or A: ")
    print("2. I feel that I have a number of good qualities.")
    two = input("Enter D, d, a, or A: ")
    print("3. All in all, I am inclined to feel that I am a failure.")
    three = input("Enter D, d, a, or A: ")
    print("4. I am able to do things as well as most other people.")
    four = input("Enter D, d, a, or A: ")
    print("5. I feel I do not have much to be proud of.")
    five = input("Enter D, d, a, or A: ")
    print("6. I take a positive attitude toward myself.")
    six = input("Enter D, d, a, or A: ")
    print("7. On the whole, I am satisfied with myself. ")
    seven = input("Enter D, d, a, or A: ")
    print("8. I wish I could have more respect for myself.")
    eight = input("Enter D, d, a, or A: ")
    print("9. I certainly feel useless at times.")
    nine = input("Enter D, d, a, or A: ")
    print("10. At times I think I am no good at all.")
    ten = input("Enter D, d, a, or A: ")
    answers = [one, two, three, four,  five, six, seven, eight, nine, ten ]
    return answers

def scoreing():
    score = 0
    for letter in answers:
        if letter == "A":
            score += 3
        elif letter == "a":
            score += 2
        elif letter == "d":
            score += 1    
        elif letter == "D":
            score += 0
    print(f"Your score is {score}. ")

main()