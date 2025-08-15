import random

levels = ["EASY", "MEDIUM", "HARD"]

def startGame():
    while True:
        try:
            startingQ = input("Would you like to guess a number I am thinking of? Y/N ").upper()
            if startingQ == 'Y':
                roundNum = int(input("How many rounds? "))
                difficultyLevel = input("How challenging would you like the game to be? Easy, Medium, or Hard? ").upper()
                if difficultyLevel not in levels:
                    print("Sorry, I did not understand.")
                    continue
                else:
                    return difficultyLevel, roundNum
            elif startingQ == 'N':
                print("Ok. Have a good day.")
                exit()
            else:
                print("Please answer with Y or N.")
        except ValueError:
            print("Sorry, I do not understand.")

def computerNum(difficulty):
    if difficulty == 'EASY':
        return random.randint(1,10)
    elif difficulty == 'MEDIUM':
        return random.randint(1,100)
    else:
        return random.randint(1,1000)

def mainGame(computer_num):
    guessCounter = 0
    completed = False
    
    while not completed:
        try:
            playerNum = int(input("Please enter a number: "))
            guessCounter += 1
            
            if playerNum == computer_num:
                print(f"You win! It took you {guessCounter} guesses.")
                completed = True
            else:
                if abs(playerNum - computer_num) <= 10:
                    print("Hot!")
                elif abs(playerNum - computer_num) <= 100:
                    print("Warm.")
                else:
                    print("Cold.")
                    
        except ValueError:
            print("Sorry, I do not understand.")

# Main
difficulty, rounds = startGame()

for round_number in range(1, rounds + 1):
    print(f"\n--- Round {round_number} ---")
    secret_num = computerNum(difficulty)
    mainGame(secret_num)