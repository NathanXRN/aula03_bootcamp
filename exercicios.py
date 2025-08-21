# 1. Verificação de Qualidade de Dados 
# Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para 'quantidade' e 'preço'.
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

quantidade = 15
preco = 29.85

if quantidade > 0 and preco > 0:
    print("Dados Válidos")
else:
    print("Dados Inválidos")

# 2. Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT.
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'.
# Considerando que Temperautra < 18ºC é baixa.
# Temperatura >= 18ºC e <= 26ºC é Normal.
# Temperatura > 26ºC é Alta.

temperatura = 27

if temperatura < 18:
    print("Baixa")

elif 18 <= temperatura <= 26:
    print("Normal")

else:
    print("Alta")

# 3. Filtragem de Logs por Severidade 
# Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'.
# Dado um registro de log em formato de dicionário como 'log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'},
# escreva um program que imprima a mensagem se a severidade for 'ERROR'.

log = {'timestamp' : '2021-06-23 10:00:00',
       'level'     : 'ERROR',
       'message'   : 'Falha na conexão'}

if log['level'] == 'ERROR':
    print(log['message'])


# Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade = 25
email = 'usuarioteste@gmail.com'


if not 18 <= idade <= 65:
    print("Idade Fora do intervalo")

elif '@' not in email or '.' not in email:
    print("Email Inválido")

else:
    print("Dados de usuários válidos")
    

# Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

transacao = {
    'valor' : 12000,
    'hora'  : 20
}

if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
    print("Transação Suspeita!")

else:
    print("Transação Normal!")

# Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = "Nada é suficiente para quem considera pouco o suficiente"

palavras = texto.split(" ")

print(palavras)

contagem_de_palavras = {}

for palavra in palavras:
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] = +1
    else:
        contagem_de_palavras[palavra] = 1

print(contagem_de_palavras)

# Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

numeros = [15, 25, 35, 45, 55]

minimo = min(numeros)
maximo = max(numeros)

normalizado = [(x - minimo) / (maximo - minimo) for x in numeros]

print(normalizado)

# Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

usuarios = [
    {"nome": "Roberta", "email": "roberta@example.com"},
    {"nome": "Jorge", "email": ""},
    {"nome": "Rodrigo", "email": "rodrigo@example.com"}
]

usuarios_validos = []

for usuario in usuarios:
    if usuario["email"]:
        usuarios_validos.append(usuario)

print(usuarios_validos)

# Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

lista_numeros = [1, 12, 20, 25, 58, 18, 90]

lista_pares = []

for numeros in lista_numeros:
    if numeros % 2 == 0:
        lista_pares.append(numeros)

print(lista_pares)

# Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {"categoria": "eletrônicos", "valor": 3000},
    {"categoria": "livros", "valor": 500},
    {"categoria": "eletrônicos", "valor": 1200}
]

total_categoria = {}

for venda in vendas:
    categoria = venda["categoria"]
    valor     = venda["valor"]

    if categoria in total_categoria:
        total_categoria[categoria] += valor 
    else:
        total_categoria[categoria] = valor

print(total_categoria)

# Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

dados = []

entrada = ""

while entrada.lower() != "sair":
    entrada = input("Digite um valor (ou 'sair' para terminar): ")

# Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

numero = int(input("Digite um numero entre 1 e 10: "))

while numero < 1 or numero > 10:
    numero = int(input("Digite um valor válido: "))
    

# Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

pagina_atual  = 1
total_paginas = 10

while pagina_atual <= total_paginas:
    print(f"Processando página {pagina_atual} de {total_paginas}")

    pagina_atual += 1

print("Todas as páginas foram processadas")

# Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

tentativa_atual  = 1
limite_tentativa = 5

while tentativa_atual <= limite_tentativa:
    print(f"Tentativa de reconexão {tentativa_atual} de um limite de tentativas {limite_tentativa}")

    if False:
        print("Conexão sucedida!")
        break
    
    tentativa_atual += 1

else:
    print("Limite máximo de tentativas excedido!")

# Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

itens = [1, 2, 3, "parar", 4, 5]

i = 0 

while i < len(itens):
    if itens[i] == 'parar':
        print("Parada Encontrada, encerrando o processamento!")
        break
    print(f"Processando item: {itens[1]}")

    i += 1