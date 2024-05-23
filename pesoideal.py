h = float (input("digite sua altura: "))
sexo = str (input("digite seu sexo: "))
if (sexo == "masculino"):
    peso_ideal_homem = (72.7*h)-58
    print (f"seu peso ideal é: {peso_ideal_homem:.2f} kg")
elif (sexo == "feminino"):
    peso_ideal_mulher = (62.1*h)-44.7
    print (f"seu peso ideal é: {peso_ideal_mulher:.2f} kg")
else:
    print ("digitou algo errado!")
    