# IMPORTS
from time import sleep
from colorama import Fore, Back, Style, init
import os
import sys
from replit import clear
import getpass
from random import randint
from game_tools import *

'''
https://docs.google.com/document/d/10rOlHKvELJlZe1rTSGimzs3Q4rMm99l2Q7uR4lm9mt4/edit
'''


#VARIABLES
debug_mode = 2 # DEBUG MODE - 1=displays messages during code operation
failures = 0

debug_log=[]
player_cards = []
computer_cards = []
cards = []

cards_to_be_played = 0
total_cards = 0
reply = ""
value_acceptable = False

excersise=0
intelligence=0
friendliness=0
drool=0

file = open("dogs.txt","rt")
for i in range(1,31):
	excersise=0
	intelligence=0
	friendliness=0
	drool=0
	dog_card=[]
	dog = file.readline()
	stats = dog[0:8]
	name=dog[8:]
	excersise=stats[0:2]
	intelligence=stats[2:4]
	friendliness=stats[4:6]
	drool=stats[6:8]
	dog_card.append(excersise)
	dog_card.append(intelligence)
	dog_card.append(friendliness)
	dog_card.append(drool)
	dog_card.append(name)
	print(dog_card)
	cards.append(dog_card)
	
file.close()
print(cards)
debug_end()

total_cards = len(cards)


# FUNCTIONS

def debug(message,log_check):
	global debug_mode
	global debug_log
	debug_log.append(message)
	if debug_mode == 1:
		print(Fore.LIGHTCYAN_EX+"Debug: "+Fore.RESET+message)
	'''
	if log_check == 1:
		if input("log/cont [enter]")=="log":
			print(debug_log)
	'''
		
		


#CODE

debug("Initialisation",0)

initialisation = "unsuccessful"
while initialisation == "unsuccessful":
	try:
		debug("Initialising...",0)
		shuffle_cards(cards,debug_mode)
	except Exception:
		debug("Error",0)
		failures+=1
	finally:
		debug("successful",0)
		initialisation = "successful"
		
		debug(Fore.RESET+"initialisation: "+Fore.GREEN+"successful"+Fore.RESET,1)
		break
	


#TITLE SEQUENCE
debug("Title",1)
print(Fore.RED+"")
slow_print(" ___   ___         ___   ___    ___     _____",0.01)
slow_print("/     |     |     |     |   \\  |   \\ |    |    \\  / ",0.01)
slow_print("|     |___  |     |___  |___/  |___/ |    |     \\/",0.01)
slow_print("|     |     |     |     |   \\  | \\   |    |      |",0.01)
slow_print("\\___  |___  |___  |___  |___/  |  \\  |    |      |",0.01)

print(Fore.BLUE+"")

slow_print(" ___     ___      ___     ___",0.01)
slow_print("|    \\  |   |    /       /",0.01)
slow_print("|    |  |   |   |   __   |___",0.01)
slow_print("|    |  |   |   |     |     |",0.01)
slow_print("|___/   |___|    \\___/   ___/",0.01)

print(Fore.GREEN+"\n\nA James Crowfoot Project")
sleep(5)
clear()


#MENU
'''
A menu is displayed allowing the user to select from the following options: 
Play Game or Quit.
'''

debug("menu",1)

print(Fore.RED+"1. PLAY GAME")
print(Fore.BLUE+"2. QUIT"+Fore.GREEN)

reply = input()
reply = reply.upper()

if "1" in reply or "PLAY" in reply:
	#PLAY GAME
	clear()
	debug("play game --> loading",0)
	loading(1,3)
elif "2" in reply or "QUIT" in reply:
	'''If the user selects the ‘Quit’ option then a suitable message should be 		  displayed and the program ends.'''
	sleep(0.5)
	clear()
	debug("quit",1)
	sys.exit(Back.RED+Fore.BLACK+"GAME QUIT"+Fore.RESET+Back.RESET)



# PLAY GAME
debug("play game",0)
debug("card select",1)

'''
 If the user selects the ‘Play Game’ option they are asked to enter the number of cards to be played. If the entered number is less than 4 or greater than 30, or is an odd number, then an appropriate error message is displayed, and the user returns to the menu'''

try:
	debug("try",0)
	value_acceptable = False
	while value_acceptable is False:
		reply = int(input("How many cards to be played in total: "))
		if reply < 30 and reply > 3 and reply%2 == 0:
			debug("value accepted",1)
			value_acceptable = True
		else:
			print("must be an even number between 4 and 30 inclusive")
except Exception:
	debug("Error",1)
finally:
	debug("finally",1)
	cards_to_be_played = reply
	deal_cards(cards_to_be_played,cards,debug)

print(computer_cards)
print(player_cards)
debug("GAME SEGMENT",1)

# G A M E   S E G M E N T#



'''
 If the user selects the ‘Play Game’ option they are asked to enter the number of cards to be played. If the entered number is less than 4 or greater than 30, or is an odd number, then an appropriate error message is displayed, and the user returns to the menu'''

'''
 The program should then read in the names of the dogs from the text file dogs.txt, creating a card for each dog.
'''
