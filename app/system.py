# This file contains all the data for main functions

from datetime import datetime
from re import U
from time import sleep
import winsound
from sys import exit

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'

SysID = f'{BLUE}[SYS]: {RESET}'

ERR_0 = "ERR-0"
ERR_1 = "ERR-1"
ERR_2 = "ERR-2"
ERR_3 = "ERR-3"
ERR_4 = "ERR-4"

adminLoggedIn = False

adminPassword = "GhmnB12"
tries = 0

GuestID = f'{CYAN}[GUEST]: {RESET}'
AdminID = f'{CYAN}[ADMIN]: {RESET}'


def MuteAudio():
	global AudioMuted
	AudioMuted = True

def UnmuteAudio():
	global AudioMuted
	AudioMuted = False

UnmuteAudio()

def Beep(Frequency: int, Duration: int):
	if AudioMuted == False:
		winsound.Beep(Frequency, Duration)
	
	else:
		pass

def Print(Text: str):
	Beep(700, 500)
	print(f'{SysID}{Text}')
	sleep(0.15)

def ErrorPrint(Text: str):
	Beep(1000, 500)
	print(f'{RED}[ERROR]: {Text}{RESET}')
	sleep(0.15)

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
	
	elif Type == 7:
		Text = 'The Program was launched'
	
	else:
		return ERR_4

	Time = str(datetime.now())
	logs = open("logs.txt","a")
	logs.writelines("""
 ["""+ Time + "]: "+ Text)
	logs.close()

def userInput(Text: str = "", Type: int = 0) -> str:
	if Type == 0:
		Print(Text)
		if adminLoggedIn == False:
			Input = input(GuestID)
		else:
			Input = input(AdminID)
	elif Type == 1:
		if adminLoggedIn == False:
			Input = input(GuestID)
		else:
			Input = input(AdminID)
	else:
		Input = "TypeError"
	return Input

def Exit():
    global ERR_1

    Log(1, "CommandExit")
    Beep(700, 500) #Plays a beeping sound
    exit(0)

    RandNum = random.randrange(0, 1_000_000)

    if RandNum == 13:
        ErrorPrint(ERR_1) #if this happens to you... you're VERY lucky... or very unlucky
        Log(2, Error(1))
    else:
        Log(0)

def SignIntoAdmin():
	global adminLoggedIn
	global tries

	while tries < 3:
		Password = userInput("Enter Admin Password: ", Type=0)
		if Password == adminPassword:
			Print("Correct Password...")
			Print("Signing into Admin account...")

			Print("Successfully signed into Admin account")
			adminLoggedIn = True
			return
	
		else:
			ErrorPrint("Incorrect password please try again")
			adminLoggedIn = False
			tries += 1
	
	Print("Too many tries to log into the Admin account")
	Print("Closing Program...")
	Log(2, "Too many tries to log into the Admin account, closing program")
	Exit()
