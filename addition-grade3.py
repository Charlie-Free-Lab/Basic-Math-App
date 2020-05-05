import random

while True:
    try:
        number_of_questions = int(input("How many questions would you like to do? Number: "))
        break
    except ValueError:
        print("Sorry please enter an integer")

def add(N1, N2):
    sum = str(N1 + N2)
    user_sum = input((str(N1) + " + " + str(N2) + " = "))
    while True:
        if str(user_sum) == sum:
            print("You are correct!")
            return True
        else:
            print("Sorry, your answer is wrong, please try again:")
            user_sum = input((str(N1) + " + " + str(N2) + " = "))

operations = [add]
for element in range(number_of_questions):
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)
    random.choice(operations)(num1, num2)
    # if num1 >= num2:
    #     random.choice(operations)(num1, num2)
    # else:
    #     element -= 1