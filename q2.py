#Input para que o usuario digite o numero
numero = int(input("Digite o numero desejado:"))

#Caso queira digitar direto no codigo
#numero = 1

#variaveis de auxilio
fiboSequencia = [0, 1]
fim = False;
existe = False

#Loop que vai gerando os numeros de Fibonacci ate que passe ou chegue no desejado
contador = 2;
while(fim == False):
    fiboSequencia.append(fiboSequencia[contador - 1] + fiboSequencia[contador - 2]);
    print(fiboSequencia[contador])
    if(fiboSequencia[contador] == numero):
        print("O número existe na sequência de Fibonacci")
        fim = True;
    
    elif(fiboSequencia[contador] > numero):
        print("O número não existe na sequência de Fibonacci")
        fim = True;

    contador += 1;
    



