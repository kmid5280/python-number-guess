import random

def number_guess():
  restart = ''
  while restart.upper() not in ['NO', 'N']:
    answer = random.randint(0,100) 
    tries = 1
    print(answer) 
    """Answer displayed for debugging purposes"""

    choice = input("Enter a number between 1 and 100: ")
    while int(answer) != int(choice) and tries < 10:
      if int(answer) > int(choice):
        tries+=1
        print(tries)
        choice = input("Answer is bigger. ")
      elif int(answer) < int(choice):
        tries+=1
        print(tries)
        choice = input("Answer is smaller. ")
    
    if tries == 10:
      restart = input("You lose. Play again? y/n ")
    elif tries == 1:
      print("Correct. It took you " + str(tries) + " try.")
      restart = input("Play again? y/n ")
    else:
      print("Correct. It took you " + str(tries) + " tries.")
      restart = input("Play again? y/n ")
  print("Thanks for playing! Goodbye.")

number_guess()

