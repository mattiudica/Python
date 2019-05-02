import string
import secrets
# This program generates 3 kind of key you would usually need for
# operating an ATM (in Argentina). There are other shorter and more secure ways tho, 
# like tokenHex or uuid

def validateInput():
	while True:
		try:
			sel_tipo = int(input("Select:\n1)3-letter key(ABC)\n2)4-digit key(NUM)\n3)12-character key(ABC-NUM-SYM)\n"))
			if sel_tipo in range(1,4):
				return(sel_tipo)
				break
			else:
				print("Options 1-2-3 available only")
		except:
			print("Error in input (only takes numbers)")
			exit()

#Saving function return into a variable
inputValue=validateInput()

#Generating key 
def keyGen():
	#ABC
	if inputValue == 1:
		alphabet = string.ascii_letters
		return''.join(secrets.choice(alphabet)for i in range(1,4))
	#NUM
	elif inputValue == 2:
		alphabet = string.digits
		return''.join(secrets.choice(alphabet)for i in range(1,5))
	#ABC-NUM-SYM
	elif inputValue == 3:
		alphabet = string.ascii_letters + string.digits + string.punctuation
		return ''.join(secrets.choice(alphabet) for i in range(1,13))
#Saving function return into a variable
keyValue=keyGen()
#Output
print(keyValue)

























 
	