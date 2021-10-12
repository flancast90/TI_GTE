from ti_system import *
import time

# TI_GTE: A general-purpose text editor for the TI84-CE PLUS series
# Copyright (c) Finn Lancaster 2021
# Open-Source MIT License

# simple opt menu for user selection
def opt_menu(msg):
	# clear TI specific messages before we begin
	disp_clr()
	
	# menu title and text
	print("\033[1mOptMenu: TI_GTE \033[0m\n\n")
	print("1. Recall Save\n")
	print("2. New File\n")
	print("3. Search Files\n")

	# get user selection as native input
	inp = int(input(msg))

	# call function determined from user input
	if (inp == 1):
		list_saves()
	elif (inp == 2):
		new_save()
	elif (inp == 3):
		search_saves()
	else:
		# clear the console (ti_system)
		disp_clr()
		opt_menu("Enter a valid sel. num. ")


# check calculator vars with recall_list() and loop
# since we know we save with a common naming structure
def list_saves():
	# clear the console (ti_system)
	disp_clr()
	print("\033[1mListSaves: TI_GTE \033[0m\n\n")
		
	i = 0
	save_exists = True

	while (save_exists == True):
		try:
			if (recall_list("GTE"+str(i))):
				print("GTE"+str(i)+"\n")
				i = i + 1
			else:
				save_exists = False
		except:
			save_exists = False


# show new file entry, with save option
def new_save():
	# clear console using native ti_system module
	disp_clr()

	# write our own input so we can have hotkeys
	print("\033[1mPress [mode] for newline, [del] for backspace, [Enter] to save\033[0m\n\n")

	text_editor()


# a dict class for dynamic retrieval of calc outputs from given keynum
Dict = {154:'a', 155:'b', 156:'c', 157:'d', 158:'e', 159:'f', 160:'g', 161:'h', 162:'i', 163:'j', 164:'k', 165:'l', 166:'m', 167:'n', 168:'o', 169:'p', 170:'q', 171:'r', 172:'s', 173:'t', 174:'u', 175:'v', 176:'w', 177:'x', 178:'y', 179:'z', 153:' ', 128:'"', 198:':', 140:'?', 183:'sin', 185:'cos', 187:'tan', 132:'^', 189:'²', 139:',', 133:'(', 134:')', 131:'/', 193:'log', 149:'7', 150:'8', 151:'9', 146:'4', 147:'5', 148:'6', 143:'1', 144:'2', 145:'3', 141:'.', 140:'-', 130:'*', 129:'-', 128:'+', 184:'sin⁻¹', 186:'cos⁻¹', 188:'tan⁻¹', 181:'π', 190:'√', 152:'EE', 236:'{', 237:'}', 239:'e', 194:'10^', 249:'u', 250:'v', 251:'w', 12:'rcl', 238:'i', 135:'[', 136:']'} 
Reverse = {v: k for k, v in Dict.items()}

# simple listener for keypress and action.
note = ""
def text_editor():
	global note
	
	try:
		keypress = int(wait_key())
	
		# on enter press
		if (keypress == 5):
			# ti only lets us store lists that are all type "int"

			# for each character in the note, replace it with it's integer value
			note_list = [Reverse[str(char)] for char in str(note)]

			LastExisted = True
			i = 0

			while (LastExisted == True):
				try:
					if (recall_list("GTE"+str(i))):
						i = i + 1
					else:
						LastExisted = False
						disp_clr()

						store_list("GTE"+str(i), note_list)
						print("\n\nSaved note as GTE"+str(i))
				except:
					LastExisted = False
                                        disp_clr()
					
					print("\n\nSaved note as GTE"+str(i))
                                        store_list("GTE"+str(i), note_list)
						

		# del key press
		elif (keypress == 10):
			note_chars = list(str(note))
			note_chars[len(note_chars)-1] = ""
			note = "".join(note_chars)

			# clear console using native ti_system module
			disp_clr()

			print("\033[1mPress [mode] for newline, [del] for backspace, [Enter] to save\033[0m\n\n")

			print(str(note))
			text_editor()
	
		# on mode press
		elif (keypress == 69):
			note = str(note) + "\n"
			# clear console using native ti_system module
			disp_clr()

			print("\033[1mPress [mode] for newline, [del] for backspace, [Enter] to save\033[0m\n\n")
			print(str(note))
			text_editor()

		# if key is not hotkey, print its value to the console
		else:
			if (Dict[int(keypress)]):
				note = str(note)+Dict[int(keypress)]
				
			# clear console using native ti_system module
			disp_clr()

			print("\033[1mPress [mode] for newline, [del] for backspace, [Enter] to save\033[0m\n\n")
			print(str(note))
			text_editor()
	except Exception as error:
		print(error)
		

# hack common naming structure so we can search vars
def search_saves():
        disp_clr()
        print("\033[1mTI_GTE: SEARCH\033[0m\n\n")

        inp = input("Enter search: ")

        # iterate over all saved notes and check if term is in them
        i = 0
	save_exists = True

	while (save_exists == True):
		try:
			if (recall_list("GTE"+str(i))):
				i = i + 1
			else:
				save_exists = False
		except:
			save_exists = False

        num_search = [Reverse[str(char)] for char in str(inp)]
        joined_search = "".join(str(num_search))
	results = False

	disp_clr()
	print("Searching...")
	time.sleep(1)
	disp_clr()
	print("\033[1mTI_GTE: SEARCH\033[0m\n\n")

        for x in range(i):
                save = [int(val) for val in recall_list("GTE"+str(x))]
                joined_save = "".join(str(save))
		letter_save = [Dict[int(char)] for char in recall_list("GTE"+str(x))]

		preview = ""
		
		if (len(letter_save) >= 7):
			for index in range(7):
				preview = preview+letter_save[index]
		else:
			for index in range(len(letter_save)):
				preview = preview+letter_save[index]


                if (joined_search in joined_save):
			results = True
			# output search results
                        print(str(x+1)+". GTE"+str(x)+": "+preview+"\n")

	if (results == False):
		print("\nWe couldn't find a note containing that term.")

	open_prompt("Enter sel. num to open: ", i)


def open_prompt(msg, i):
	entry = input("\n\n"+msg)

	if (((int(entry)-1) > i) or (int(entry) < 0)):
		open_prompt("Invalid entry. Try again: ", i)
	else:
		disp_clr()
		print("\033[1mTI_GTE: OpenFile\033[0m\n\n")

		readable_file = [Dict[int(char)] for char in recall_list("GTE"+str(int(entry)-1))]
		print("".join(readable_file))


opt_menu("Enter sel. num. ")
		

