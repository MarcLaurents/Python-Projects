from random import randint

jogada = ['pedra', 'papel', 'tesoura']

while True:
  computador = jogada[randint(0,2)]
  jogador = input('pedra, papel or tesoura? *ou terminar jogo* ').lower()
  if (jogador == 'terminar jogo'):
    print('O jogo terminou.')
    break
  elif (jogador == computador):
    print('Empate!')
  elif (jogador == 'pedra'):
    if (computador == 'papel'):
      print('Voce Perdeu!', computador, ' vence ', jogador)
    else:
      print('Voce Ganhou!', jogador, ' vence ', computador)
  elif (jogador == 'papel'):
    if (computador == 'tesoura'):
      print('Voce Perdeu!', computador, ' vence ', jogador)
    else:
      print('Voce Ganhou!', jogador, ' vence ', computador)
  elif (jogador == 'tesoura'):
    if (computador == 'pedra'):
      print('Voce Perdeu!', computador, ' vence ', jogador)
    else:
      print('Voce Ganhou!', jogador, ' vence ', computador)
  else:
    print('Confira se digitou certo...')