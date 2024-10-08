#Calculo dos valores totais e porcentagens das cidades
def calculoValores(cidadesValores):
    total = 0;
    dicCidadesPorcentagens = {};
    for i in cidadesValores:
        total += cidadesValores[i];

    for i in cidadesValores:
        porcentagem = (cidadesValores[i] / total) * 100;
        dicCidadesPorcentagens[i] = porcentagem;

    return dicCidadesPorcentagens;

#Printa os resultados na tela
def printCidades(dicCidades):
    for i in dicCidades:
        print(f"{i} possui {dicCidades[i]:.2f}% do faturamento.")



#Dicionario com os valores
dicCidadesValores = { 
    "SP" : 67836.43 ,
    "RJ" : 36678.66 ,
    "MG" : 29229.88 ,
    "ES" : 27165.48 ,
    "Outros" : 19849.53
}

#Executando o codigo
dicCidadesPorcentagens = calculoValores(dicCidadesValores);
print("Porcentagem de cada cidade:")
printCidades(dicCidadesPorcentagens);