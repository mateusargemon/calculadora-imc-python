print(">>>>CALCULADORA DE IMC<<<<")
print()

# Inserimento de dados
peso=float(input("Insira seu peso [KG]: "))
altura=float(input("Insira sua altura [M]: "))
print()

# IMC do usuario
imc=peso/(altura**2)

# Faixa de peso ideal para a altura informada.
pesoMin=18.5*(altura**2)
pesoMax=24.9*(altura**2) 

# Classificacoes de IMC
classificacao=None
if imc<18.5:
    classificacao=("Baixo peso")
else:
    if (imc<25):
        classificacao=("Peso adequado")
    elif imc<30:
        classificacao=("Sobrepeso")
    elif imc<35:
        classificacao=("Obesidade grau I")
    elif imc<40:
        classificacao=("Obesidade grau II")
    else:
        classificacao=("Obesidade grau III")

# Exibicao de informacoes do usuario
print(f"Classificação: {classificacao}")
print(f"Altura: {altura:.2f}m")
print(f"Peso: {peso:.2f}kg")
print(f"IMC: {imc:.2f}")
print()

# Recomendacoes ao usuario
if classificacao=="Peso adequado":
    print(f"Você está no peso ideal.")
elif classificacao=="Baixo peso":
    print(f"Você deve engordar aproximadamente: {(pesoMin-peso):.2f}kg.")
else:
    print(f"Você deve emagrecer aproximadamente: {(abs(pesoMax-peso)):.2f}kg.")
        

# Faixa ideal de peso para o usuario
print()
print(f"Faixa ideal de peso: {pesoMin:.2f}kg. a {pesoMax:.2f}kg.\n"
      f"Peso médio ideal: {((pesoMin+pesoMax)/2):.2f}kg.")


