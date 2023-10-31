dias = float(input("Digite quantos dias vai alugar o carro: "))
km = float(input("Digite quantos KM vai rodar com o carro: "))
alg = dias*60
dis = km*0.15
print("O aluguel deu um total de: R${:.2f}".format(dis+alg))