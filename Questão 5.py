#Questão 5
t = int(input("Digite a quantidade total de segundos: "))

horas = t // 3600
resto = t % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas} horas, {minutos} minutos e {segundos} segundos")