vendas = {'jabson': 500, 'marcel': 600, 'cezar': 400}

#or colaborador in vendas:
#    if vendas[colaborador] > 500:
#        print('Muito bem')
#    else:
#        print('Se esforce mais!')

nomes = vendas.keys()
sells = vendas.values()

lista_nomes = list(nomes)
lista_nomes.sort()
lista_vendas = list(sells)
lista_vendas.sort()

print(lista_nomes)
print(lista_vendas)