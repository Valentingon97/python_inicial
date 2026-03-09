texto = imput('introduce un texto')
nombre_fichero = 'archivo-'+ texto + '.txt'
f = open(nombre_fichero, 'w') #apertura w= write, r= red, a= apped
f.write(f'{texto}\n')
f.close()
