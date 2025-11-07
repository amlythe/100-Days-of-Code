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

import random
options = ["Rock", "Paper", "Scissors"]

while True:
    computer_choice = random.choice(options)

    player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    if player_choice == "0":
        print(rock)
    elif player_choice == "1":
        print(paper)
    else:
        print(scissors)

    print("Computer chose:")
    if computer_choice == "Rock":
        print(rock)
    elif computer_choice == "Paper":
        print(paper)
    else:
        print(scissors)

    #Player plays Rock
    if player_choice == "0" and computer_choice == "Rock":
        print("Draw")
    elif player_choice == "0" and computer_choice == "Paper":
        print("You lose")
    elif player_choice == "0" and computer_choice == "Scissors":
        print("You win")

    #Player plays Paper
    if player_choice == "1" and computer_choice == "Rock":
        print("You win")
    elif player_choice == "1" and computer_choice == "Paper":
        print("Draw")
    elif player_choice == "1" and computer_choice == "Scissors":
        print("You lose")

    #Player plays Scissors
    if player_choice == "2" and computer_choice == "Rock":
        print("You lose")
    elif player_choice == "2" and computer_choice == "Paper":
        print("You win")
    elif player_choice == "2" and computer_choice == "Scissors":
        print("Draw")

    again = input("Play again? (y/n):\n").lower()
    if again != "y":
        break