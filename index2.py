"""
2. Considerando que uma determinada escola possui
média 7 e que não há exame, efetuar a leitura de 3
notas de um aluno, calcular a média aritmética simples e
apresentar se o aluno está reprovado ou aprovado.

"""

nota1 = int(input("Coloque a sua primeira nota: "))
nota2 = int(input("Coloque a sua segunda nota: "))
nota3 = int(input("Coloque a sua terceira nota: "))

resultado = (nota1 + nota2 + nota3) / 3

if resultado >= 7:
    print("Você foi aprovado")
else:
    print("Você foi reprovado")

