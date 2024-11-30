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




### Code Lock ###
'''
print(Fore.RESET + Back.RESET,
			"CODE LOCKED. ENTER KEY" + Fore.BLACK + Back.BLACK + Style.DIM)
unlock = os.getenv("run_key")
#key = input("key: ")

# masking the password
key = getpass.getpass('Enter unlock key: ')

if key != unlock:
	sys.exit("Incorrect Key")
	cduld = False

clear()
clear = lambda: print("\033c", end="", flush=True)
print("RESET TEXT STYLE" + Fore.RESET + Back.RESET + Style.RESET_ALL)
clear()
print(Fore.GREEN + "CODE UNLOCKED" + Fore.RESET)
cduld = True
'''

