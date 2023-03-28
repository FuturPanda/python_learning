import random

def get_choices() : 
  choices_list = ["rock", "paper", "scissors"]
  computer_choice = random.choice(choices_list)
  player_choice = input("Enter a move : ")
  choices = {
    "player" : player_choice,
    "computer" : computer_choice
  }
  return choices

def checkwin(player, computer):
  print(f"you chose {player}, and the computer chose {computer}")
  if player == computer :
    return "Draw"
  elif player == "rock" : 
    if computer == "paper" : 
      return "Paper cover Rock, You lose"
    else :
      return  "Rock Smashes Scissors : You win"
  elif player == "paper" : 
    if computer == "rock" : 
      return "Paper cover Rock, You win"
    else :
      return  "Paper Get Cut by Scissors : You loose"
  elif player == "scissors" : 
    if computer == "rock" : 
      return "Scissors get smashed by Rock, You loose"
    else :
      return  "Scissors Cut Paper : You Win"
  else : return "I Dont understand the choices"

def play() : 
  choices = get_choices()
  print(checkwin(choices["player"], choices["computer"]))

play()