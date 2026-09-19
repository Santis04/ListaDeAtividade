#Questão 4
while True:
    n = int(input("Digite o valor em reais: "))

    notas_100 = n // 100  
    resto = n % 100       

    notas_50 = resto // 50  
    resto = resto % 50      

    notas_10 = resto // 10  
    resto = resto % 10     

    notas_1 = resto // 1    
    print("Notas de 100:", notas_100)
    print("Notas de 50:", notas_50)
    print("Notas de 10:", notas_10)
    print("Notas de 1:", notas_1)

    continuar = input("Deseja calcular outro valor? (s/n): ").lower()
    if continuar != 's':
        break