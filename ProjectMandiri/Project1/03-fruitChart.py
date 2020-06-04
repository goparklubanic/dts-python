#!/bin/python3

# dua variable berikut jangan diubah
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

# list buah
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

# MULAI KODEMU DI SINI
fruit_price = dict()
for i in range(len(fruits)):
    fruit_price[fruits[i]] = prices[i]


def counter_item(items):
    pass
    biting = dict()
    for item in items:
        if item in biting:
            biting[item]+=1
        else:
            biting[item]=1
    
    return biting

def total_price(dcounter,fprice):
    pass
    # MULAI KODEMU DI SINI
    tprice = 0
    for sfruit in dcounter:
        #print(sfruit,':',dcounter[sfruit],'*',fprice[sfruit])
        tprice += (dcounter[sfruit]*fprice[sfruit])
    
    return tprice

print(total_price(counter_item(chart),fruit_price))