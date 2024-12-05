nome = input("Digite seu nome:")
print("Seu nome é: "+nome)

idade = int(input("Digite sua idade: "))
print("Sua idade é :"+str(idade))

if idade < 18:
    print(f"O {nome} é menor de idade")
elif idade == 18:
    print(f"O {nome} é maior de idade")
else:
    if idade < 30:
        print(f"O {nome} é um jovem adulto")
    elif idade < 60:
        print(f"O {nome} é adulto")
    else:
        print(f"O {nome} é um idoso")






