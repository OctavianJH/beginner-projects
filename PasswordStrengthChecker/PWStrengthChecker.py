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
            

def uniquenessOfPW(password): #check for numbers, letters, and special characters. 
    criteria =+ 1
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

    elif password.isdigit():
        print("Password must include letters.")
        q = input("Enter new password or type '1' if you want me to create one for you: ")

        if q == '1':
            newPW = ''.join(random.sample(string.ascii_letters, 4)) + password
            print(f"Your new password is {newPW}")
            return newPW
        else:
            return q
        
    else:
        if re.match("^[a-zA-Z0-9]*$", password):
            print("No special characters detected.")
            q = input("Enter new password or type '1' if you want me to create one for you: ")

            if q == '1':
                number = random.randint(0, len(specialChar) - 1)
                character = specialChar[number]

                # Example: create a new password with some letters + special character + numbers
                newPW = ''.join(random.sample(string.ascii_letters, 4)) + character + str(random.randint(10,99))
                
                print(f"Your new password is {newPW}")
                return newPW
            else:
                return q
        else:
            ogPWCount += 1
            return newPW
        

#------------------ Main Program ---------------------

password = pwLength()
password = uniquenessOfPW(password)
print(f"Final password is: {password}")

print(f"Your original password a strength rating of {ogPWCount} out of {criteria}")
print(f"\n But after the ammendments it now has a score of {newPWCount} out of {criteria}")