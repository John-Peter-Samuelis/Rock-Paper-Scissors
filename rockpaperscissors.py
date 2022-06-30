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

choice      = [rock, paper, scissors]
user_input  = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
user_choice = "TO BE A DUMBASS!"

if user_input < 0 or user_input>2:
    print("Invalid Choice. Computer WINS!")
else:    
    user_choice = choice[user_input]

computer_choice = random.choice(choice)
print(f"You chose: \n {user_choice} \nComputer chose: {computer_choice}")

if user_choice == rock and computer_choice == scissors:
    print("You Win")
elif user_choice == scissors and computer_choice == paper:
    print("You win!")
elif user_choice == paper and computer_choice == rock:
    print("You win!")
elif user_choice == computer_choice:
    print("You draw!")
else:
    print ("You lose")
