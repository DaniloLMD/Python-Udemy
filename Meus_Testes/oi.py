nome = input('Nome Arquivo: ')
texto = input('Texto a ser escrito no Arquivo (<l quebra linha): ').replace('<l ', '\n')
a = open(nome+'.txt', 'wt+')
a.write(texto)
