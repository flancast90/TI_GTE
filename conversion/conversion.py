import sys

Dict = {154:'a', 155:'b', 156:'c', 157:'d', 158:'e', 159:'f', 160:'g', 161:'h', 162:'i', 163:'j', 164:'k', 165:'l', 166:'m', 167:'n', 168:'o', 169:'p', 170:'q', 171:'r', 172:'s', 173:'t', 174:'u', 175:'v', 176:'w', 177:'x', 178:'y', 179:'z', 153:' ', 128:'"', 198:':', 140:'?', 183:'sin', 185:'cos', 187:'tan', 132:'^', 189:'²', 139:',', 133:'(', 134:')', 131:'/', 193:'log', 149:'7', 150:'8', 151:'9', 146:'4', 147:'5', 148:'6', 142:'0', 143:'1', 144:'2', 145:'3', 141:'.', 140:'-', 130:'*', 129:'-', 128:'+', 184:'sin⁻¹', 186:'cos⁻¹', 188:'tan⁻¹', 181:'π', 190:'√', 152:'EE', 236:'{', 237:'}', 239:'e', 194:'10^', 249:'u', 250:'v', 251:'w', 12:'rcl', 238:'i', 135:'[', 136:']'} 
Reverse = {v: k for k, v in Dict.items()}

f = open("OUT/transfer.py", "w")
f.write("")
f.close()

print("\nInitializing...")
			
f = open("OUT/transfer.py", "a")
f.write("from ti_system import *")
f.write("\ni = 0")
f.write("\nsave_exists = True")
f.write("\nwhile (save_exists == True):")
f.write("\n	try:")
f.write("\n		if (recall_list('GTE'+str(i))):")
f.write("\n			i = i + 1")
f.write("\n		else:")
f.write("\n			save_exists = False")
f.write("\n	except:")
f.write("\n		save_exists = False")
f.close()
		
print("Done.")

for i in range(len(sys.argv)):
	if (len(sys.argv) < 1):
		print("Error: you must specify the files to convert as arguments!")
	else:	
		if (i >= 1):
			
			print("\nStarting conversion of file "+sys.argv[i]+"...")
			
			n = 100
			f = open(sys.argv[i], "r")
			txt = f.read()
			
			# quick patch since converting '\n' can throw it off
			# TODO: find and replace all unknown characters
			for item in txt:
				if item not in Dict:
					txt = txt.replace(item, '')
			
			write = [txt[index : index + n] for index in range(0, len(txt), n)]	
			
			for index in range(len(write)):
				note_list = [Reverse[str(char)] for char in str(write[index].lower())]
			
				print("\nStoring file... ")
				f = open("OUT/transfer.py", "a")
				f.write("\n\nprint('Going to save file as GTE'+str(i))")
				f.write("\n\nstore_list('GTE'+str(i), "+str(note_list)+')')
				f.write("\nprint('Saved.')")
				f.write("\ni=i+1")
				f.close()
				
				print("Done.")
				
				
print("\nConversion complete!")
			
			
			
		
