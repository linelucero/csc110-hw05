"""
Name: Aline Valenzuela-Lucero
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

def get_letter():
    """ This fucntions purpose is to use a while true loop which asks
        the user for a single letter. A series of conditionals then
        reject if the character is more than one and if it is not A
        B or C. After, if all conditionals are obeyed, the input will
        be returned."""
    
    while True:
        lett = input("Give an single uppercase letter: ") #asks user for a letter
        if len(lett) > 1 or len(lett) == 0:
            print("Error: it needs to be a single character.") # sets length boundaries
            continue
        elif "A" not in lett and "B" not in lett and "C" not in lett:
            print("Error: You provided the wrong character.")
            #if the letter aint A,B,C, then it will restart
        else:
            return lett #if A,B,C then the letter will be returned
        

def get_digit():
    """ This function uses a while true loop which asks the user for
        a single numberm making sure it is a digit. A series of conditionals
        will reject the value if its not a digit or if its too long. It also has to be 1,2,3
        in order for it to work. At the end, the input will be returned."""

    while True:
        digit = str(input("Give an single number character: ")) #asks for user digit input
        if not digit.isdigit(): #reads id digit is not a digit
            print("Error: your input should be only digits.") #rejects and asks for it again
            continue
        elif len(digit) > 1 or len(digit) == 0: #sets the conditions for input length
            print("Error: a single digit needs to be in [1,3].") #if not 1 then it rejects
        elif "1" not in digit and "2" not in digit and "3" not in digit:
            print("Error: a single digit needs to be in [1,3].") #if it aint 1,2,3 then try again
        else:
            return digit #returns if all conditions are met


def check_pattern(letter, digit, st_list):
    """ this function checks to see if the input from the user appears in a list of values where the letter does first then the digit for any combination. """

    print("Strings with the pattern:")
    
    for word in st_list: #searched for indexes in the list
        if letter in word and digit in word: #narrows down the indexes for those that include both inputs
            if word.index(letter) < word.index(digit): #if the index of the letter is smaller than that of the digit, in other words the letter comes first
                print(word,end= " ") #then those values that meet the conditions will be printed on one line
    print()


#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------
    
    while True:
        letter = get_letter() #calls get letter
        digit = get_digit()#calles the digit
    
        ls = check_pattern(letter, digit, st_list) #inserts the parameters in said function
    
        ta = input("Try Again? (y/n): ") #after all functions are cycled trhough, it will ask to try again y if yes and n if no from user.
        if ta == "y":
            continue
        elif ta == "n":
            break
    

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()