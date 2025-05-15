#This is the commands module
#This module contains all the commands for the program
import random
import sys
import time
import os
import datetime
import winsound
from system import *

CommandsExecutedInSesion = 0

#Declares global error variables
ERR_0 = "ERR-0"
ERR_1 = "ERR-1"
ERR_2 = "ERR-2"
ERR_3 = "ERR-3"
ERR_4 = "ERR-4"

NewCommands = False

def Log(Type: int, Data: str = ""):
	"""
	Logs data in a specific rule set for debuging perposes

	Args:
		Type (int): Determines how the data is logged
		Data (str): The data needed to log data efficiently e.g. The function name, The Error code, The names of a group of variables, or the name of a command.
	
	Returns:
		str: Returns an error if the arg 'Type' is invalid
	"""

	Text = ''
	if Type == 0:
		Text = 'The program has closed successfully'

	elif Type == 1:
		Text = f'Function: {Data} was called'
	
	elif Type == 2:
		Text = f'ERROR: {Data}'

	elif Type == 3:
		Text = f'Declared variable(s): {Data}'
	
	elif Type == 4:
		Text = f'Command: {Data} was executed'
	
	elif Type == 5:
		Text = 'Debugging Process started'
	
	elif Type == 6:
		Text = 'Debugging Process completed'
	
	else:
		return ERR_4

	Time = str(datetime.now())
	logs = open("logs.txt","a")
	logs.writelines("""
 ["""+ Time + "]: "+ Text)
	logs.close()

def Error(Error: int, Data: str = "", Data2: str = ""):
	"""
	This function processes the Inputed data and returns the error message for a certain error

	Args:
		Error (int): The integer value of the Error of the Error message you want
		Data (str):  The Data for the desired error message
		Data2 (str): The second set of Data needed for some error messages
	
	Returns:
		str: The Error messaage created from the userInputted data
	"""

	if Error == 0:
		return f'Command: {Data} is invalid or does not exist ## ERR-0'
	
	elif Error == 1:
		return 'The program has failed to close ## ERR-1'
	
	elif Error == 2:
		return f'Could not find file: {Data} ## ERR-2'
	
	elif Error == 3:
		return f'An unexpected internal error has occured within: {Data} ## ERR-3'
	
	elif Error == 4:
		return f"Arg: '{Data}' in function: '{Data2}' is invalid ## ERR-4"

#Defines the "randomInt" command
def CommandRandomInt(num1, num2):
    SysPrint(f"{random.randrange(num1, num2)}")
    Log(1, 'CommandRandomInt')
    winsound.Beep(700, 500) #Plays a beeping sound

#Defines the "exit" command
def CommandExit():
    global ERR_1

    Log(1, "CommandExit")
    winsound.Beep(700, 500) #Plays a beeping sound
    sys.exit(0)

    RandNum = random.randrange(0, 1_000_000)

    if RandNum == 13:
        ErrPrint(ERR_1) #if this happens to you... you're VERY lucky... or very unlucky
        Log(2, Error(1))
    else:
        Log(0)

#Defines the "errors" command
def CommandErrors():
    Log(1, 'CommandErrors')
    
    winsound.Beep(700, 500) #Plays a beeping sound
    SysPrint('Code:       Meaning:')
    SysPrint("\n")
    SysPrint("ERR-0: Command is not valid or does not exist")
    SysPrint("ERR-1: The program has failed to close")
    SysPrint("ERR-3: An unexpected internal error has occured")
    SysPrint("ERR-4: Arg: '' in function: '' is invalid")
    
def CommandPercy():
    Log(1, 'CommandPercy')

    winsound.Beep(700, 500) #Plays a beeping sound
    SysPrint('''@@@@@@@%%@@@%%%%%%%%%%%#%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%###%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@%@@@@%%%%%%%%%%########%%@@@@@@@@@@@@@@@@@@@@@@@@@@@%%#*****#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@%%%%%%%%%%%%#########%%%@@@@@@@@@@%@@%%@%%%%%*+++++****#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@%%%%%%%%%%%%%%%%%#******####%%####***++****#*####%##******#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@%%%%%%%%%%%%%%%%%%#********#####***+++++++*###%%%##******#%@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@%%%%%%%%%%%%%%%%%%********#####%%#******+*#%%%%%##******%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@%%%%%%%%%%%%%%%%%%%#*+++****########*#**#*#%#%%####****+#%@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@%%%%%%%%%%%%%%%%%%%%%*++**++++****#%%*++==+#%%####*******%@@@@%@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@%%%%%%%%%%%%%%%%%%%%%#*++==+++*****#*+=---==+*********++#%@@@%%%@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@%@%%%%%%%%%%%%%%%%%%%%*===+++++*+++==-------==++********+#@@@@%%@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@%%%%%%%%%%%%%%%%%%%%%#+==++++++++====--------===+++******#%@@@@@@@@%@@@@@@@@@@%%%%%%%%%%%%%%%@
@@@@@@@%%%%%%%%%%%%%%%%%%%%*===++++++======----=---====+++*****+#%@@@@@%%%%%%#*+++=================+
@@@@@@%%%%%%%%%%%%%%%%%%%%%*====+++++++++++============++++****++#%%#*======-----==================+
@@@@@@@%%%%%%%%%%%%%%%%%%%%#*+++++++********+++++++***+****#%%#+=----------------===================
@@@@@@@%%%%%%%%%%%%%%%%%%%%%#**++++*#%@@@%##***+++*#%@@%#*****+=-----------------===================
@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%#**++***###%#****++++####**++++==-----------------====================
@@@@@@%%%%%%%%%%%%%%%%%%@@@@@@%#***++++****++++++==+++++++=====--------------=======================
@@@@@@@%%%%%%%%%%%%@@@@@@@@@@@@%###***+++++++=========++++=====-----------==========================
@@@@@@@@%@%%%%@@@@@@@@@@@@@@@@@@@%####*+++++++========+++++++==----------========================+++
@@@@@@@@%%%%%%%@@@@@@@@@@@@@@@@@@@#####******+++==+==+++++++====--===---=======================+++++
@@@@@@@%%@%%%%@@@@@@@@@@@@@@@@@@@@%######***###****==++++++===============================++++++++++
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#########%%#**+++++++==================++++===+++++++++++++++++
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#######%###****+++++=+++++++======+++++++=+++++++++++++++++++
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#########****++++++===+++=+======+++++++++++++++++++++++++++
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%########*****+++===============+++++++++++++++++++++++++++++
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#************++++==============+++++****++***+++++++++++++++
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*************+++++++===========++++********++++++++++++++++
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*************+++++===++++++===++++********+++++++++++++***
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#####********++++++++++++++++++++*********++++++++++++++***
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#####***************++++++++++++*******++++++++++++******
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%####****************+****+++++*******++++++++**********
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%###******++++++*********++**+*******++++++**********##
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*++++++++++++++++********************++*************###
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*++++++++++++++***********************************#####
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#**************#########***####***************#*#######
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%################%%############*********##############
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@%%%%%@%%%##*******#***######%%%%#%%##
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%##############%%%%%%%%%%#
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%##########%%%%%%%%%%%%
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%@@%%%%%%
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%@%''')
    
def get_word():
        words1 = ["python", "run", "fun", "computer", "science", "reindeer", "marry", "kill", "technology", "wash", "civilian", "cow", "obligation", "uncle", "abortion", "throat", "chase", "weave", "brick", "grave", "plane", "five", "cook", "train", "names"]
        words2 = ['hello', 'truck', 'bus', 'down', 'dawn', 'swish', 'name', 'money', 'monday', 'ruck', 'ruckus', 'baby', 'cop', 'criminal', 'firefighter', 'cancer', 'lung', 'lungs', 'city', 'java', 'c sharp', 'c plus plus', 'go', 'twenty', 'one', 'two', 'three']
        words1.extend(words2)
        words = words1
        return random.choice(words)

def play_hangman(debugging):
    global word
    global used_letters
    global word_letters
    word = get_word()
    word_letters = set(word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set()
    lives = 6

    while lives > 0 and len(word_letters) > 0:
        # Letters used
        SysPrint("Used letters: ", " ".join(used_letters)) # type: ignore

        # Current word (e.g. p - t - o n)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        SysPrint("Current word: ", " ".join(word_list)) # type: ignore
        if debugging != True:
            user_letter = userInput(0, "Guess a letter: ").lower()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    SysPrint("")

                else:
                    lives -= 1  # Takes away a life if wrong
                    SysPrint("Letter is not in word.")

            elif user_letter in used_letters:
                SysPrint("You have already used that character. Please try again.")
    
            else:
                SysPrint("Invalid character. Please try again.")

            # Gets here when len(word_letters) == 0 OR lives == 0
            if lives == 0:
                SysPrint(f"You died, sorry. The word was {word}") # type: ignore
            elif len(word_letters) == 0:
                SysPrint(f"You guessed the word {word}, !!")
        else:
            SysPrint(f"You died, sorry. The word was {word}")
            SysPrint(f"You guessed the word {word}, !!")

def Hangman(debugging):
    Log(1, 'Hangman')

    winsound.Beep(700, 500) #Plays a beeping sound
    play_hangman(debugging)

def ClearTerminal(debugging: bool = False):
    Log(1, 'ClearTerminal')

    winsound.Beep(700, 500) #Plays a beeping sound
    if debugging != True:
        UserInput2 = userInput(0, "Are you sure(y/n)? ")
        if UserInput2 == "y":
            winsound.Beep(700, 500) #Plays a beeping sound
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            winsound.Beep(700, 500) #Plays a beeping sound
            SysPrint("Canceled, did not clear the terminal.")
    else:
        winsound.Beep(700, 500)#Plays a beeping sound
        #Clears the terminal
        os.system('cls' if os.name == 'nt' else 'clear')

def OpenFile(path):
    Log(1, 'OpenFile')

    winsound.Beep(700, 500) #Plays a beeping sound
    if os.path.exists(path):
        file = open(path, "r")
        SysPrint(file.read())
    else:
        winsound.Beep(700, 500) #Plays a beeping sound
        ErrPrint("File not found")

def DebugAll():
    Log(1, 'DebugAll')
    Log(5)

    winsound.Beep(700, 500) #Plays a beeping sound
    CommandRandomInt(1, 999_999_999)
    time.sleep(1)
    CommandErrors()
    time.sleep(1)
    CommandPercy()
    time.sleep(1)
    ClearTerminal(True)
    time.sleep(1)
    OpenFile("C:/Users/daxos/Python/MTerminal/MTerminal_ALPHA_0.1.7/app/debug.txt")
    time.sleep(1)
    CommandExit()
    Log(6)

def DebugNew():
    global NewCommands
    Log(1, 'DebugNew')
    Log(5)

    winsound.Beep(700, 500) #Plays a beeping sound

    if NewCommands == False:
        SysPrint("There are no new commands.")

    else:
        pass

    Log(6)
