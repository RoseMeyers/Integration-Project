    # Rose Meyers
    # An integration of everything I've learned about programming so far.
def main():
    print("Hello!")
    print("Welcome to my Integration Project for COP1500!")
    userName =input("Enter your name: ")
    # Name that user inputs will be combined with phrases throughout quiz
    print(userName + ", are you smarter than a fifth grader??")
    #Enter "math"
    print("Please enter below what subject you would like to try: math, history, english")
    subject1 = input()
    print("Subject you chose:", end= subject1)
    print()
    print("Great! Let's start with some basic math and find out!")
    # First question of math, addition
    Question1 = print("Question 1: What is 2.55 + 3 = ?")
    score = 0
    answer = input("Enter your answer: ")
    if float(answer) == (2.55+3) :
        print("Correct!")
        score += 1
    else:
        print("That is incorrect. No points earned.")
    print("The correct answer is",format(5.55,'.2f'))
    print("Your current score is {0}".format(score))
    #Second question of math,
    Question2 = print("Question 2! What is 50-15")
    score = score
    answer = input("Enter your answer: ")
    if int(answer) == (50-15):
        print("Correct!")
        score += 1
    if not int(answer) == (50-15) :
        print("That is incorrect. No points earned.")
        print("The correct answer is 35!")
    print("Your current score is {0}".format(score))
    #Third question of math, exponents and multiplication
    print("On to question 2!")
    Question3 = print("Question 3: What is (2*1)^3 ?")
    score = score
    answer = input("Enter your answer: ")
    if int(answer) == ((2*1)**3):
        print("Correct!")
        score += 1
    else:
        print("That is incorrect. No points earned.")
    print("The correct answer is 8!")
    print("Your current score is {0}".format(score))
    #Fourth question of math, division
    Question4 = print("Question 4: What is 30/3?")
    score = score
    answer = input("Enter your answer: ")
    if int(answer) == (30/3) :
        print("Correct!")
        score += 1
    else:
        print("That is incorrect. No points earned.")
    print("The correct answer is 10!")
    print("Your current score is {0}".format(score))
    #Fifth question of math, floor division
    Question5 = print("Question 5! You're halfway done! What is half of 15, rounded down to nearest whole number?")
    score = score
    answer = input("Enter your answer: ")
    if int(answer) == (15//2) :
        print("Correct!")
        score += 1
    else:
        print("That is incorrect. No points earned.")
    print("The correct answer is 7!")
    print("Your current score is {0}".format(score))
    #Sixth question of math, remainders
    #Invalid syntax with modulus?
    print("Keeping up so far? Next question")
    Question6 = print("Question 6: What is the remainder of 17/5?")
    score = score
    answer = input("Enter your answer: ")
    if answer == "2" :
    #Should calculate 17%5
        print("Correct!")
        score += 1
    else:
        print("That is incorrect. No points earned.")
        print("The correct answer is 2!")
    print("Your current score is {0}".format(score))
    if score >=6:
        print("Great job so far! You've gotten more than half of the questions correct! Keep it up!")
    #Seventh question of math, range and even numbers
    print("Next! Question 7")
    Question7 = print("Question 7: True or False: The even numbers between 3 and 11 are:")
    score = score
    for num in range(3,12):
        if num % 2 == 0:
            print(num, end = " ")
    print("\n") #skips line, easier to read
    answer = input("Enter your answer: ")
    if answer == ("true"):
        print("Correct!")
        score +=1
    elif answer == ("false"):
        print("That is incorrect. No points earned.")
        print("The correct answer is true!")
    else:
        print("That is incorrect. No points earned.")
        print("The correct answer is true!")
    print("Your current score is {0}".format(score))
    #Eigth question of math, logical operators, test if both true
    Question8 = print("Question 8: True or False again! If x = 10, is x greater than 3 and also less than 9?")
    score = score
    answer = input("Enter your answer: ")
    x = 10
    if answer == (x > 3 and x < 9) or ("false"):
        print ("you are correct!" )
        score +=1
    elif answer != ("false"):
            print("That is incorrect. No points earned.")
            print("The correct answer is false!")
    print("Your current score is {0}".format(score))
    #Ninth question of math
    Question9 = print("Question 9: List the numbers between 1 and 5.")
    score = score
    answer = input("Enter your answer: ")
    i=1
    while i < 6:
        if answer == ("1,2,3,4,5") or ("1 2 3 4 5"):
                print("Correct!")
                i += 1
                score += 1
                break #stops score count
        else:
            print("That is incorrect. No points earned.")
            break #ends loop
    print("The correct answer is",(1,2,3,4,5))
    print("Your current score is {0}".format(score))
    #Tenth question of math, final
    Question10 = print("Question 10: Take your number that's greater than 2, but less than 20, and divide it by 3. Round down if needed.")
    score= score
    import random
    import math
    randomNumber = random.randint(2,20)
    #w3schools "Python Random randint() Method"
    print("Your number is:", randomNumber)
    answer = input("Enter your answer: ")
    if int(answer) == (randomNumber//3) :
        print("Correct!")
        score += 1
    elif round(int(answer)) == round(int(answer)) :
    #Pogil 11 built in functions
        print("That is incorrect. You forgot to round down. No points earned.")
        print("The correct answer is" ,(randomNumber//3))
    else:
        print("That is incorrect. No points earned.")
    print("Your current score is {0}".format(score))
    
main()
