n1 = int(input('Digite algum número: '))
n2 = int(input("Mais um número:"))
s = n1+n2
sb = n1-n2
m = n1*n2
p = n1**n2
di = n1//n2
d = n1/n2
print("\n O numero escolhido foi {},\n Seu antecessor é {} \n Seu sucessor é {}".format(n1, n1-1, n1+1))
print("\n O segundo número escolhido foi: {} \n Seu antecessor é: {} \n Seu sucessor é: {}".format(n2, n2-1, n2+1))

print('\n Aqui está suas somas: {} \n Sua subtração: {} \n Sua multiplicação: {} \n Sua potencia: {} \n Sua divisão '
      'inteira: {} \n Sua divisão padrão: {}'.format(s, sb, m, p, di, d))
print('\n Lambida no piru é mó bom')