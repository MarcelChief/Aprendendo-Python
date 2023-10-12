nome1 = 'marcel'
altura1 = 1.8
peso1 = 57

nome2 = 'rebeca'
altura2 = 1.5
peso2 = 55

nome3 = 'laura'
altura3 = 1.5
peso3 = 60

def calculadora_bmi(nome, altura, peso):
    bmi = peso / (altura ** 2)
    print('bmi: ', bmi)
    if bmi < 25:
        return nome + 'ta safe'
    else:
        return nome + ' não ta safe'
    

resultado1 = calculadora_bmi(nome1, altura1, peso1)
resultado2 = calculadora_bmi(nome2, altura2, peso2)
resultado3 = calculadora_bmi(nome3, altura3, peso3)

print(resultado1)
print(resultado2)
print(resultado3)
