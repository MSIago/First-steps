"""Este programa é uma calculadora
Digite o primeiro valor, a operação que deseja, e o segundo valor
O programa mostrará o resultado"""
A = float(input("Insira o primeiro valor:"))
O = int(input("Insira a operação:\n1 para adição;\n2 para subitração;\n3 para multiplicação;\n4 para divisão:"))
if O == 1:
    B = float(input("Insira o segundo valor:"))
    R = A+B
    print("O resultado é:",R)
elif O == 2:
    B = float(input("Insira o segundo valor:"))
    R = A-B
    print("O resultado é:",R)
elif O == 3:
    B = float(input("Insira o segundo valor:"))
    R = A*B
    print("O resultado é:",R)
elif O == 4:
    B = float(input("Insira o segundo valor:"))
    R = A/B
    print("O resultado é:",R)