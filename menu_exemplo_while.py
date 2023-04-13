#Será definido qual opção o cliente ira colocar, se for entre 0 ou 5 o programa não ira funcionar.
op = -1

#definimos o loop do programa para 4 opção.

while op != 4:

#tela aonde o programa irá rodar as informações de escolha.

    print(" Selecione a opção do Programa: ")

    print(" \n Roda programa 1 ")
    print(" Roda programa 2 ")
    print(" Roda programa 3 ")
    print(" ou Sair do programa ")

#Definimos o input aonde o cliente ira escolher a opção que deseja.

    op = int(input(" \n Informe a opção: "))

#Na escolha da opção 1 será exibido o programa assim para os demais.

    if op == 1:

        print(" Rodando programa 1 \n ")

    elif op == 2:

        print(" Rodando programa 2 \n ")

    elif op == 3:

        print(" Rodando programa 3 \n ")

#Caso selecione a opção 4 ele ira sair do programa, caso coloque um outro valor, ira seguir o loop até escolher a opção certa.

print( " Ok, programa encerrado ")