"""An integration of everything I've learned about programming so far."""
__author__ = "Rose Meyers"


def main():
    """Main Program"""
    print("Hello!")
    print("Welcome to my Integration Project for COP1500!")
    userName = input("Enter your name: ")
    print(userName + ", are you smarter than a fifth grader??")
    # Enter "math"
    print(
        "You'll be tested on your math skills today. Please confirm this by "
        "entering the subject you're interested in below.")
    subject = input("Your subject today is: ")
    while subject not in ("math", "Math"):
        print(
            "That is not the subject you're being tested on. Please choose "
            "again.")
        # User is asked to try again
        subject = input("Your subject today is: ")
    print("Fantastic! Let's start with some basic ", end=subject)
    print("\n")
    # First question of math, addition
    print("Question 1: What is 2.55 + 3 = ?")
    score = 0
    # try and except were based off a TowardsDataScience user input in python
    # article on exception handling
    try:
        answer = input("Enter your answer: ")
        if float(answer) == (2.55 + 3):
            print("Correct!")
            score += 1
        else:
            print("That is incorrect. No points earned.")
    except ValueError:
        print("Incorrect. You did not enter a number.")
    print("The correct answer is", format(5.55, '.2f'))
    print_score(score)
    # Second question of math, TA helped with function with parameters
    print("\n")
    print("Question 2! What is 50-15")
    try:
        answer = input("Enter your answer: ")
        if int(answer) == (50 - 15):
            print("Correct!")
            score += 1
        if not int(answer) == (50 - 15):
            print("That is incorrect. No points earned.")
    except ValueError:
        print("Incorrect. You did not enter a number.")
    print("The correct answer is", simple_subtraction(50, 15))
    print_score(score)
    # Third question of math, exponents and multiplication
    print("\n")
    print("On to question 2!")
    print("Question 3: What is (2*1)^3 ?")
    try:
        answer = input("Enter your answer: ")
        if int(answer) == ((2 * 1) ** 3):
            print("Correct!")
            score += 1
        else:
            print("That is incorrect. No points earned.")
    except ValueError:
        print("Incorrect. You did not enter a number.")
    print("The correct answer is 8!")
    print_score(score)
    # Fourth question of math, division
    print("\n")
    print("Question 4: What is 30/3?")
    try:
        answer = input("Enter your answer: ")
        if int(answer) == (30 / 3):
            print("Correct!")
            score += 1
        else:
            print("That is incorrect. No points earned.")
    except ValueError:
        print("Incorrect. You did not enter a number.")
    print("The correct answer is 10!")
    print_score(score)
    # Fifth question of math, floor division
    print("\n")
    print(
        "Question 5! You're halfway done! What is half of 15, rounded down to "
        "nearest whole number?")
    try:
        answer = input("Enter your answer: ")
        if int(answer) == (15 // 2):
            print("Correct!")
            score += 1
        else:
            print("That is incorrect. No points earned.")
    except ValueError:
        print("Incorrect. You did not enter a number.")
    print("The correct answer is 7!")
    print_score(score)
    # Sixth question of math, remainders
    print("\n")
    print("Keeping up so far? Next question")
    print("Question 6: What is the remainder of 17/5?")
    try:
        answer = input("Enter your answer: ")
        if int(answer) == (17 % 5):
            print("Correct!")
            score += 1
        else:
            print("That is incorrect. No points earned.")
    except ValueError:
        print("Incorrect. You did not enter a number.")
    print("The correct answer is 2!")
    print_score(score)
    if score >= 6:
        print(
            "Great job so far! You've gotten more than half of the questions "
            "correct! Keep it up!")
    # Seventh question of math, range and even numbers
    print("\n")
    print("Next! Question 7")
    print(
        "Question 7: True or False: The even numbers between 3 and 11 are:")
    for num in range(3, 12):
        if num % 2 == 0:
            print(num, end=" ")
    print("\n")
    # skips line, easier to read
    answer = input("Enter your answer: ")
    if answer == "true":
        print("Correct!")
        score += 1
    elif answer == "false":
        print("That is incorrect. No points earned.")
        print("The correct answer is true!")
    else:
        print("That is incorrect. No points earned.")
        print("The correct answer is true!")
    print_score(score)
    # Eighth question of math, logical operators, test if both true
    print("\n")
    print(
        "Question 8: True or False again! If x = 10, is x greater than 3 and "
        "also less than 9?")
    answer = input("Enter your answer: ")
    while answer not in ("true", "false"):
        print("Please only enter true or false.")
        answer = input("Enter your answer: ")
    x = 10
    if answer == (3 < x < 9):
        print("you are correct!")
        score += 1
        print(score)
    elif answer != "false":
        print("That is incorrect. No points earned.")
    print("The correct answer is false!")
    print_score(score)
    # Ninth question of math
    print("\n")
    print("Question 9: List the numbers between 1 and 5.")
    answer = input("Enter your answer: ")
    i = 1
    while i < 6:
        if answer == "1,2,3,4,5" or answer == "1 2 3 4 5":
            print("Correct!")
            i += 1
            score += 1
            break
        # stops score count
        else:
            print("That is incorrect. No points earned.")
            break
    # ends loop
    print("The correct answer is", (1, 2, 3, 4, 5))
    print_score(score)
    # Tenth question of math, final
    print("\n")
    print(
        "Question 10: Take your number that's greater than 2, but less than "
        "20, and divide it by 3. Round down if needed.")
    import random
    random_number = random.randint(2, 20)
    # w3schools "Python Random randint() Method"
    print("Your number is:", random_number)
    try:
        answer = input("Enter your answer: ")
        if int(answer) == (random_number // 3):
            print("Correct!")
            score += 1
        elif round(int(answer)) == (random_number // 3) + 1:
            # Pogil 11 built in functions
            print(
                "That is incorrect. You forgot to round down. No points "
                "earned.")
            print("The correct answer is", (random_number // 3))
        else:
            print("That is incorrect. No points earned.")
    except ValueError:
        print("Incorrect. You did not enter a whole number.")
    print("\n")
    print("Your final score is {0}".format(score))
    if score >= 10:
        print("Great job!! You got 10/10 correct!")
    if score < 10:
        print("Well done! You got", score, "out of 10 correct!")
    print("\n")
    print("Thank you so much for playing!")


def simple_subtraction(number1, number2):
    """This function subtracts, parameters are number1 and number2, returns
answer"""
    answer = number1 - number2
    return answer


def print_score(score):
    """Keeps count of user score"""
    print("Your current score is {0}".format(score))


main()
