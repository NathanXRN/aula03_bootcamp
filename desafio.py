CONSTANTE_BONUS = 1000

# 1. Solicita ao usuário que digite seu nome.

nome_valido = False 
salario_valido = False 
bonus_valido = False 

while nome_valido is not True:
    try:
        nome_usuario = input("Digite o seu nome: ")

        if nome_usuario.isdigit():
            raise ValueError("Você digitou seu nome errado!")

        elif len(nome_usuario) == 0:
            raise ValueError("Você não digitou nada!")
        
        elif any(char.isdigit() for char in nome_usuario):
            raise ValueError("O nome não deve conter números.")

        else:
            nome_valido = True 
            print("Nome válido = ", nome_usuario)

    except ValueError as e:
        print(f"Erro: {e}")
# 2. Solicita ao usuário que digite o valor do seu salário.
# Converte a entrada para um número de ponto flutuante

while salario_valido is not True:

    try:
        salario = float(input("Digite o valor do salario: "))

        if salario <= 0:
            raise ValueError("Salário tem que ser positivo!")

        else:
            salario_valido = True
            print("Salário Válido: ", salario)

    except ValueError:
        print("Entrada inválida, Por favor digite só números!")


# 3. Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

while bonus_valido is not True:

    try:
        bonus = float(input("Digite o valor do bônus: "))

        if bonus <= 0:
            raise ValueError("Bônus tem que ser positivo!")

        else:
            bonus_valido = True
            print("Bônus Válido: ", bonus)
            
    except ValueError:
        print("Entrada inválida, Por favor digite apenas números")


# 4. Calcule o valor do bônus final 

valor_do_bonus = round((CONSTANTE_BONUS + salario * bonus),2)


# 5. Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus.

print(f"O usuário {nome_usuario} possui um bônus de R${valor_do_bonus} reais.")