#a variavel para o while não necessita de um input.
#ele apenas vai decidir a condição inicial do while.


resposta = "0"

#a condição da resposta é 42, se não ele mantem o loop até acertar o valor.

while (resposta != "42"):

#sempre vai seguir a condição até voce acetar a resposta.

    resposta = input(" Qual a resposta da vida erra não CARAI!? ")

#enquanto voce não atingir a condição, o loop continuará, quando acetar o laço sai. te apresentando um print de finalização.

print(" Acertou miseravi! ")


#-------------------------------------------------------------------------------------------------------------------------------------

print (" Digite 5 numeros: ")

x = 1
n = 2

lista = []

while x <= 25:

     n = int(input('Digite um número: [ %s ]: ' % x))

     if n % 2 == 1:

        lista.append(n)

        x += 1

     else:

            print(" erro ")