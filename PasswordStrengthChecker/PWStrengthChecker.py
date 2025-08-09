#-------------- Libraries ---------------------
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
    global password, ogPWCount, newPWCount, criteria

    if ogInput != '1':
        criteria = 3
        password = customPW()
        print(f"\nYour generated password: {password}")

    else:
        password = pwLength()
        password = uniquenessOfPW(password)

    print("\n--- RESULTS ---")
    print(f"Final password is: {password}")
    print(f"Original password strength rating: {ogPWCount} out of {criteria}")
    print(f"After amendments: {newPWCount} out of {criteria}")


def customPW():
    while True:
        try:
            length = int(input("How long do you want your password to be (MAX 32): "))
            if length > 32 or length < 4:
                print("Please enter a length between 4 and 32.")
                continue    

            character = random.choice(specialChar)
            lettersPart = ''.join(random.choices(string.ascii_letters, k=length - 3))
            numberPart = str(random.randint(10, 99))

            newPW = lettersPart + character + numberPart
            return newPW

        except ValueError:
            print("Please only enter a number (e.g., '16').")


def pwLength():
    global ogPWCount, criteria
    criteria += 1

    while True:
        userPW = input("Please enter password for evaluation: ")
        length = len(userPW)

        if length <= 6:
            print("Password too short.")
            continue
        
        elif length > 32:
            print("Password is long - Shorten for memorability?")
            answer = input("Y/N: ")

            if answer.upper() == 'Y':
                newPW = input("Enter new password or type '1' for auto-generation: ")

                if newPW != '1':
                    return newPW
                else:
                    excess = len(userPW) - 32
                    shortenedPW = userPW[:-excess]
                    return shortenedPW
            else:
                return userPW        

        else:
            ogPWCount += 1
            return userPW


def uniquenessOfPW(password):
    global newPWCount, criteria
    criteria += 1

    if password.isalpha():
        print("Password must include numbers.")
        q = input("Enter new password or type '1' for auto-generation: ")
        if q == '1':
            num = random.randint(1000, 9999)
            password = password + str(num)
        else:
            password = q

    elif password.isdigit():
        print("Password must include letters.")
        q = input("Enter new password or type '1' for auto-generation: ")
        if q == '1':
            password = ''.join(random.choices(string.ascii_letters, k=4)) + password
        else:
            password = q

    elif re.match("^[a-zA-Z0-9]*$", password):
        print("No special characters detected.")
        q = input("Enter new password or type '1' for auto-generation: ")
        if q == '1':
            character = random.choice(specialChar)
            password = ''.join(random.choices(string.ascii_letters, k=4)) + character + str(random.randint(10, 99))
        else:
            password = q
    else:
        print("Password contains special characters.")

    newPWCount += 1
    return password

#------------------ Main Program ---------------------
originalInput = input("Enter '1' for your own PW to be evaluated, or type anything else for a generated password: ")
main(originalInput)