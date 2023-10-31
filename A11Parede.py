largura = float(input("Largura da sua parede: "))
altura = float(input("Altura da sua parede: "))
m2 = largura*altura
tinta = m2/2
print("Considerando que sua parede tem {:.2f}m² a quantidade de tinta necessária é: {:.2f}L".format(m2,tinta))