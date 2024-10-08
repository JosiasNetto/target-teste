import json

#funcao que calcula os maiores, menores e a media dos valores do faturamento
def calculoValores(faturamentos):
    maior = float('-inf');
    menor = float('inf');
    media = 0
    diasSuperior= 0;
    diasDescartados = 0;

    for i in range(len(faturamentos)):
        if(faturamentos[i]['valor'] != 0):
            if(faturamentos[i]['valor'] > maior):
                maior = faturamentos[i]['valor'];
            if(faturamentos[i]['valor'] < menor):
                menor = faturamentos[i]['valor'];
            
            media += faturamentos[i]['valor'];
        else:
            diasDescartados += 1;

    media = media / len(faturamentos) - diasDescartados;

    for j in range(len(faturamentos)):
        if(faturamentos[j]['valor'] > media):
            diasSuperior += 1;

    return maior, menor, diasSuperior;

#importando o json
with open("/home/josiasnetto/faculdade/estagios/target/dados.json", 'r') as file:
    faturamentos = json.load(file)
maiorValor, menorValor, diasSuperior = calculoValores(faturamentos)

#Printando os valores desejados
print(f"O maior valor é: {maiorValor:.2f}. O menor valor é: {menorValor:.2f}. O número de dias que passaram do valor da média foi: {diasSuperior}")
            

