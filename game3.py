def amongus():
  import random
  from time import sleep
  tripulantes = ["AZUL", "VERMELHO", "PRETO", "VERDE", "BRANCO", "AMARELO", "ROSA", "ROXO", "CIANO", "CINZA"]
  impostor = random.choice(tripulantes)
  print('OLÁ, SEJA BEM VINDO AO AMONG US (≧▽≦)')
  jogador = str(input('PARA COMEÇAR, APERTE ENTER ʘ‿ʘ'))
  print('''`.      　。　　　　•　    　ﾟ　　。
　　.　　　.　　　  　　.　　　　　。　　   。　.
　.　　      。　        ඞ   。　    .    •
•               。　.
　 　　。　　 　　　　ﾟ　　　.　      　　　.
,　　　　.                  .`''')
  tripulantes.remove(impostor)
  random.shuffle(tripulantes)
  while True:
    print('=' * 27)
    print('TRIPULANTES VIVOS:') 
    for c in tripulantes:
      print(f'[*]{c}')
    print(f'[*]{impostor}')
    jogador = str(input('QUEM VOCÊ ACHA QUE É O IMPOSTOR: ')).upper()
    print('=' * 27)
    if jogador == "AZUL":
      if jogador in tripulantes:
        print('O AZUL N ERA O IMPOSTOR❌')
        sleep(1)
      else:
        print('O AZUL ERA O IMPOSTOR👺🔪')
        print('PARABÉNS, VOCÊ GANHOU 🎉')
        break
      tripulantes.remove("AZUL")
      print('VOCÊ REMOVEU UM INOCENTE😔')
    if jogador == "VERMELHO":
      if jogador in tripulantes:
        print('O VERMELHO NÃO ERA O IMPOSTOR❌')
        sleep(1)
      else:
        print('O VERMELHO ERA O IMPOSTOR👺🔪')
        print('PARABÉNS, VOCÊ GANHOU 🎉')
        break
      tripulantes.remove("VERMELHO")
      print('VOCÊ REMOVEU UM INOCENTE😔')
    if jogador == "PRETO":
      if jogador in tripulantes:
        print('O PRETO NÃO ERA O IMPOSTOR❌')
        sleep(1)
      else:
        print('O PRETO ERA O IMPOSTOR👺🔪')
        print('PARABÉNS, VOCÊ GANHOU 🎉')
        break
      tripulantes.remove("PRETO")
      print('VOCÊ REMOVEU UM INOCENTE😔')
    if jogador == "VERDE":
      if jogador in tripulantes:
        print('O VERDE NÃO ERA O IMPOSTOR❌')
        sleep(1)
      else:
        print('O VERDE ERA O IMPOSTOR👺🔪')
        print('PARABÉNS, VOCÊ GANHOU 🎉')
        break
      tripulantes.remove("VERDE")
      print('VOCÊ REMOVEU UM INOCENTE😔')
    if jogador == "BRANCO":
      if jogador in tripulantes:
        print('O BRANCO NÃO ERA O IMPOSTOR❌')
        sleep(1)
      else:
        print('O BRANCO ERA O IMPOSTOR👺🔪')
        print('PARABÉNS, VOCÊ GANHOU 🎉')
        break
      tripulantes.remove("BRANCO")
      print('VOCÊ REMOVEU UM INOCENTE😔')
    if jogador == "AMARELO":
      if jogador in tripulantes:
        print('O AMARELO NÃO ERA O IMPOSTOR❌')
        sleep(1)
      else:
        print('O AMARELO ERA O IMPOSTOR👺🔪')
        print('PARABÉNS, VOCÊ GANHOU 🎉')
        break
      tripulantes.remove("AMARELO")
      print('VOCÊ REMOVEU UM INOCENTE😔')
    if jogador == "ROSA":
      if jogador in tripulantes:
        print('O ROSA NÃO ERA O IMPOSTOR❌')
        sleep(1)
      else:
        print('O ROSA ERA O IMPOSTOR👺🔪')
        print('PARABÉNS, VOCÊ GANHOU 🎉')
        break
      tripulantes.remove("ROSA")
      print('VOCÊ REMOVEU UM INOCENTE😔')
    if jogador == "ROXO":
      if jogador in tripulantes:
        print('O ROXO NÃO ERA O IMPOSTOR❌')
        sleep(1)
      else:
        print('O ROXO ERA O IMPOSTOR👺🔪')
        print('PARABÉNS, VOCÊ GANHOU 🎉')
        break
      tripulantes.remove("ROXO")
      print('VOCÊ REMOVEU UM INOCENTE😔')
    if jogador == "CIANO":
      if jogador in tripulantes:
        print('O CIANO NÃO ERA O IMPOSTOR❌')
        sleep(1)
      else:
        print('O CIANO ERA O IMPOSTOR👺🔪')
        print('PARABÉNS, VOCÊ GANHOU 🎉')
        break
      tripulantes.remove("CIANO")
      print('VOCÊ REMOVEU UM INOCENTE😔')
    if jogador == "CINZA":
      if jogador in tripulantes:
        print('O CINZA NÃO ERA O IMPOSTOR❌')
        sleep(1)
      else:
        print('O CINZA ERA O IMPOSTOR👺🔪')
        print('PARABÉNS, VOCÊ GANHOU 🎉')
        break
      tripulantes.remove("CINZA")
      print('VOCÊ REMOVEU UM INOCENTE😔')
      sleep(3)
    morreu = random.choice(tripulantes)
    tripulantes.remove(morreu)
    sleep(2)
    print('=' * 27)
    print(f'{morreu} FOI MORTO☠️')
    sleep(2)
    if len(tripulantes) < 3:
      print('❌VOCÊ PERDEU❌')
      print(f'O IMPOSTOR ERA O {impostor}👺🔪')
      break