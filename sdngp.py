import random
import string
import time
import os
import webbrowser
clear = lambda: os.system('cls')

print("Coded by imskidyo")
print("Discord Username: imskidyo")
print("Please wait 20 seconds")
webbrowser.open('https://youtube.com/@imskidyo?sub_confirmation=1')
webbrowser.open('https://discord.com/invite/QdPJmHfC6d')
time.sleep(20)
clear()

amount = int(input('Amount of nitro codes to generate: '))
value = 1
while value <= amount:
	code = "https://discord.gift/" + ('').join(
	    random.choices(string.ascii_letters + string.digits, k=16))
	f = open('Nitro Classic Codes.txt', "a+")
	f.write(f'{code}\n')
	f.close()
	print(f'Invalid | {code}')
	value += 1

	code = "https://discord.gift/" + ('').join(
	    random.choices(string.ascii_letters + string.digits, k=24))
	f = open('Nitro Boost Codes.txt', "a+")
	f.write(f'{code}\n')
	f.close()
	print(f'Invalid | {code}')
	value += 1
  
