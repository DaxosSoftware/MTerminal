# This is the commands module
# This module contains all the commands for the program
import random
import sys
import time
import os
import datetime
import system
from system import Log

CommandsExecutedInSession = 0

FolderName = "app"

#Declares global error variables
ERR_0 = "ERR-0"
ERR_1 = "ERR-1"
ERR_2 = "ERR-2"
ERR_3 = "ERR-3"
ERR_4 = "ERR-4"

NewCommands = False

def Log(Type: int, Data: str = ""):
	"""
	Logs data in a specific rule set for debugging purposes

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

	Time = str(datetime.datetime.now())
	logs = open("logs.txt","a")
	logs.writelines("""
 ["""+ Time + "]: "+ Text)
	logs.close()

def Error(Error: int, Data: str = "", Data2: str = ""):
	"""
	This function processes the Inputted data and returns the error message for a certain error

	Args:
		Error (int): The integer value of the Error of the Error message you want
		Data (str):  The Data for the desired error message
		Data2 (str): The second set of Data needed for some error messages
	
	Returns:
		str: The Error message created from the system.userInputted data
	"""

	if Error == 0:
		return f'Command: {Data} is invalid or does not exist ## ERR-0'
	
	elif Error == 1:
		return 'The program has failed to close ## ERR-1'
	
	elif Error == 2:
		return f'Could not find file: {Data} ## ERR-2'
	
	elif Error == 3:
		return f'An unexpected internal error has occurred within: {Data} ## ERR-3'
	
	elif Error == 4:
		return f"Arg: '{Data}' in function: '{Data2}' is invalid ## ERR-4"

#Defines the "randomInt" command
def CommandRandomInt(num1, num2):
    system.Print(str(random.randrange(num1, num2)))
    Log(1, 'CommandRandomInt')
    system.Beep(700, 500) #Plays a beeping sound

#Defines the "exit" command
def CommandExit():
    global ERR_1

    Log(1, "CommandExit")
    system.Beep(700, 500) #Plays a beeping sound
    sys.exit(0)

    RandNum = random.randrange(0, 1_000_000)

    if RandNum == 13:
        system.ErrorPrint(ERR_1) #if this happens to you... you're VERY lucky... or very unlucky
        Log(2, Error(1))
    else:
        Log(0)

#Defines the "errors" command
def CommandErrors():
    Log(1, 'CommandErrors')
    
    system.Beep(700, 500) #Plays a beeping sound
    system.Print('Code:       Meaning:')
    system.Print("\n")
    system.Print("ERR-0: Command is not valid or does not exist")
    system.Print("ERR-1: The program has failed to close")
    system.Print("ERR-3: An unexpected internal error has occurred")
    system.Print("ERR-4: Arg: '' in function: '' is invalid")
    
def CommandPercy():
    Log(1, 'CommandPercy')

    system.Beep(700, 500) #Plays a beeping sound
    system.Print('''@@@@@@@%%@@@%%%%%%%%%%%#%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%###%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
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
        words: list[str] = ["python", "run", "fun", "computer", "science", "reindeer", "marry", "kill", "technology", "wash", "civilian", "cow", "obligation", "uncle", "abortion", "throat", "chase", "weave", "brick", "grave", "plane", "five", "cook", "train", "names"]
        words2: list[str] = ['hello', 'truck', 'bus', 'down', 'dawn', 'swish', 'name', 'money', 'monday', 'ruck', 'ruckus', 'baby', 'cop', 'criminal', 'firefighter', 'cancer', 'lung', 'lungs', 'city', 'java', 'c sharp', 'c plus plus', 'go', 'twenty', 'one', 'two', 'three']
        words.extend(words2)
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
        system.Print(f"Used letters: {" ".join(used_letters)}")

        # Current word (e.g. p - t - o n)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        system.Print(f"Current word: {" ".join(word_list)}")
        if debugging != True:
            user_letter = input("Guess a letter: ").lower()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    system.Print("")

                else:
                    lives -= 1  # Takes away a life if wrong
                    system.Print("Letter is not in word.")

            elif user_letter in used_letters:
                system.Print("You have already used that character. Please try again.")
    
            else:
                system.Print("Invalid character. Please try again.")

            # Gets here when len(word_letters) == 0 OR lives == 0
            if lives == 0:
                system.Print(f"You died, sorry. The word was {word}")
            elif len(word_letters) == 0:
                system.Print(f"You guessed the word {word}!!")
        else:
            system.Print(f"You died, sorry. The word was {word}")
            system.Print(f"You guessed the word {word}!!")

def CommandHangman(debugging):
    Log(1, 'Hangman')

    system.Beep(700, 500) #Plays a beeping sound
    play_hangman(debugging)

def ClearTerminal(debugging: bool = False):
    Log(1, 'ClearTerminal')

    system.Beep(700, 500) #Plays a beeping sound
    if debugging != True:
        userInput2 = system.userInput("Are you sure(y/n)? ", Type=0)
        if userInput2 == "y":
    
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
    
            system.Print("Canceled, did not clear the terminal.")
    else:
        system.Beep(700, 500)#Plays a beeping sound
        #Clears the terminal
        os.system('cls' if os.name == 'nt' else 'clear')

def CommandOpenFileText(FileName: str) -> None:
    Log(1, 'CommandOpenFileText')
    Path: str = f"./accessible_files/{FileName}.txt"
    if os.path.exists(Path):
        file = open(Path, "r")
        system.Print(file.read())
    else:

        system.ErrorPrint("File not found")

def CommandOpenFileBin(FileName: str) -> None:
    Log(1, 'CommandOpenFileBin')
    global FolderName
    Path = f"{FolderName}/accessible_files/{FileName}.bin"
    if os.path.exists(Path):
        file = open(Path, "r")
        system.Print(file.read())
    else:

        system.ErrorPrint("File not found")

def CommandOpenFileDat(FileName: str) -> None:
    Log(1, 'CommandOpenFileDat')
    global FolderName
    Path = f"{FolderName}/accessible_files/{FileName}.dat"
    if os.path.exists(Path):
        file = open(Path, "r")
        system.Print(file.read())
    else:

        system.ErrorPrint("File not found")

def CommandOpenFileNone(FileName: str) -> None:
    Log(1, 'CommandOpenFileNone')
    global FolderName
    Path = f"{FolderName}/accessible_files/{FileName}"
    if os.path.exists(Path):
        file = open(Path, "r")
        system.Print(file.read())
    else:

        system.ErrorPrint("File not found")

def CommandDebugAll():
    Log(1, 'CommandDebugAll')
    Log(5)

    system.Beep(700, 500) #Plays a beeping sound
    CommandRandomInt(1, 999_999_999)
    time.sleep(1)
    CommandErrors()
    time.sleep(1)
    CommandPercy()
    time.sleep(1)
    ClearTerminal(True)
    time.sleep(1)
    time.sleep(1)
    CommandExit()
    Log(6)

def CommandDebugNew():
    global NewCommands
    Log(1, 'CommandDebugNew')
    Log(5)

    system.Beep(700, 500) #Plays a beeping sound

    if NewCommands == False:
        system.Print("There are no new commands.")

    else:
        pass

    Log(Type=6)

def CommandWriteFileText(FileName: str) -> None:
    Log(1, 'CommandWriteFileText')
    global FolderName

    Path = f"{FolderName}/accessible_files/{FileName}.txt"
    if os.path.exists(Path):
        file = open(Path, "a")
        file.write(system.userInput(f"Enter data to be written to: {FileName}"))
    else:

        system.ErrorPrint("File not found")

def CommandWriteFileBin(FileName: str) -> None:
    Log(1, 'CommandWriteFileBin')
    global FolderName

    Path = f"{FolderName}/accessible_files/{FileName}.bin"
    if os.path.exists(Path):
        file = open(Path, "a")
        file.write(system.userInput(f"Enter data to be written to: {FileName}"))
    else:

        system.ErrorPrint("File not found")

def CommandWriteFileDat(FileName: str) -> None:
    Log(1, 'CommandWriteFileDat')
    global FolderName

    Path = f"{FolderName}/accessible_files/{FileName}.dat"
    if os.path.exists(Path):
        file = open(Path, "a")
        file.write(system.userInput(f"Enter data to be written to: {FileName}"))
    else:

        system.ErrorPrint("File not found")

def CommandWriteFileNone(FileName: str) -> None:
    Log(1, 'CommandWriteFileText')
    global FolderName

    Path = f"{FolderName}/accessible_files/{FileName}"
    if os.path.exists(Path):
        file = open(Path, "a")
        file.write(system.userInput(f"Enter data to be written to: {FileName}"))
    else:

        system.ErrorPrint("File not found")

def CommandCreateFileText(FileName: str) -> None:
    Log(1, 'CommandCreateFileText')
    global FolderName

    Path = f"{FolderName}/accessible_files/{FileName}.txt"
    if os.path.exists(Path):
        file = open(Path, "x")
        file.close()
    else:

        system.ErrorPrint("File not found")

def CommandCreateFileBin(FileName: str) -> None:
    Log(1, 'CommandCreateFileBin')
    global FolderName

    Path = f"{FolderName}/accessible_files/{FileName}.bin"
    if os.path.exists(Path):
        file = open(Path, "x")
        file.close()
    else:

        system.ErrorPrint("File not found")

def CommandCreateFileDat(FileName: str) -> None:
    Log(1, 'CommandCreateFileDat')
    global FolderName

    Path = f"{FolderName}/accessible_files/{FileName}.dat"
    if os.path.exists(Path):
        file = open(Path, "x")
        file.close()
    else:

        system.ErrorPrint("File not found")

def CommandCreateFileNone(FileName: str) -> None:
    Log(1, 'CommandCreateFileNone')
    global FolderName

    Path = f"{FolderName}/accessible_files/{FileName}"
    if os.path.exists(Path):
        file = open(Path, "x")
        file.close()
    else:

        system.ErrorPrint("File not found")

def CommandCreateAdminFile(FileName: str) -> None:
    if system.adminLoggedIn == False:
        system.ErrorPrint("Not logged into admin account")
        return
    Log(1, 'CommandCreateAdminFile')
    global FolderName

    Path = f"{FolderName}/admin_files/{FileName}"
    if os.path.exists(Path):
        file = open(Path, "x")
        file.close()
    else:
        system.ErrorPrint("File not found")

def CommandReadAdminFile(FileName: str) -> None:
    if system.adminLoggedIn == False:
        system.ErrorPrint("Not logged into admin account")
        return
    Log(1, 'CommandReadAdminFile')
    global FolderName
    Path = f"{FolderName}/admin_files/{FileName}"
    if os.path.exists(Path):
        file = open(Path, "r")
        system.Print(file.read())
    else:
        system.ErrorPrint("File not found")

def CommandWriteAdminFile(FileName: str) -> None:
    if system.adminLoggedIn == False:
        system.ErrorPrint("Not logged into admin account")
        return
    Log(1, 'CommandWriteAdminFile')
    global FolderName

    Path = f"{FolderName}/admin_files/{FileName}"
    if os.path.exists(Path):
        file = open(Path, "a")
        file.write(system.userInput(f"Enter data to be written to: {FileName}"))
    else:
        system.ErrorPrint("File not found")

def CommandAudioMute() -> None:
    Log(1, 'CommandAudioMute')
    system.MuteAudio()

def CommandAudiounmute() -> None:
    Log(1, 'CommandAudioUnmute')
    system.UnmuteAudio()
