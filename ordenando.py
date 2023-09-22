from time import sleep
import os
carros=[
    {'fabricante':'fiat','modelo':'palio','ano':2010,'kmrodado':120000,'preco':23000},
    {'fabricante':'fiat','modelo':'argo','ano':2018,'kmrodado':40000,'preco':50000},
    {'fabricante':'fiat','modelo':'pulse','ano':2023,'kmrodado':12000,'preco':90000},
    {'fabricante':'honda','modelo':'fit','ano':2015,'kmrodado':100000,'preco':60000},
    {'fabricante':'honda','modelo':'civic','ano':2010,'kmrodado':80000,'preco':40000},
    {'fabricante':'honda','modelo':'city','ano':2008,'kmrodado':140000,'preco':33000},
    {'fabricante':'gm','modelo':'corsa','ano':1999,'kmrodado':280000,'preco':8000},
    {'fabricante':'gm','modelo':'prisma','ano':2019,'kmrodado':15000,'preco':45000},
    {'fabricante':'toyota','modelo':'corolla','ano':2014,'kmrodado':7000,'preco':62000},
    {'fabricante':'toyota','modelo':'yaris','ano':2018,'kmrodado':5000,'preco':75000}
]

def imprimir(lista):
    print("Fabricante\tModelo\tAno Fabricante\tKM Rodado\tPreço")
    print("---------------------------------------------------------------------")
    for c in lista:
        print(f"{c['fabricante']}\t\t{c['modelo']}\t\t{c['ano']}\t\t{c['kmrodado']}\t\t{c['preco']}")
    print("---------------------------------------------------------------------")

imprimir(carros)
sleep(5)

def imprimir_ordenados(lista, criterio, ordem): 
    os.system("cls")
    if ordem == 1: lista = sorted(carros, key=lambda item: item[criterio], reverse=False)
    else: lista = sorted(carros, key=lambda item: item[criterio], reverse=True)
    print("Fabricante\tModelo\tAno Fabricante\tKM Rodado\tPreço")
    print("---------------------------------------------------------------------")
    for c in lista:
        print(f"{c['fabricante']}\t\t{c['modelo']}\t\t{c['ano']}\t\t{c['kmrodado']}\t\t{c['preco']}")
    print("---------------------------------------------------------------------")

c=str(input("Insira o critério de prioridade: "))
o=0
while o<1 or o>2:
    o=int(input("1 - crescente\n2 - decrescente \nInsira a ordem desse critério: "))

imprimir_ordenados(carros,c,o)


'''
Ordenação de listas de dicionários:

Cada item vai ter as chaves específicas que carregarão os metadados daquele item.
Como um carro por exemplo, teríamos, marca, ano de fabricação, modelo e etc...


carros = [{"marca": XXXX,"modelo": XXXX,"ano": XXXX,"preco": XXXX},
          {<aqui teríamos outro carro com marca, modelo, ano e precos diferentes>}
]

para ordenar utilizamos a mesma sintaxe, mas sem o itens, pois agora é uma lista.

ordenados = sorted(carros, key = lambda item: item['preco'])

'''
ordenados = sorted(carros, key=lambda item: item['preco'])