#### 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input('Informe uma nota entre 0 e 10: '))

while not (0 <= nota <= 10):
    print('Nota inválida')
    nota = float(input('Informe uma nota entre 0 e 10: '))


#### 3. Faça um programa que leia e valide as seguintes informações (e para cada uma delas, continue pedindo a informação até o usuário inserir corretamente):
##### Nome: maior que 3 caracteres;
##### Idade: entre 0 e 150;
##### Salário: maior que zero;
##### Sexo: 'f' ou 'm';
##### Estado Civil: 's', 'c', 'v', 'd';


nome = input('Digite seu nome aqui: ')
while len(nome) < 4:
    print('Nome invalido')
    nome = input('Digite seu nome aqui: ')

idade = int(input('Digite sua idade: '))
while not (0 <= idade <= 150):
    print('Idade invalida')
    idade = int(input('Digite sua idade: '))

salario = float(input('Digite seu salario: '))
while salario <= 0:
    print('Salario invalido')
    salario = float(input('Digite seu salario: '))

sexo = input('Digite seu sexo: ')
while not sexo in ['f','m']:
    print('Sexo invalido')
    sexo = input('Digite seu sexo: ')

estado = input('Digite seu estado civil: ')
while not estado in ['s','c','v','d']:
    print('Estado invalido')
    estado = input('Digite seu estado civil: ')


