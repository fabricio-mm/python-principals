real = float(input("Reais que você deseja converter: "))
dolar = 3.27
euro = 6.78
print("\n A cotação atual referente ao valor indicado é:\n U${:.2f} \n €{:.2f}".format(real/dolar, real/euro))