k = float(input('Digite a quantidade de km percorridos:'))
d = int(input('Digite a quantidade de dias que voce ficou com o carro:'))
kr = (k * 0.15) + (d * 60)
print('O total a se pagar pelo carro alugado e de {:.2f} reais ! '.format(kr))
