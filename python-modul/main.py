#!/bin/python3
import aritmatika as rit

# print(rit.tambah(6,2.0))
# print(rit.kali(6,2.0))
# print(rit.kurang(6,2.))
# print(rit.bagi(6,2))

radius = 14
luas = rit.phi(radius) * radius ** 2
kllg = rit.phi(radius) * 2 * radius
print("Luas lingkaran dengan radius " , radius , " adalah " , luas , " satuan persegi")
print("Keliling lingkaran dengan radius " , radius , " adalah " , kllg , " satuan")