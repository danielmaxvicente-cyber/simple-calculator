resposta = "y"
while resposta == "y":
    num1 = int(input("What is your first number?"))
    num2 = int(input ("What is your second number?"))
    operacao = input("enter your operation")
    soma = (num1+num2)
    subtracao = (num1-num2)
    multiplicacao = (num1*num2)
    divisao = (num1/num2)
    if operacao == "+" :
        print("your result is" ,soma)
    elif operacao == "-" :
        print("your result is" ,subtracao)
    elif operacao == "*" :
        print("your result is" ,multiplicacao)
    elif operacao == "/" :
        print("your result is" ,divisao)

    resposta = input("Do you want to do another calculation? (y/n): ")
print("See you!")