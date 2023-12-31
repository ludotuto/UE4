# Copyright 2023 Ludovic Rousseau, Tutorat PSA
# Distribuée sous licence CC BY-NC-ND 4.0 
# Attribution-NonCommercial-NoDerivatives 4.0 International  
# https://creativecommons.org/licenses/by-nc-nd/4.0/
from math import*
print("")

print("cohorte, on connais E on cherche M")
print("cas-temoin, on connais M ... E")
print("Entre: ")
print("0 si etude de cohorte")
print("1 si etude de cas-temoin")
k=float(input("0 ou 1 "))
a=float(input("nb Malade et Exposé "))
c=float(input("nb Malade et Non Exposé "))
b=float(input("nb non Malade et Exposé "))
d=float(input("nb Non Malade et Non Exposé"))
rabse=0
rabsne=0
RR=0
OR=0
RApe=0
RApp=0
pE=0
pE=(b+a)/(a+b+c+d)
print("")

if k==0:
  rabse=a/(a+b)
  rabsne=c/(c+d)
  RR=rabse/rabsne
  OR=(a*d)/(b*c)
  if RR>1:
    RApe=(RR-1)/RR
    RApp=(pE*(RR-1))/(1+pE*(RR-1))
    print("Rabs chez exposés=PM|E=",rabse)
    print("Rabs, non exp=PM|nonE=",rabsne)
    print("Risk relatif= ",RR)
    print("rap.d.cotes=odds.ratio=",OR)
    print("EXPOSITION=FACTEUR DE RISQUE")
    print("R.atribuable.exp= ",RApe)
    print("R.atribuabl.en.popu= ",RApp)
  elif RR==1:
    print("Rabs chez exposés=PM|E=",rabse)
    print("Rabs, non exp=PM|nonE=",rabsne)
    print("Risk relatif= ",RR)
    print("rap.d.cotes=odds.ratio=",OR)
    print("PAS_DE_LIEN_EXPO_MALADIE")
  elif OR<1 :
    print("Rabs chez exposés=PM|E=",rabse)
    print("Rabs, non exp=PM|nonE=",rabsne)
    print("Risk relatif= ",RR)
    print("rap.d.cotes=odds.ratio=",OR)
    print("EXPOSITION=FACTEUR PROTECTEUR")
  else:
    print("erreur valeur RR")
elif k==1:
  OR=(a*d)/(b*c)
  if OR>1:
    RApe=(OR-1)/OR
    RApp=(pE*(OR-1))/(pE*(OR-1)+1)
    print("rap.d.cotes=odds.ratio=",OR)
    print("R.atribuable.exp= ",RApe)
    print("R.atribuabl.en.popu= ",RApp)
    print("on peut pas estimer R absolu")
    print("on peut pas estimer R relatif")  
    print("EXPO=FACTEUR DE RISQUE")
  elif OR==1:
    print("OR= ",OR)
    print("pas de lien expo maladie")
  elif OR<1:
    print("OR= ",OR)
    print("l'expo protège de la maladie")
  else:
    print("erreur valeur OR")
else:
  print("erreur k")
