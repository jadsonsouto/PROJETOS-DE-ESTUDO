print("Digite o primeiro número: ")
a=int(input())

print("Digite o operador")
operador=input()
   
while operador != "+" != "-" != "*" != "/":
    print("Digite um operador válido")
    operador=input()

if operador == "+":
    print("Digite o segundo número: ")
    b=int(input())
    print("O resultado é: ", a+b)


if operador == "-":
    print("Digite o segundo número: ")
    b=int(input())
    print("O resultado é: ", a-b)

if operador == "*":
    print("Digite o segundo número: ")
    b=int(input())
    print("O resultado é: ", a*b)

if operador == "/":
    print("Digite o segundo número: ")
    b=int(input())
    print("O resultado é: ", a/b)


print("Digite o segundo número: ")
b=int(input())

soma="+"
subtracao="-"
multiplicacao="*"
divisao="/"


if operador == "+":
    print("O resultado é: ", a+b)

if operador == "-":
    print("O resultado é: ", a-b)

if operador == "*":
    print("O resultado é: ", a*b)

if operador == "/":
    print("O resultado é: ", a/b)




