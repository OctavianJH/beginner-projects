#Libraries
import random
import time

#Lists
actions = ["rock", "paper", "scissors"]

rules = {
    ("rock", "scissors"): "win",
    ("rock", "paper"): "lose",
    ("rock", "rock"): "draw",
    ("paper", "rock"): "win",
    ("paper", "scissors"): "lose",
    ("paper", "paper"): "draw",
    ("scissors", "paper"): "win",
    ("scissors", "rock"): "lose",
    ("scissors", "scissors"): "draw"
}

#Global Variables

roundCounter = 0 
playerScore = 0 
computerScore = 0
counter = 0


#Subprograms
def startGame():
    try:
        start = input("Would you like to play rock paper scissors? Y/N")
        if start.upper() == 'Y':
            maxRounds = int(input("How many rounds would you like to play?: "))
            return maxRounds
        
        else:
            print("Ok. Have a good day!")
            return 0

    except ValueError:
        print("Sorry, your input was not recognized.")
        return 0


def mainGame(maxRounds):
    counter = 1
    score = 0 

    while counter <= maxRounds:
        print("Rock!")
        time.sleep(0.5)
        print("Paper!")
        time.sleep(0.5)
        print("Scissors!")
        time.sleep(0.5)
        print("Shoot!")

        userAction = input("What did you put?: ").lower()
        computerAction = random.choice(["rock", "paper", "scissors"])

        if userAction not in ["rock", "paper", "scissors"]:
            print("Sorry, I did not understand that action.")
            continue
        
        result = rules[(userAction, computerAction)]
        print(f"The computer chose {computerAction}. That means you {result}!")

        if result == 'win':
            score += 1
        elif result == 'lose':
            score -= 1  # remove this line if you don't want negative scores

        print(f"Current score: {score}")
        
        counter += 1  # increment here only once per round

    print(f"Final score after {maxRounds} rounds: {score}")


      
#Main
rounds = startGame()

if rounds > 0:
    mainGame(rounds)