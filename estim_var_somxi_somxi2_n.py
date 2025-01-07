# Copyright 2023-2025 Ludovic Rousseau, TSSU
# Distribuée sous licence CC BY-NC-ND 4.0 
# Attribution-NonCommercial-NoDerivatives 4.0 International  
# https://creativecommons.org/licenses/by-nc-nd/4.0/
from math import*
var=0
s=0
a=float(input("Somme des xi= "))
b=float(input("Somme des xi carré= "))
n=float(input("taille de l'échantillon= "))
var=(b-((a**2)/n))/(n-1)
s=sqrt(var)
print("var=")
print(var)
print("")
print("s= ")
print(s)
