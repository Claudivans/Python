# Pega dados do usuario e retorna em duma frase
print("Qual seu nome? ")
nome = input()

print(f'Seja bem-vindo(a) {nome}')

print("Qual sua idade? ")
idade = input()

print(f'O  {nome} tem {idade} anos')

print(f'O(a) nome nasceu em {2020 - int(idade)}')
