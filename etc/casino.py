import random

user_choice = int(input("Choose number: "))

pc_choice = random.randint(1, 10)

playing = True

while playing:
    user_choice = int(input("Choose number: "))
    if user_choice == pc_choice:
        print("You won!")
        playing = False
    elif user_choice < pc_choice:
        print("Higher!")
    elif user_choice > pc_choice:
        print("Lower!")
