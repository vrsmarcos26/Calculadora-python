#calculadora

def add(x,y):
    return x+y
def subtrai(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def potencia(x,y):
    return x**y
def raiz(x):
    return x ** (1/2)

#progrma principal da calculadora

while True:
    print('''Opções:
            1. soma
            2. subtração
            3. multiplicação
            4. divisão
            5. potência
            6. raiz quadrada
            7. sair''')

    op = int(input("Digite uma opção: "))

    if op == 7:
        break
        
    z = int(input("Digite o primeiro operando: "))

    if op == 6:
        print("A sua resposta é: ")
        print(raiz(z))

    w = int(input("Digite o segundo operando: "))

    if op == 1:
        print("A sua resposta é: ")
        print(add(z,w))
    if op == 2:
        print("A sua resposta é: ")
        print(subtrai(z,w))
    if op == 3:
        print("A sua resposta é: ")
        print(multiply(z,w))
    if op == 4:
        print("A sua resposta é: ")
        print(divide(z,w))
    if op == 5: 
        print("A sua resposta é: ")
        print(potencia(z,w))
    if op == 6:
        print("A sua resposta é: ")
        print(raiz(z,w))