import datetime
from commands import *
import winsound
from system import *
import system

#Logs the launching of the program
Log(7)

#Declares global variables
Active = True
ConsolVer = "BETA 0.1.8 Build 1"
ConsolStartUpMessage = f"Welcome to MTerminal {ConsolVer}"
UserInput = ""
UserInput2 = ""
UserInput3 = ""
CommandsExecutedInSesion = 0
ComIdChar = "/" #Declares the character(s) to reconize commands
adminLoggedIn = system.adminLoggedIn

Log(3, 'Global')

#Declares global error variables
ERR_0 = "ERR-0"
ERR_1 = "ERR-1"
ERR_2 = "ERR-2"
ERR_3 = "ERR-3"
ERR_4 = "ERR-4"

Log(3, 'Global Error')

#Declares global command variables
Com1 = ComIdChar + "help"
Com1Def = ": Shows a list of commands"
Com2 = ComIdChar + "randint"
Com2Def = ": Generates a random number without a decimal between 2 numbers given by the user"
Com3 = ComIdChar + "exit"
Com3Def = ": Closes the program"
Com4 = ComIdChar + "errors"
Com4Def = ": Shows a list of errors"
Com5 = ComIdChar + "percy"
Com5Def = ": Displays a picture of my cat Percy out of ASCII characters"
Com6 = ComIdChar + "hangman"
Com6Def = ": Starts a game of hangman"
Com7 = ComIdChar + "clear"
Com7Def = ": Clears the terminal"
Com8 = ComIdChar + "open.txt"
Com8Def = ": Opens a text file"
Com9 = ComIdChar + "debug.all"
Com9Def = ": Runs through all of the commands one after another to find errors and bugs"
Com10 = ComIdChar + "debug.new"
Com10Def = ": Runs through all of the NEW commands one after another to find errors and bugs"
Com11 = ComIdChar + "admin"
Com11Def = ": Signs into the admin account"
Com12 = ComIdChar + "var"
Com12Def = ": displays the value of a variable (For debugging)"
Com13 = ComIdChar + "var.all"
Com13Def = ": displays the values of all variables (For debugging)"

OneParameterCommands = list()
DualParameterCommands = list(Com2)

Log(3, 'Global Command')

def Error(Error: int, Data: str = "", Data2: str = ""):
	"""
	This function processes the userInputed data and returns the error message for a certain error

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
	
AdminOnlyCommands = [Com8, Com9, Com10, Com12, Com13]

Vars = [
	"adminLoggedIn",
	"UserInput",
	"UserInput2",
	"UserInput3",
]

#Defines a function to get the user's Input
def GetUserInput():
	Log(1, 'GetUserInput')
	global UserInput
	global UserInput2
	global UserInput3
	global Com2
	UserInput = userInput(1)
	if UserInput in DualParameterCommands:
		UserInput2 = userInput(0,"Enter first parameter for command: \n")
		UserInput3 = userInput(0,"Enter second parameter for command: ")
	elif UserInput in OneParameterCommands:
		UserInput2 = userInput(0,"Enter first parameter for command: ")

#Defines the "help" command
def CommandHelp():
	Log(1)
	SysPrint(f'{GREEN}---------- COMMANDS: ----------{RESET}')
	SysPrint(f'{GREEN}--- Command: --------- Meaning: ---{RESET}')
	SysPrint(f'{Com1}{Com1Def}')
	SysPrint(f'{Com2}{Com2Def}')
	SysPrint(f'{Com3}{Com3Def}')
	SysPrint(f'{Com4}{Com4Def}')
	SysPrint(f'{Com6}{Com6Def}')
	SysPrint(f'{Com7}{Com7Def}')
	SysPrint(f'{Com8}{Com8Def}')
	SysPrint(f'{Com9}{Com9Def}') 
	SysPrint(f'{Com10}{Com10Def}')
	SysPrint(f'{Com11}{Com11Def}')
	SysPrint(f'{Com12}{Com12Def}')

def CommandVar(Var: str):
	global adminLoggedIn
	global UserInput
	global UserInput2
	global UserInput3
	if Var == "adminLoggedIn":
		SysPrint(f'adminLoggedIn: {adminLoggedIn}')
	
	elif Var == "UserInput":
		SysPrint(f'UserInput: {UserInput}')
	
	elif Var == "UserInput2":
		SysPrint(f'UserInput2: {UserInput2}')
	
	elif Var == "UserInput3":
		SysPrint(f'UserInput3: {UserInput3}')

def CommandVarAll():
	SysPrint(f"{GREEN}=========== Variables: ===========\n")
	SysPrint(f"{GREEN}== Variable: =========== Value: ==")
	for Var in Vars:
		CommandVar(Var)


#Defines the function that processes the user's userInput
def ExecuteCommand():
	global UserInput
	global UserInput2
	global UserInput3
	global CommandsExecutedInSesion
	global Com1
	global Com2
	global Com3
	global Com4
	global Com5
	global Com6
	global Com7
	global Com8
	global Com9
	global Com10
	global Com11
	global ERR_0
	global adminLoggedIn
	Log(1, 'ExecuteCommand')
	if adminLoggedIn == False:
		if UserInput in AdminOnlyCommands:
			ErrPrint("Not logged into admin account")
			return

	if UserInput[0] != ComIdChar:
		SysPrint(UserInput)
		CommandsExecutedInSesion = CommandsExecutedInSesion + 1

	else:

		if UserInput == Com1:
			CommandHelp()
			CommandsExecutedInSesion = CommandsExecutedInSesion + 1

		elif UserInput == Com2:
			winsound.Beep(700, 500) #Plays a beeping sound
			UserInput2 = userInput(0,'Enter parameter one: ')
			UserInput3 = userInput(0,"Enter parameter two: ")
			CommandRandomInt(int(UserInput2), int(UserInput3))
			CommandsExecutedInSesion = CommandsExecutedInSesion + 1

		elif UserInput == Com3:
			CommandExit()
			CommandsExecutedInSesion = CommandsExecutedInSesion + 1

		elif UserInput == Com4:
			CommandErrors()
			CommandsExecutedInSesion = CommandsExecutedInSesion + 1

		elif UserInput == Com5:
			CommandPercy()
			CommandsExecutedInSesion = CommandsExecutedInSesion + 1
		
		elif UserInput == Com6:
			Hangman(False)
			CommandsExecutedInSesion = CommandsExecutedInSesion + 1

		elif UserInput == Com7:
			ClearTerminal(False)

		elif UserInput == Com8:
			UserInput2 = userInput(0,"Enter file path(Copy-paste) ")
			OpenFile(UserInput2)

		elif UserInput == Com9:
			DebugAll()

		elif UserInput == Com10:
			DebugNew()
		
		elif UserInput == Com11:
			SignIntoAdmin()
			adminLoggedIn = system.adminLoggedIn
		
		elif UserInput == Com12:
			UserInput2 = userInput(0,"Enter variable: ")
			CommandVar(UserInput2)
		
		elif UserInput == Com13:
			CommandVarAll()

		else:
			ErrPrint(ERR_0)
			Log(2, Error(0, UserInput)) # type: ignore
			CommandsExecutedInSesion = CommandsExecutedInSesion + 1

#Defines the start of the program
def ProgramStart():
	Log(1, 'ProgramStart')
	SysPrint(ConsolStartUpMessage)
	SysPrint("Enter '/help' for help with commands")

ProgramStart()
while True:
	GetUserInput()
	ExecuteCommand()