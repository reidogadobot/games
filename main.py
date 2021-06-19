#importacões e modulos
from time import sleep
from game2 import ppt
from game3 import amongus
from game1 import cassino
from os import system
#---------------------#

print('''╔════════════════════════════════════╗
┃  OLÁ, SEJA BEM VINDO AO MENU DE GAMES ʘ‿ʘ ┃   
╠════════════════════════════════════╣
┃[•]SUAS OPÇÕES:                        ㅤㅤ                                 ㅤ║      
║                          ㅤㅤ                                                              ㅤ║
┃[ 1 ] CASSINO 🎰               ㅤㅤㅤㅤ                       ㅤㅤ ㅤㅤ║
║(GIRE UM CAÇA NÍQUEIS)  ㅤ                                        ㅤㅤ║      
┃[ 2 ] PPT 🎮                   ㅤㅤㅤㅤㅤㅤ                             ㅤㅤ║ 
║(PEDRA, PAPEL E TESOURA)                                     ㅤㅤㅤ║ 
╚════════════════════════════════════╝''')
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
