# Exercício Python 16: Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou cadeirante. 
# Escreva um programa que pergunta a situação do usuário 
# (se é idoso, se é gestante, se é cadeirante ou nenhum destes) 
# e diga se ele pode ter acesso a fila prioridade ou não.

print("Escolha sua situação")
print("1 - Idoso")
print("2 - Gestante")
print("3 - Cadeirante")
print("4 - Nenhum destes")

escolha = input("Digite o número correspondente a sua situação: ")

if escolha == "1": 
    print("Você pode ter acesso a fila de prioridade por ser idoso.")
elif escolha == "2": 
    print("Você pode ter acesso a fila de prioridade por ser gestante.")
elif escolha == "3":
    print("Você pode ter acesso a fila de prioridade por ser cadeirante.")
elif escolha == "4":
    print("Você não se encaixa em nenhuma das situações que dão acesso a fila de prioridade.")
else:
    print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")