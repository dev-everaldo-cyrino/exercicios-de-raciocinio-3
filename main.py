n = int(input('quantos numeros vão ser adicionados:  '))
nnumero = 0
media=0
total = []

for x in range(n):
    nnumero +=1
    num = int(input('qual o {}° numero:'.format(nnumero)))
    total.append(num)
    media += num
    
total.sort()
print('''
      o total de numeros adicionados foi {}
      o maior numero foi {}
      e o menor numero foi {}
      a soma de todos os numeros foi {}
      e a media entre os numeros é de {:.1f}'''.format(n,total[len(total)-1],total[0],media,media/n))
    


    