from random import randint
from time import sleep
from replit import clear
from colorama import Fore, Back, Style

def slow_print(text,speed):
		for char in text:
				print(char, end='', flush=True)
				sleep(speed)
		print(flush=False)

#slow_print("Hello, World!",0.05)


def shuffle_cards(array,disp):
	for i in range(0,len(array)):
		pos_a = randint(0,len(array))
		pos_b = randint(0,len(array))
		card_a = array[pos_a]
		card_b = array[pos_b]
		array[pos_a] = card_b
		array[pos_b] = card_a
	if disp == 1:
		print("cards shuffled")



def deal_cards(num_cards,cards,disp): #total cards to be played, array of cards, debug.
	global player_cards
	global computer_cards
	cards_each = num_cards // 2 #cards each is half of the total amount of cards
	player_cards = cards[0:cards_each]
	computer_cards = cards[cards_each:(cards_each*2)]
	#print(player_cards)
	#print()
	#print(computer_cards)
	if disp == 1:
		print("Cards Dealt")



def loading(load_speed,loop):
	step = load_speed/10
	for i in range(0,loop):
		clear()
		print(Fore.RESET+Back.RESET+"Loading...")
		slow_print("■■■■■■■■■■■",step)
	clear()
	print("loaded")
	sleep(1)
	clear()






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

