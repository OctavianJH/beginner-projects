#------------------ Global Variables ---------------
password = ''






#------------------ Subfunctions -------------------

def pwLength():
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
                    newPW = userPW("Enter new password or type '1' if you want me to create one for you: ")

                    if newPW != '1':
                        print(f"Your new password is {password}.")
                        return newPW


                    else:
                        excess = len(userPW) - 32 #This gets the exceess amount of digits.
                        shortenedPW = newPW[:-excess]
                        print(f"Your new password is {password}.")
                        return shortenedPW
                        break
                else:
                     return userPW        

            else:
                print("PW Accepted.")
                return userPW

#------------------ Main Program ---------------------

password = pwLength()