n1 = float(input("Entre com o 1º número: "))
n2 = float(input("Entre com o 2º número: "))
n3 = float(input("Entre com o 3º número: "))

maior = n1

if n2 >= n1 and n2 >= n3:
 maior = n2

if n3 >= n1 and n3 >= n2:
 maior = n3
menor = n1

if n2 <= n1 and n2 <= n3:
 menor = n2

if n3 <= n2 and n3 <= n1:
 menor = n3

print(f"O maior valor é {maior}.")
print(f"O menor valor é {menor}.")