#--------------Libraries---------------------
import random
import string
import re 

#------------------ Global Variables ---------------
password = ''
ogPWCount = 0
newPWCount = 0
criteria = 0 
#------------------ Lists --------------------------
specialChar = [
    "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/",
    ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"
]

#------------------ Subfunctions -------------------
def main(ogInput):
    if ogInput != '1':
        customPW()

    else:
        password = pwLength()
        password = uniquenessOfPW(password)

        print(f"Final password is: {password}")

        print(f"Your original password a strength rating of {ogPWCount} out of {criteria}")
        print(f"\n But after the ammendments it now has a score of {newPWCount} out of {criteria}")


def customPW():
    while True:

        try:
            length = int(input("How long do you want your password to be (MAX 32):"))
            if length > 32 or length < 4:
                print("Please enter a length between 4 and 32.")
                continue    
            
            number = random.randint(0, len(specialChar) - 1)
            character = specialChar[number]
            newPW = ''.join(random.sample(string.ascii_letters, 4)) + character + str(random.randint(10,99))

            lettersCount = length - 3

            lettersPartofPW = ''.join(random.choices(string.ascii_letters, k=lettersCount))
            numberPart = str(random.randint(10, 99))

            newPW = lettersPartofPW + character + numberPart
            print(f"Your new password is: {newPW}")
            return newPW

        except ValueError:
            print("Please only enter a number - ie '16' (Meaning 16 Characters long.)")


def pwLength():
    criteria =+ 1 
    while True:
            userPW = input("Please enter password for evaluation:")
            length = len(userPW)

            if length <= 6:
                print("Password too short.")
                continue
            
            elif length >= 32:
                print("Password is long - Shorten for memorability?")
                answer = input("Y/N")

                if answer.upper() == 'Y':
                    newPW = input("Enter new password or type '1' if you want me to create one for you: ")

                    if newPW != '1':
                        print(f"Your new password is {newPW}.")
                        return newPW


                    else:
                        excess = len(userPW) - 32 #This gets the exceess amount of digits.
                        shortenedPW = newPW[:-excess]
                        print(f"Your new password is {shortenedPW}.")
                        return shortenedPW
                        break
                else:
                     return userPW        

            else:
                ogPWCount += 1
                return userPW
            

def uniquenessOfPW(password): # checks if password contains just letters
    if password.isalpha():
        print("Password must include numbers.")
        q = input("Enter new password or type '1' if you want me to create one for you: ")

        if q == '1':
            num = random.randint(1000, 9999)  # 4 digit number
            newPW = password + str(num)
            print(f"Your new password is {newPW}")
            return newPW
        else:
            return q

    elif password.isdigit(): #checks to see if password contains only digits

        print("Password must include letters.")
        q = input("Enter new password or type '1' if you want me to create one for you: ")

        if q == '1':
            newPW = ''.join(random.choices(string.ascii_letters, k=4)) + password
            print(f"Your new password is {newPW}")
            return newPW
        else:
            return q

    elif re.match("^[a-zA-Z0-9]*$", password):  #checks if password contains only letters and digits (no special characters)
        print("No special characters detected.")
        q = input("Enter new password or type '1' if you want me to create one for you: ")

        if q == '1':
            character = random.choice(specialChar)
            newPW = ''.join(random.choices(string.ascii_letters, k=4)) + character + str(random.randint(10,99))
            print(f"Your new password is {newPW}")
            return newPW
        else:
            return q

    # If password contains special characters already, accept it as is
    else:
        print("Password contains special characters.")
        return password

#------------------ Main Program ---------------------

originalInput = input("Enter 1 for your custom PW to be evaluated or type 'create' if you want a generated password:")

main(originalInput)