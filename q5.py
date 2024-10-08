#Funcao que inverte a string
def inverteString(palavra):
    palavraInvertida = [];
    for i in range(len(palavra) - 1, -1, -1):
        palavraInvertida.append(palavra[i]);
    
    palavraInvertida = ''.join(palavraInvertida)
    print(palavraInvertida)

#Executando o codigo pedido
palavra = input("digite a palavra:")

#Caso queira digitar a sting no proprio codigo
#palavra = ''

inverteString(palavra)
