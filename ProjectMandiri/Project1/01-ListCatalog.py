#!/bin/python3

def letter_catalog(items,letter='A'):
    pass
    output=[]
    for i in range( len(items) ):
        item = items[i]
        if item[0] == letter:
            output.append(item)
    print(output)


bunga = ['Anggrek','Anyelir','Bougenvile','Cempaka','Asoka','Camelia','Bouvardia','Deposito']
negara = ['Amerika','Brazil','Chile','Belgia','Canada','Argentina','Cameroon','Afganistan','Bangladesh']
letter_catalog(bunga,'A')
letter_catalog(negara,'B')