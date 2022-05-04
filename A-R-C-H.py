# CREATED BY ARCH0ZZ
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
BLACK = '\033[30m'

import requests
import os
import time

os.system("clear")

print(BLUE+"╭━━━╮╱╱╭━━━╮╱╭━━━╮╱╱╭╮╱╭╮")
print(GREEN+"┃╭━╮┃╱╱┃╭━╮┃╱┃╭━╮┃╱╱┃┃╱┃┃")
print(MAGENTA+"┃┃╱┃┃╱╱┃╰━╯┃╱┃┃╱╰╯╱╱┃╰━╯┃")
print(CYAN+"┃╰━╯┣━━┫╭╮╭┻━┫┃╱╭┳━━┫╭━╮┃")
print(YELLOW+"┃╭━╮┣━━┫┃┃╰┳━┫╰━╯┣━━┫┃╱┃┃")
print(RED+"╰╯╱╰╯╱╱╰╯╰━╯╱╰━━━╯╱╱╰╯╱╰╯")
print("")
print(MAGENTA+"####DOXXED NUM#####")
a = int(input("1.-INFORMACION DE UN NUMERO TELEFONICO \n Arch0zz~¢ "))

api_key = 'c4bc3b229e87a5ad428aee9ddc2180ac'

number = int(input(CYAN+"NUMERO TELEFONICO = "+RESET))

data = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api_key, number))

for key, value in data.json().items():

    print("%s: %s" % (key, value))
print("")
print(CYAN+"CHILE NO SIRVE EL LOCATION  NI URUGUAY O PARAGUAY")
print("")

print(GREEN+"============================")
print(GREEN+"|     Created By Arch0zz   | ")
print(GREEN+"============================")
print(GREEN+"|     TIK TOK: arch0zz     |")
print(GREEN+"============================")
print(GREEN+"|    TELEGRAM: arch0zz     |")
print(GREEN+"============================")
print(GREEN+"|    LIMITE DE DOXXEO:100  |")
print(GREEN+"============================")
