meta = 10000
lista_pessoas_dados = ['Marcel', 'Matheus' , 'João' ,'Vivi',]
lista_pessoas_numero = [20000, 30000, 10000, 15000]
 
print(lista_pessoas_dados[1])

for item in lista_pessoas_numero:
    if item[1] >= meta:
        print('Parabéns {} você bateu a meta' .format(item[0]))