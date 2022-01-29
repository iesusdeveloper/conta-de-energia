import math
atual = float(input('Digite a Leitura Atual: '))
anterior = float(input('Digite a Leitura anterior: '))
kwh = float(input('Digite o valor Kwh: '))
publica = float(input('Digite o valor da iluminação pública: '))
bandeira = float(input('Digite o valor da bandeira tarifária: '))
calculo = ((atual - anterior) * kwh) + publica + (bandeira * (atual-anterior))
print('O valor é R${:.2f}'.format(calculo))