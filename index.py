"""
1. Escreva um programa que pergunte a distância que
um passageiro deseja percorrer em km. Calcule o preço
da passagem, cobrando 

R$ 0,50 por km para viagens de até 200 km e 

R$ 0,45 para viagens mais longas.

"""

distância = int(input("Qual  a distância que um passageiro deseja percorrer em km: "))

if distância <= 200:
    valor1 = distância * 0.50
    print("Você irá pagar", valor1, "reais")
else:
    valor2 = distância * 0.45
    print("Você irá pagar", valor2, "reais")
