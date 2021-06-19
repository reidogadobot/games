def ppt():
  from random import randint
  import time
  print('[*]OLÁ, SEJA BEM-VINDO AO PPT (θ‿θ)')
  jogador = str(input('[*]PARA COMEÇAR, APERTE ENTER ʘ‿ʘ'))
  print('═' * 37)
  saldo = 50
  aposta = 0
  while True:
    itens = ["PEDRA⛰️", "PAPEL📃", "TESOURA✂️"]
    computador = randint(0,2)
    if saldo <= 0:
      print('❌VOCÊ NÃO TEM MAIS DINHEIRO PRA APOSTAR❌')
      break
    print(f'''VOCÊ TEM R${saldo}

SUAS OPÇÕES:           
[ 0 ] PEDRA ✊
[ 1 ] PAPEL ✋
[ 2 ] TESOURA ✌️
[ 3 ] SAIR ❌''')
    jogador = int(input('ESCOLHA A SUA OPÇÃO: '))
    if jogador != 0 and jogador != 1 and jogador != 2 and jogador != 3:
      print('❌JOGADA INVÁLIDA ❌') 
      break
    time.sleep(1)
    if jogador == 3:
      print('SAINDO...')
      time.sleep(1)
      break
    else:
      aposta = int(input('QUANTO QUER APOSTAR? R$'))
      if aposta > saldo:
        print('❌VOCÊ N TEM ESSE VALOR PRA APOSTAR❌')
        break
      print(f'VOCÊ FEZ UMA APOSTA NO VALOR DE R${aposta:.2f}')
      if jogador != computador:
        saldo -= aposta
      print('═' * 37)
      print('JO')
      time.sleep(1)  
      print('KEN')
      time.sleep(1)
      print('PÔÔÔ!!')
      print('═' * 37)
      print('VOCÊ ESCOLHEU {}'.format(itens[jogador]))
      print('O COMPUTADOR JOGOU {}'.format(itens[computador]))
      print(' ')
      if jogador == 0:
        if computador == 0:
          print('EMPATE 😖')
        if computador == 1:
          print('VOCÊ PERDEU ☹️')
          print(f'❌VOCÊ PERDEU R${aposta:.2f}')
        if computador == 2:
          print('VOCÊ GANHOU 🙂')
          saldo += (aposta * 2)
          print(f'😳🙌VOCÊ GANHOU R${aposta * 2:.2f}')
      elif jogador == 1:
        if computador == 0:
          print('VOCÊ GANHOU 🙂')          
          saldo += (aposta * 2)
          print(f'😳🙌VOCÊ GANHOU R${aposta * 2:.2f}')
        if computador == 1:
          print('EMPATE 😖')
        if computador == 2:
          print('VOCÊ PERDEU ☹️')          
          print(f'❌VOCÊ PERDEU R${aposta:.2f}')
      elif jogador == 2:
        if computador == 0:
          print('VOCÊ PERDEU ☹️')
          print(f'❌VOCÊ PERDEU R${aposta:.2f}')
        if computador == 1:
          print('VOCÊ GANHOU 🙂')
          saldo += (aposta * 2)
          print(f'😳🙌VOCÊ GANHOU R${aposta * 2:.2f}')
        if computador == 2:
          print('EMPATE 😖')
      print(f'💵VOCÊ TEM R${saldo:.2f}')
      print('═' * 37)
      time.sleep(1)
      jogador = str(input('Quer jogar novamente? [S/N]: ')).upper()
      if jogador == 'N':
        print('saindo...')
        time.sleep(2)
        break