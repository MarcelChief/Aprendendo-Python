qntd_pessoas = input('Quaarntas pessoas vão ter no seu quto?: ')
verificar_qntd_pessoas = qntd_pessoas.isnumeric()
if verificar_qntd_pessoas == True:
    pass
else:
    print('Digite um número valido')

lista_pessoas = []

for i in range(4):
    perguntar_cpf = input('Digite seu CPF: ')
    verificar = perguntar_cpf.isnumeric()
    verificar_longo = len(perguntar_cpf)
    if verificar == True and verificar_longo == 11:
        lista_pessoas.append(perguntar_cpf)
    else:
        print('Digite um CPF válido)')

    perguntar_nome = input('Digite o seu nome: ')
    verificar_nome = perguntar_nome.isalpha()
    if verificar_nome == True:
        lista_pessoas.append(perguntar_nome)
    else:
        print('Digite um nome valido')

print(lista_pessoas)
