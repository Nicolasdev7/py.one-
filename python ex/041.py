from datetime import date
ano_Atual = date.today().year

nacimento_Atleta = int(input('Entre com ano de nacimento do atleta: '))
classe = ano_Atual - nacimento_Atleta

if classe < 10:
    print('O atleta pertence a categoria MIRIM')

elif classe < 15:
      print('O atleta pertence a categoria INFATIL')

elif classe < 20:     
      print('O atleta pertence a categoria JUNIOR')

elif classe < 26:
      print('O atleta pertence a categoria SÊNIOR')

else:
      print('O atleta pertence a categoria Master')

