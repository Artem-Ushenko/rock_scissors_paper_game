import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
pc_choice_list = [rock, paper, scissors]

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
pc_choice = random.choice(pc_choice_list)

if my_choice == 0:
    print(rock)
    print(f"Computer chose: \n {pc_choice}")
    if pc_choice == rock:
        print("It's a draw!")
    elif pc_choice == paper:
        print("You lose!")
    elif pc_choice == scissors:
        print("You win!")


elif my_choice == 1:
    print(paper)
    print(f"Computer chose: \n {pc_choice}")
    if pc_choice == rock:
        print("You win!")
    elif pc_choice == paper:
        print("It's a draw")
    elif pc_choice == scissors:
        print("You lose!")

elif my_choice == 2:
    print(scissors)
    print(f"Computer chose: \n {pc_choice}")
    if pc_choice == rock:
        print("You lose!")
    elif pc_choice == paper:
        print("You win!")
    elif pc_choice == scissors:
        print("It's a draw")

else:
    print("Please enter your choice number (0-2) !!!")