# Rock Paper Scissors
# Instructions
# Make a rock, paper, scissors game.
#
# Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.
#
# Start the game by asking the player:
#
# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."
#
# From there you will need to figure out:
#
# How you will store the user's input.
# How you will generate a random choice for the computer.
# How you will compare the user's and the computer's choice to determine the winner (or a draw).
# And also how you will give feedback to the player.
# You can find the "official" rules of the game on the World Rock Paper Scissors Association website.

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