#Faça um programa que peça uma nota, entre zero e dez
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

valido=False
while valido==False:
    valor=input("Digite o valor")
    valornumero=int(valor)   
    valido=valornumero>0 and valornumero<10
    if valido==False:
        print("Invalido")