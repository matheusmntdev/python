# ------------------------------------------------------------------------------
# Jogo de Adivinhação
# ------------------------------------------------------------------------------
import random

numero = random.randint(1, 100)
tentativas = []
adivinhou = False

while not adivinhou: 
    palpite = int(input("Digite seu palpite (1 a 100): "))
    tentativas.append(palpite)
    
    if palpite == numero:
        print("Parabéns! Você acertou!")
        adivinhou = True
    elif palpite < numero:
        print("Maior")
    else:
        print("Menor") 

print("\nHistórico de tentativas:", tentativas)
print("Total de tentativas:", len(tentativas))

# ------------------------------------------------------------------------------
# Calculadora de Média com Aprovação
# ------------------------------------------------------------------------------
notas = []
nota = 0

while nota != -1: 
    nota = float(input("Digite uma nota (ou -1 para encerrar): "))
    if nota != -1:
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota deve estar entre 0 e 10") 

if notas:
    media = sum(notas) / len(notas)
    print(f"\nMédia: {media:.2f}")
    if media >= 7:
        print("Aprovado")
    elif media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")
else:
    print("Nenhuma nota inserida")
    
# ------------------------------------------------------------------------------
# Filtro de Números Pares e Ímpares
# ------------------------------------------------------------------------------
numeros = []
pares = []
impares = []

numero = None
while numero != 0:
    try:
        numero = int(input("Digite um número (0 para encerrar): "))
        if numero != 0:
            numeros.append(numero)
            if numero % 2 == 0:
                pares.append(numero)
            else:
                impares.append(numero)
    except ValueError:
        print("Digite um número válido")

print("\nLista completa:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)

# ------------------------------------------------------------------------------
# Simulador de Caixa Eletrônico
# ------------------------------------------------------------------------------

notas_disponiveis = {100: 10, 50: 10, 20: 10, 10: 10} 
 
valor = int(input("Digite o valor a sacar (múltiplo de 10): "))

if valor <= 0:
    print("Valor deve ser positivo")
elif valor % 10 != 0:
    print("Valor deve ser múltiplo de 10")
else: 
    notas_usadas = {100: 0, 50: 0, 20: 0, 10: 0}
    resto = valor
    
    for nota in notas_usadas:
        while resto >= nota and notas_disponiveis[nota] > 0:
            resto -= nota
            notas_usadas[nota] += 1
            notas_disponiveis[nota] -= 1
    
    if resto == 0:
        print("\nNotas fornecidas:")
        for nota, quantidade in notas_usadas.items():
            if quantidade > 0:
                print(f"{quantidade} nota(s) de R${nota}")
    else:
        print("Não há notas suficientes para o saque")