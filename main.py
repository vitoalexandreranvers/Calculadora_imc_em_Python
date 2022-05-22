#CALCULO DE IMC - INDICE DE MASSA CORPORAL

'''
Qual é a sua Altura em cm : 
Qual é o seu peso em kg:
'''

# MENOR QUE 18,5    MAGREZA
# ENTRE 18,5 E 24,9 NORMAL
# ENTRE 25,0 E 29,9 SOBREPESO
# ENTRE 30,0 E 39,9 OBESIDADE
# MAIOR QUE 40,0    OBESIDADE GRAVE

altura = float(input('Qual a sua Altura em cm ? '))
peso   = float(input('Qual seu peso em kg ? '))
imc = peso / (altura * altura)   # ou assim --> imc = peso / (altura/100)**2

if imc < 18.5:
    print('magraza')
elif imc >= 18.5 and imc < 24.9:
    print('normal')
elif imc >= 25.0 and imc < 29.9:
    print('sobrepeso')    
elif imc >= 30.0 and imc < 39.9:
    print('obesidade')
else:
    print("obesidade grave")