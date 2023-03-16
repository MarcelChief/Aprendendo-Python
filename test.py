
for i in range(4):
    valor1 = input('Digite o primeiro valor para calcular:  ')
    valor2 = input('Digite o segundo valor para calcular: ')
    convert1 = int(valor1)
    convert2 = int(valor2)

    lista_das_contas = []


    conta = input('Digite a conta: ')

    if '+' in conta:
        adicionar1 = resposta_mais = convert1 + convert2
    if '-' in conta:
        adicionar2 = resposta_menos = convert1 - convert2
    if '*' in conta:
        adicionar3 = resposta_multi = convert1 * convert2
    if '/' in conta:
        adicionar4 = resposta_div = convert1 / convert2


lista_das_contas.append(adicionar1)
lista_das_contas.append(adicionar2)
lista_das_contas.append(adicionar3)
lista_das_contas.append(adicionar4)

print('Os cálculos usados por você foram: {}' .format(lista_das_contas))


