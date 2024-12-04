# IMPORTS
from time import sleep
from colorama import Fore, Back, Style, init
import os
import sys
from replit import clear
from random import randint
from game_tools import *
import binascii



'''
https://docs.google.com/document/d/10rOlHKvELJlZe1rTSGimzs3Q4rMm99l2Q7uR4lm9mt4/edit
'''
#EXCERSISE, INTELLIGENCE, FRIEDNLINESS, DROOL, NAME


#ASCII DOGS

dog1 = ["  __    __", "o-''))_____\\\\", "\"--__/ * * * )", "c_c__/-c____/"]
dog2 = ["  .", "..^____/", "`-. ___ )", "  ||  || mh"]
dog3 = ["		    __", "(\,--------'()'--o", " (_    ___    /~\"", "  (_)_)  (_)_)"]
dog4=["	^..^      /","	/_/\\_____/","	   /\\   /\\",".     /  \\ /  \\"]
dog5 = [".     __      _","	o'')}____//","	 `_/      )","	 (_(_/-(_/",]
ASCIIdogs = [dog1,dog2,dog3,dog4,dog5]

#VARIABLES
debug_mode = 0  # DEBUG MODE - 1=displays messages during code operation
failures = 0

debug_log = []
player_cards = []
computer_cards = []
cards = []

cards_to_be_played = 0
total_cards = 0
reply = ""
value_acceptable = False

excersise = 0
intelligence = 0
friendliness = 0
drool = 0

game = True
current_card = 0


#LOADING DOGS FROM TXT

file = open("dogs.txt", "rt")
for i in range(0, 30):
	excersise = 0
	intelligence = 0
	friendliness = 0
	drool = 0
	dog_card = []
	dog = file.readline()
	NameEnd = dog.index(".")
	name = dog[0:NameEnd]
	excersise = randint(1, 5)
	intelligence = randint(1, 100)
	friendliness = randint(1, 10)
	drool = randint(1, 10)
	dog_card.append(excersise)
	dog_card.append(intelligence)
	dog_card.append(friendliness)
	dog_card.append(drool)
	dog_card.append(name)
	#print(dog_card)
	cards.append(dog_card)

file.close()
#print(cards)
#debug_end()

total_cards = len(cards)

# FUNCTIONS


def debug(message, log_check):
	'''
	message, log check
	'''
	global debug_mode
	global debug_log
	debug_log.append(message)
	if debug_mode == 1:
		print(Fore.LIGHTCYAN_EX + "Debug: " + Fore.RESET + message)
	'''
	if log_check == 1:
		if input("log/cont [enter]")=="log":
			print(debug_log)
	'''


#CODE

debug("Initialisation", 0)

initialisation = "unsuccessful"
while initialisation == "unsuccessful":
	try:
		debug("shuffling cards...", 0)
		shuffle_cards(cards, 0)
		#print(cards)
	except Exception:
		debug("Error", 0)
		failures += 1
	finally:
		debug("successful", 0)
		initialisation = "successful"

		debug(
		    Fore.RESET + "initialisation: " + Fore.GREEN + "successful" +
		    Fore.RESET, 1)
		break

#TITLE SEQUENCE
debug("Title", 1)
print(Fore.RED + "")
slow_print(" ___   ___         ___   ___    ___     _____", 0.01)
slow_print("/     |     |     |     |   \\  |   \\ |    |    \\  / ", 0.01)
slow_print("|     |___  |     |___  |___/  |___/ |    |     \\/", 0.01)
slow_print("|     |     |     |     |   \\  | \\   |    |      |", 0.01)
slow_print("\\___  |___  |___  |___  |___/  |  \\  |    |      |", 0.01)

print(Fore.BLUE + "")

slow_print(" ___     ___      ___     ___", 0.01)
slow_print("|    \\  |   |    /       /", 0.01)
slow_print("|    |  |   |   |   __   |___", 0.01)
slow_print("|    |  |   |   |     |     |", 0.01)
slow_print("|___/   |___|    \\___/   ___/", 0.01)

print(Fore.GREEN + "\n\nA James Crowfoot Project")
sleep(5)
clear()

#MENU
'''
A menu is displayed allowing the user to select from the following options: 
Play Game or Quit.
'''

debug("menu", 1)

print(Fore.RED + "1. PLAY GAME")
print(Fore.BLUE + "2. QUIT" + Fore.GREEN)

reply = input()
reply = reply.upper()

if "1" in reply or "PLAY" in reply:
	#PLAY GAME
	clear()
	debug("play game --> loading", 0)
	#loading(1, 3)
elif "2" in reply or "QUIT" in reply:
	'''If the user selects the ‘Quit’ option then a suitable message should be 		  displayed and the program ends.'''
	sleep(0.5)
	clear()
	debug("quit", 1)
	sys.exit(Back.RED + Fore.BLACK + "GAME QUIT" + Fore.RESET + Back.RESET)

# PLAY GAME
debug("play game", 0)
debug("card select", 1)
'''
 If the user selects the ‘Play Game’ option they are asked to enter the number of cards to be played. If the entered number is less than 4 or greater than 30, or is an odd number, then an appropriate error message is displayed, and the user returns to the menu'''

try:
	debug("try", 0)
	value_acceptable = False
	while value_acceptable is False:
		reply = int(input("How many cards to be played in total: "))
		if reply <= 30 and reply > 3 and reply % 2 == 0:
			msg = Fore.GREEN + "value accepted" + Fore.RESET
			print(msg)
			value_acceptable = True
		else:
			print("must be an even number between 4 and 30 inclusive")
except Exception:
	debug("Error", 1)
finally:
	debug("finally", 1)
	cards_to_be_played = int(reply)
	cards_each = int(cards_to_be_played / 2)
	computer_cards = cards[0:cards_each]
	player_cards = cards[cards_each:cards_to_be_played]
	#print(computer_cards)
	#print(player_cards)

debug("GAME SEGMENT", 1)

# G A M E   S E G M E N T#

print("\n\n")
print("  #####     #    #     # ####### ")
print("#     #   # #   ##   ## #       ")
print("#        #   #  # # # # #       ")
print("#  #### #     # #  #  # #####   ")
print("#     # ####### #     # #       ")
print("#     # #     # #     # #       ")
print("#####   #     # #     # ####### ")
print("\n________________________________\n")
print("\n")

game = True
current_card = 0
PrevWinner = "Player"
while game == True:
	CurrentPlayerCard = player_cards[current_card]
	CurrentComputerCard = computer_cards[current_card]
	
	PlayExcersise = CurrentPlayerCard[0]
	PlayIntelligence = CurrentPlayerCard[1]
	PlayFriendliness = CurrentPlayerCard[2]
	PlayDrool = CurrentPlayerCard[3]
	PlayName = CurrentPlayerCard[4]

	BotExcersise = CurrentComputerCard[0]
	BotIntelligence = CurrentComputerCard[1]
	BotFriendliness = CurrentComputerCard[2]
	BotDrool = CurrentComputerCard[3]
	BotName = CurrentComputerCard[4]
	
	display_player_card(player_cards,computer_cards,current_card,ASCIIdogs)
	ValidCategory = False
	category = ""
	while ValidCategory is False:
		category = input("Category: ")
		if category.upper() in "EXCERSISE INTELLIGENCE FRIENDLINESS DROOL":
			ValidCategory = True
		else:
			print("Category must be: EXCERSISE INTELLIGENCE FRIENDLINESS DROOL")


	
	if category.lower() == "excersise":
		PlayerStat = PlayExcersise
		BotStat = BotExcersise
		if PlayerStat > BotStat:
			slow_print("Player Wins!",0.1)
			
			computer_cards.pop(current_card)
			player_cards.append(CurrentComputerCard)
			player_cards.pop(current_card)
			player_cards.append(CurrentPlayerCard)
		
		elif PlayerStat < BotStat:
			slow_print("Bot Wins!",0.1)
			player_cards.pop(current_card)
			computer_cards.append(CurrentPlayerCard)
			computer_cards.pop(current_card)
			computer_cards.append(CurrentComputerCard)
		else:
			slow_print("It's a Draw!",0.1)

	elif category.lower() == "intelligence":
		PlayerStat = PlayIntelligence
		BotStat = BotIntelligence
		if PlayerStat > BotStat:
			slow_print("Player Wins!",0.1)
			
			computer_cards.pop(current_card)
			player_cards.append(CurrentComputerCard)
			
			player_cards.pop(current_card)
			player_cards.append(CurrentPlayerCard)
		
		elif PlayerStat < BotStat:
			slow_print("Bot Wins!",0.1)
			player_cards.pop(current_card)
			computer_cards.append(CurrentPlayerCard)
			computer_cards.pop(current_card)
			computer_cards.append(CurrentComputerCard)
		else:
			slow_print("It's a Draw!",0.1)

	elif category.lower() == "friendliness":
		PlayerStat = PlayFriendliness
		BotStat = BotFriendliness
		if PlayerStat > BotStat:
			slow_print("Player Wins!",0.1)
			computer_cards.pop(current_card)
			player_cards.append(CurrentComputerCard)
			player_cards.pop(current_card)
			player_cards.append(CurrentPlayerCard)
		elif PlayerStat < BotStat:
			slow_print("Bot Wins!",0.1)
			player_cards.pop(current_card)
			computer_cards.append(CurrentPlayerCard)
			computer_cards.pop(current_card)
			computer_cards.append(CurrentComputerCard)
		else:
			slow_print("It's a Draw!",0.1)

	elif category.lower() == "drool":
		PlayerStat = PlayDrool
		BotStat = BotDrool
		if PlayerStat < BotStat:
			slow_print("Player Wins!",0.1)
			computer_cards.pop(current_card)
			player_cards.append(CurrentComputerCard)
			player_cards.pop(current_card)
			player_cards.append(CurrentPlayerCard)
			
		elif PlayerStat > BotStat:
			slow_print("Bot Wins!",0.1)
			player_cards.pop(current_card)
			computer_cards.append(CurrentPlayerCard)
			computer_cards.pop(current_card)
			computer_cards.append(CurrentComputerCard)
		else:
			slow_print("It's a Draw!",0.1)

	sleep(2)
	display_computer_card(player_cards,computer_cards,current_card,ASCIIdogs)
	sleep(2)
	if len(computer_cards) == 0:
		game = False
		print("PLAYER WINS")
	elif len(player_cards) == 0:
		game = False
		print("COMPUTER WINS")


sys.exit("GAME OVER")
	
