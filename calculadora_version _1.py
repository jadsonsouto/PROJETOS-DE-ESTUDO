
#CALCULADORA
"\n"
soma="+"
sub="-"
multi="*"
div="/"


print("Vamos Calcular!!!\n")

print("Digite o primeiro número: ")
a=int(input())

print("Digite o operador")
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
    
else:
    print("Digite um operador válido")
    operador=input()


print("Digite o segundo número: ")
b=int(input())




if operador == "+":
    print("O resultado é: ", a+b)

if operador == "-":
    print("O resultado é: ", a-b)

if operador == "*":
    print("O resultado é: ", a*b)

if operador == "/":
    print("O resultado é: ", a/b)




