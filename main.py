#importacões e modulos
from time import sleep
from game2 import ppt
from game3 import amongus
from game1 import cassino
from os import system
#---------------------#

print('''╔════════════════════════════════════════════╗
┃  OLÁ, SEJA BEM VINDO AO MENU DE GAMES ʘ‿ʘ  ┃   
╠════════════════════════════════════════════╣
┃[•]SUAS OPÇÕES:                               
║                          ㅤㅤ                                               ㅤ║
┃[ 1 ] CASSINO 🎰               ㅤㅤㅤㅤ            
║(GIRE UM CAÇA NÍQUEIS)  ㅤ            
┃[ 2 ] PPT 🎮                   ㅤㅤㅤㅤㅤㅤ               
║(PEDRA, PAPEL E TESOURA)                    
╚════════════════════════════════════════════╝''')
usr = int(input('DIGITE A SUA OPÇÃO: '))

if usr == 1: # cassino
  print('INICIANDO...')
  sleep(2)
  cassino()
if usr == 2: # ppt
  print('INICIANDO...')
  sleep(2)
  ppt()
if usr == 3:
	print('INICIANDO...')
	sleep(2)
	amongus()
	
print('▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄')
