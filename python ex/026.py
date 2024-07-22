string = input ('Digite uma frase qualquer: ').upper().strip()
print ('À {} letras "a" na frase' .format(string.count('A')))
print ('Ela aparece pela primeira vez na posição {}' .format(string.find('A')+1))
print ('E aparece pela ultima vez na posição {}' .format(string.rfind('A')+1))
