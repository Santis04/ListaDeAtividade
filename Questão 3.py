#Questão 3
nome = input("Digite seu nome:")
primeira_letra = nome[0]  # Captura a primeira letra
ultima_letra = nome[-1]  # Captura a última letra
print(f"A primeira letra do seu nome é: {primeira_letra}")
print(f"A última letra do seu nome é: {ultima_letra}")


idade = int(input("Digite sua idade:"))
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
    
altura = float(input("Digite sua altura em centimetros:"))
print(f"Sua altura é: {altura} cm")

peso = float(input("Digite seu peso em kg:"))
print(f"Seu peso é: {peso} kg")

