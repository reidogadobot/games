from random import choice
from time import sleep
saldo = 100
while True:
  ítens = ["🍋", "🍇", "🍓"]
  slot1 = choice(ítens)
  slot2 = choice(ítens)
  slot3 = choice(ítens)
  if saldo <= 0:
    print('❌VOCÊ NÃO TEM MAIS DINHEIRO PRA JOGAR❌')
    break
  print('═' * 36)
  print('🎰GIRANDO🎰')
  sleep(2)
  print('┏═════════════════┓')
  print(f'   {slot1}  |  {slot2}  |  {slot3}    ʙʏ ʜᴜɴᴛᴇʀᴢɪɴ ©')
  print('┗═════════════════┛')
  if slot1 == slot2 and slot2 == slot3:
    print('🎉PARABÉNS, VOCÊ GANHOU🎉!')
    sleep(1)
    if slot1 and slot2 and slot3 == "🍋":
      print('VOCÊ GANHOU MIL REAIS💵')
      saldo += 1000
    elif slot1 and slot2 and slot3 == "🍇":
      print('VOCÊ GANHOU 500 REAIS💵')
      saldo += 500
    elif slot1 and slot2 and slot3 == "🍓":
      print('VOCÊ GANHOU 100 REAIS💵')
      saldo += 100
  else:
    print('❌VOCÊ PERDEU. MAIS SORTE NA PRÓXIMA VEZ☹️')
  saldo -= 5
  print(f'💵SALDO DISPONÍVEL: R${saldo:.2f}'.replace('.', ','))
  sleep(1)
  jogador = str(input('Deseja jogar novamente? [S/N]: ')).upper()
  if jogador == 'N':
    print('SAINDO...')
    print(f'VOCÊ SAIU DO CASSINO COM R${saldo:.2f}'.replace('.', ','))
    if saldo < 100:
      print('PERDEU DINHEIRO NO CASSINO OTÁRIO KKK')
    else:
      print('BOA CAMPEÃO, GANHOU UMA GRANA😳')
    break