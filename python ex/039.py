from datetime import date

ano_Atual = date.today().year
nacimento = int(input('Em que ano vc naceu? '))
idade = ano_Atual - nacimento

if idade < 18:
    idade = 18 - idade
    print(f'Faltam {idade} ano(s) até seu alistamento!!!')

elif idade == 18:
    print('Está na hora de se alistar!!')

else:
    idade = idade - 18
    print(f'Esta esperando o que? Vc passou {idade} ano(s) da data de alistamento!!!')
