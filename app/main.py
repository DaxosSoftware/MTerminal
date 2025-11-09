import datetime
from commands import * # type: ignore #! This issue is not able to be fixed in this update, "# type: ignore" should not be removed under any circumstances unless the issue has been resolved.
import winsound
import system
import inspect
from system import Log

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'

#Logs the launching of the program
Log(7)

#Declares global variables
Active = True
ConsolVer = "ALPHA 0.1.8 Build #2025110801"
ConsolStartUpMessage = f"Welcome to MTerminal \n {ConsolVer}"
UserInput = ""
UserInput2 = ""
UserInput3 = ""
CommandsExecutedInSession = 0
ComIdChar = "/" #Declares the character(s) to recognize commands
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
Com8 = ComIdChar + "file.open"
Com8Def = ": Opens a file"
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
Com14 = ComIdChar + "file.write"
Com14Def = ": writes a line of data to the specified file"
Com15 = ComIdChar + "file.create"
Com15Def = ": creates a file with the specified extension and name"
Com16 = ComIdChar + "file.create.admin"
Com16Def = ": creates a file in the 'admin_files' folder (Admin only)"
Com17 = ComIdChar + "file.write.admin"
Com17Def = ": writes a line of data to the specified file in the 'admin_files' folder (Admin only)"
Com18 = ComIdChar + "file.read.admin"
Com18Def = ": reads the contents of a file in the 'admin_files' folder and prints out to the terminal(Admin only)"
Com19 = ComIdChar + "settings.audio.mute"
Com19Def = ": Mutes all audio from the program"
Com20 = ComIdChar + "settings.audio.unmute"
Com20Def = ": Unmutes all audio from the program"

Commands = [Com1,Com2,Com3,Com4,Com5,Com6,Com7,Com8,Com9,Com10,Com11,Com12,Com13,Com14,Com15, Com16, Com17, Com18, Com19, Com20]
CommandDefs = [Com1Def,Com2Def,Com3Def,Com4Def,Com5Def,Com6Def,Com7Def,Com8Def,Com9Def,Com10Def,Com11Def,Com12Def,Com13Def,Com14Def,Com15Def, Com16Def, Com17Def, Com18Def, Com19Def, Com20Def]

OneParameterCommands = list()
DualParameterCommands = list(Com2)

Log(3, 'Global Command')

def Error(Error: int, Data: str = "", Data2: str = "") -> str:
	"""
	This function processes the inputted data and returns the error message for a certain error

	Args:
		Error (int): The integer value of the Error of the Error message you want
		Data (str):  The Data for the desired error message
		Data2 (str): The second set of Data needed for some error messages
	
	Returns:
		str: The Error message created from the Inputted data
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
	
	else:
		return "An unknown error has occurred"
	
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
	UserInput = system.userInput(Type=1)
	if UserInput in DualParameterCommands:
		UserInput2 = system.userInput("Enter first parameter for command: \n")
		UserInput3 = system.userInput("Enter second parameter for command: ")
	elif UserInput in OneParameterCommands:
		UserInput2 = system.userInput("Enter first parameter for command: ")

#Defines the "help" command
def CommandHelp():
	Log(1)
	system.Print(f'{GREEN}---------- COMMANDS: ----------{RESET}')
	system.Print(f'{GREEN}--- Command: --------- Meaning: ---{RESET}')
	for Command in Commands[:]:
		CommandDef = CommandDefs[Commands.index(Command)]
		system.Print(f"{Command}{CommandDef}")

def CommandVar(Var: str):
	global adminLoggedIn
	global UserInput
	global UserInput2
	global UserInput3
	if Var == "adminLoggedIn":
		system.Print(f'adminLoggedIn: {adminLoggedIn}')
	
	elif Var == "UserInput":
		system.Print(f'UserInput: {UserInput}')
	
	elif Var == "UserInput2":
		system.Print(f'UserInput2: {UserInput2}')
	
	elif Var == "UserInput3":
		system.Print(f'UserInput3: {UserInput3}')

def CommandVarAll():
	system.Print(f"{GREEN}=========== Variables: ===========\n")
	system.Print(f"{GREEN}== Variable: =========== Value: ==")
	for Var in Vars:
		CommandVar(Var)


#Defines the function that processes the user's system.userInput
def ExecuteCommand():
	global Commands
	for Command in Commands[:]:
		if UserInput == Command:
			# build a function name from the command string, e.g. "/help" -> "CommandHelp", "/var.all" -> "CommandVarAll"
			func_name = "Command" + "".join(part.capitalize() for part in Command.lstrip(ComIdChar).split("."))
			func = globals().get(func_name)

			if callable(func):
				try:
					# decide how many arguments the target function expects (0..2) and call accordingly
					params = len(inspect.signature(func).parameters)
					if params == 0:
						func()
					elif params == 1:
						func(UserInput2)
					else:
						# for 2 or more parameters we pass UserInput2 and UserInput3
						func(UserInput2, UserInput3)
				except Exception:
					# report internal error if the call failed
					system.ErrorPrint(Error(3, func_name))
				# command handled, exit the loop / function
				return
			else:
				# no handler found for this command
				system.ErrorPrint(Error(0, Command))
				return

#Defines the start of the program
def ProgramStart():
	Log(1, 'ProgramStart')
	system.Print(ConsolStartUpMessage)
	system.Print("Enter '/help' for help with commands")

ProgramStart()
while True:
	GetUserInput()
	ExecuteCommand()
