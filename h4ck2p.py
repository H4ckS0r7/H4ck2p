#!/usr/bin/python3

import os

print("\033[1;34m"+"------------------------")
print("\033[1;34m"+"| H4ck2P | P2P network |")
print("\033[1;34m"+"------------------------")
 
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("\033[1;35m"+"Introduce una seccion: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print("\033[1;34m1. H4ck2P start")
    print("\033[1;34m2. H4ck2P stop")
    print("\033[1;34m3. Salir")
      
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print("\033[1;32m"+"H4ck2P start")
        exit()
    elif opcion == 2:
        print("\033[1;31m"+"H4ck2P stop")
        exit()
    elif opcion == 3:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
        clear
print("\033[5;1;31;40m"+"Exit")
