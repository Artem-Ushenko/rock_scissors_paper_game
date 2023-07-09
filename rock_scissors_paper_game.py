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

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
pc_choice = [rock, paper, scissors]

pc_score = 0
my_score = 0

print(random.choice(pc_choice))