from random import randint
from time import sleep
from replit import clear
from colorama import Fore, Back, Style
import sys

def slow_print(text,speed):
	'''
	text:str(), speed:int()
	text will be printed one character at a time,
	print(char)
	sleep(speed)
	----------------------------------------
	    >>>slowprint("Hello World",0.1)
			Hello World
	'''
	for char in text:
			print(char, end='', flush=True)
			sleep(speed)
	print(flush=False)

#slow_print("Hello, World!",0.05)


def shuffle_cards(array,disp):
	'''
	array : array
	disp : int() 1 or 0
	---------------------------
	>>>#shuffles cards
	>>>shuffle_cards(array,1)
	cards shuffled
	'''
	for i in range(0,len(array)):
		pos_a = randint(0,len(array))
		pos_b = randint(0,len(array))
		card_a = array[pos_a]
		card_b = array[pos_b]
		array[pos_a] = card_b
		array[pos_b] = card_a
	if disp == 1:
		print("cards shuffled")



def deal_cards(num_cards,cards,disp,comp_cards,play_cards): 
	'''
	num_cards:int()  total number of cards
	cards:array  array of cards
	disp:int() 1 or 0  prints "cards dealt"
	comp_cards:array  computer cards
	play_cards:array  player cards
	---------------------------------
	>>>deal_cards(20,array1,0,array2,array3)
	'''
	#total cards to be played, array of cards, debug.
	cards_each = int(num_cards / 2)#cards each is half of the total amount of cards
	print(cards_each)
	play_cards = cards[0:cards_each]
	comp_cards = cards[cards_each:(cards_each*2)]
	print(play_cards)
	print()
	print(comp_cards)
	if disp == 1:
		print("Cards Dealt")



def loading(load_speed,loop):
	'''
	load_speed: int() or float()
	loop: int()
	----------------------
	load_speed : speed [see slow_print()]
	loop: how many times for the loading animation to play
	'''
	step = load_speed/10
	for i in range(0,loop):
		clear()
		print(Fore.RESET+Back.RESET+"Loading...")
		slow_print("■■■■■■■■■■■",step)
	clear()
	print("loaded")
	sleep(1)
	clear()

def debug_end():
	'''
	ends program at this point
	'''
	sys.exit("Debug test. Ended Program")




def display_player_card(player_cards,computer_cards,current_card,ASCIIdogs):
	'''
	player_cards:array
	computer_cards:array
	current_card:int()
	ASCIIdogs:array
	-------------------------------
	displays current player card
	'''
	CurrentPlayerCard = player_cards[current_card]

	#extract values to display
	#EXCERSISE, INTELLIGENCE, FRIEDNLINESS, DROOL, NAME
	PlayExcersise = CurrentPlayerCard[0]
	PlayIntelligence = CurrentPlayerCard[1]
	PlayFriendliness = CurrentPlayerCard[2]
	PlayDrool = CurrentPlayerCard[3]
	PlayName = CurrentPlayerCard[4]

	NameAddon=""
	msg="|  name: "+ str(PlayName)
	LenName=len(msg)
	#print(LenName)
	for i in range(0,32-LenName):
		NameAddon+=" "

	ExcersiseAddon=""
	msg="|  excersise: "+ str(PlayExcersise)
	LenExcersise=len(msg)
	#print(LenExcersise)
	for i in range(0,32-LenExcersise):
		ExcersiseAddon+=" "

	IntelligenceAddon=""
	msg="|  intelligence: "+ str(PlayIntelligence)
	LenIntelligence=len(msg)
	#print(LenIntelligence)
	for i in range(0,32-LenIntelligence):
		IntelligenceAddon+=" "

	FriendlinessAddon=""
	msg="|  friendliness: "+ str(PlayFriendliness)
	LenFriendliness=len(msg)
	#print(LenFriendliness)
	for i in range(0,32-LenFriendliness):
		FriendlinessAddon+=" "

	DroolAddon=""
	msg="|  drool: "+ str(PlayDrool)
	LenDrool=len(msg)
	#print(LenDrool)
	for i in range(0,32-LenDrool):
		DroolAddon+=" "

	ascii = ASCIIdogs[randint(0,4)]
	print(Fore.LIGHTBLUE_EX+"\n\n-*--------- player card ---------*-")

	#Dog image
	for a in ascii:
		DogAddon=""
		msg="|  "+a
		LenDog=len(msg)
		#print(LenDog)
		for i in range(0,32-LenDog):
			DogAddon+=" "
		print("|   "+a,DogAddon,"|")
	#Dog Stats
	print("|  ~                               |")
	print("|  name: ", PlayName,NameAddon,"|")
	print("|  ~                               |")
	print("|  excersise: ", PlayExcersise,ExcersiseAddon,"|")
	print("|  ~                               |")
	print("|  intelligence: ", PlayIntelligence,IntelligenceAddon,"|")
	print("|  ~                               |")
	print("|  friendliness: ", PlayFriendliness,FriendlinessAddon,"|")
	print("|  ~                               |")
	print("|  drool: ", PlayDrool,DroolAddon,"|")
	print("|  ~                               |")
	print("-*--------------------------------*-\n"+Fore.RESET)









def display_computer_card(player_cards,computer_cards,current_card,ASCIIdogs):
	'''
	player_cards:array
	computer_cards:array
	current_card:int()
	ASCIIdogs:array
	-------------------------------
	displays current player card
	'''
	CurrentComputerCard = computer_cards[current_card]

	#extract values to display
	#EXCERSISE, INTELLIGENCE, FRIEDNLINESS, DROOL, NAME

	BotExcersise = CurrentComputerCard[0]
	BotIntelligence = CurrentComputerCard[1]
	BotFriendliness = CurrentComputerCard[2]
	BotDrool = CurrentComputerCard[3]
	BotName = CurrentComputerCard[4]

	NameAddon=""
	msg="|  name: "+ str(BotName)
	LenName=len(msg)
	#print(LenName)
	for i in range(0,32-LenName):
		NameAddon+=" "

	ExcersiseAddon=""
	msg="|  excersise: "+ str(BotExcersise)
	LenExcersise=len(msg)
	#print(LenExcersise)
	for i in range(0,32-LenExcersise):
		ExcersiseAddon+=" "

	IntelligenceAddon=""
	msg="|  intelligence: "+ str(BotIntelligence)
	LenIntelligence=len(msg)
	#print(LenIntelligence)
	for i in range(0,32-LenIntelligence):
		IntelligenceAddon+=" "

	FriendlinessAddon=""
	msg="|  friendliness: "+ str(BotFriendliness)
	LenFriendliness=len(msg)
	#print(LenFriendliness)
	for i in range(0,32-LenFriendliness):
		FriendlinessAddon+=" "

	DroolAddon=""
	msg="|  drool: "+ str(BotDrool)
	LenDrool=len(msg)
	#print(LenDrool)
	for i in range(0,32-LenDrool):
		DroolAddon+=" "

	ascii = ASCIIdogs[randint(0,4)]
	print(Fore.LIGHTRED_EX+"\n\n-*-------- computer card --------*-")

	#Dog image
	for a in ascii:
		DogAddon=""
		msg="|  "+a
		LenDog=len(msg)
		#print(LenDog)
		for i in range(0,32-LenDog):
			DogAddon+=" "
		print("|   "+a,DogAddon,"|")
	#Dog Stats
	print("|  ~                               |")
	print("|  name: ", BotName,NameAddon,"|")
	print("|  ~                               |")
	print("|  excersise: ", BotExcersise,ExcersiseAddon,"|")
	print("|  ~                               |")
	print("|  intelligence: ", BotIntelligence,IntelligenceAddon,"|")
	print("|  ~                               |")
	print("|  friendliness: ", BotFriendliness,FriendlinessAddon,"|")
	print("|  ~                               |")
	print("|  drool: ", BotDrool,DroolAddon,"|")
	print("|  ~                               |")
	print("-*--------------------------------*-\n"+Fore.RESET)
