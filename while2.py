vendas = []

while True:
    item1 = input('Digite a parada: ')

    if not item1:
        break

    item2 = int(input('Digite a 2 parada: '))

    vendas.append(item1)
    vendas.append(item2)

print(vendas)
