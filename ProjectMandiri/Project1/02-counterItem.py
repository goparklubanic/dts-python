#!/bin/python3

def counter_item(items):
    pass
    biting = dict()
    for item in items:
        if item in biting:
            biting[item]+=1
        else:
            biting[item]=1
    
    return biting
        

items = ['Merah','Kuning','Merah','Hijau','Kuning','Merah','Hijau','Kuning','Hijau']
warna = counter_item(items)
print(warna)

pilkades = ['Calon 1','Calon 1','Calon 2','Calon 3','Calon 2','Calon 2','Calon 3','Calon 1','Calon 2','Calon 3','Calon 2','Calon 1']
print(counter_item(pilkades))
