#Programa que calculo o tempo e a velocidade média entre dois pontos.
distancia = int(input('Insira a distância a ser percorrida em Km: '))
velocidade = int(input('Insira a velocidade média de deslocamento em Km/h: '))
tempo = distancia/velocidade
print(f'O tempo médio para se chegar no destino, tendo percorrido a distância numa velocidade média de {velocidade/3.6:.1f} metros por segundo é de: {tempo:.1f} horas.')
