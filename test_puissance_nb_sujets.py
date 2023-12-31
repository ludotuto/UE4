# Copyright 2023 Ludovic Rousseau, Tutorat PSA
# Distribuée sous licence CC BY-NC-ND 4.0 
# Attribution-NonCommercial-NoDerivatives 4.0 International  
# https://creativecommons.org/licenses/by-nc-nd/4.0/
from math import *
print("")
print("Si on nous donne la puissance,si.on.veut")
print("un N très précis, mais que la puissance")
print("n'est pas un %age rond, rentrer P=0")
print("puis rentrer u2b (faut le calculer avant)")


print("")
print("entre k=0 pour n avec 1 proportion")
print("entre k=1 pour P avec 1 proportion")
print("entre k=2 pour n avec 1 moyenne")
print("entre k=3 pour P avec 1 moyenne")
print("entre k=4 pour n avec 2 proportions")
print("entre k=5 pour P avec 2 proportions")
print("entre k=6 pour n avec 2 moyennes")
print("entre k=7 pour P avec 2 moyennes")
print("")
def udbfromPuissance(P,Verbose=False):
    tmptable=[[0 ,0.01 ,0.02 ,0.03 ,0.04 ,0.05 ,0.06 ,0.07 ,0.08 ,0.09],
    [0 ,1e9 ,2.576 ,2.326 ,2.17 ,2.054 ,1.96 ,1.881 ,1.812 ,1.751 ,1.695],
    [0.1 ,1.645 ,1.598 ,1.555 ,1.514 ,1.476 ,1.44 ,1.405 ,1.372 ,1.341 ,1.311],
    [0.2 ,1.282 ,1.254 ,1.227 ,1.2 ,1.175 ,1.15 ,1.126 ,1.103 ,1.08 ,1.058],
    [0.3 ,1.036 ,1.015 ,0.994 ,0.974 ,0.954 ,0.935 ,0.915 ,0.896 ,0.878 ,0.86],
    [0.4 ,0.842 ,0.824 ,0.806 ,0.789 ,0.772 ,0.755 ,0.739 ,0.722 ,0.706 ,0.69],
    [0.5 ,0.674 ,0.659 ,0.643 ,0.628 ,0.613 ,0.598 ,0.583 ,0.568 ,0.553 ,0.539],
    [0.6 ,0.524 ,0.51 ,0.496 ,0.482 ,0.468 ,0.454 ,0.44 ,0.426 ,0.412 ,0.399],
    [0.7 ,0.385 ,0.372 ,0.358 ,0.345 ,0.332 ,0.319 ,0.305 ,0.292 ,0.279 ,0.266],
    [0.8 ,0.253 ,0.24 ,0.228 ,0.215 ,0.202 ,0.189 ,0.176 ,0.164 ,0.151 ,0.138],
    [0.9 ,0.126 ,0.113 ,0.1 ,0.088 ,0.075 ,0.063 ,0.05 ,0.038 ,0.025 ,0.013]]

    tmptable2=[[0.001,0.0001,0.00001,0.000001,0.0000001,0.00000001,0.000000001],
    [3.29053 ,3.89059 ,4.41717 ,4.89164 ,5.32672 ,5.73073 ,6.10941]]

    Nl=len(tmptable)
    Nc=len(tmptable[0])
    # P=1-alpha/2
    if P<=0:
        udb=float(input("u2b = ?"))
        return udb
    alpha=round(100*2*(1-P))/100
    if alpha!=0:
        if Verbose: print("P=",P,"=1-alpha/2 => alpha=",alpha)
        lignealpha=1+int(alpha*10)
        colonnealpha=1+int(alpha*100)-10*int(alpha*10)
        udb=tmptable[lignealpha][colonnealpha]
        #if Verbose: print("ligne",lignealpha,"colonne",colonnealpha,"udb",udb)
        print("u2b",udb)
        return udb
    else:
        # on a une petite valeur
        for i in range(3,9):
            alpha=round(2*(1-P),i)
            if alpha!=0:
                #if Verbose: print("P=",P,"=1-alpha/2 => alpha=",alpha)
                udb=tmptable2[1][i-3]
                #if Verbose: print("ligne 1, colonne",i,"udb",udb)
                print("alpha petit=",alpha,"u2b=",udb)
                return udb
    udb=float(input("u2b = ?"))
    return udb
def PuissanceLigneColonne(x):
   u2btable=[
[0.5000,0.5040,0.5080,0.5120,0.5160,0.5199,0.5239,0.5279,0.5319,0.5359],
[0.5398,0.5438,0.5478,0.5517,0.5557,0.5596,0.5636,0.5675,0.5714,0.5753],
[0.5793,0.5832,0.5871,0.5910,0.5948,0.5987,0.6026,0.6064,0.6103,0.6141],
[0.6179,0.6217,0.6255,0.6293,0.6331,0.6368,0.6406,0.6443,0.6480,0.6517],
[0.6554,0.6591,0.6628,0.6664,0.6700,0.6736,0.6772,0.6808,0.6844,0.6879],
[0.6915,0.6950,0.6985,0.7019,0.7054,0.7088,0.7123,0.7157,0.7190,0.7224],
[0.7257,0.7291,0.7324,0.7357,0.7389,0.7422,0.7454,0.7486,0.7517,0.7549],
[0.7580,0.7611,0.7642,0.7673,0.7704,0.7734,0.7764,0.7794,0.7823,0.7852],
[0.7881,0.7910,0.7939,0.7967,0.7995,0.8023,0.8051,0.8078,0.8106,0.8133],
[0.8159,0.8186,0.8212,0.8238,0.8264,0.8289,0.8315,0.8340,0.8365,0.8389],
[0.8413,0.8438,0.8461,0.8485,0.8508,0.8531,0.8554,0.8577,0.8599,0.8621],
[0.8643,0.8665,0.8686,0.8708,0.8729,0.8749,0.8770,0.8790,0.8810,0.8830],
[0.8849,0.8869,0.8888,0.8907,0.8925,0.8944,0.8962,0.8980,0.8997,0.9015],
[0.9032,0.9049,0.9066,0.9082,0.9099,0.9115,0.9131,0.9147,0.9162,0.9177],
[0.9192,0.9207,0.9222,0.9236,0.9251,0.9265,0.9279,0.9292,0.9306,0.9319],
[0.9332,0.9345,0.9357,0.9370,0.9382,0.9394,0.9406,0.9418,0.9429,0.9441],
[0.9452,0.9463,0.9474,0.9484,0.9495,0.9505,0.9515,0.9525,0.9535,0.9545],
[0.9554,0.9564,0.9573,0.9582,0.9591,0.9599,0.9608,0.9616,0.9625,0.9633],
[0.9641,0.9649,0.9656,0.9664,0.9671,0.9678,0.9686,0.9693,0.9699,0.9706],
[0.9713,0.9719,0.9726,0.9732,0.9738,0.9744,0.9750,0.9756,0.9761,0.9767],
[0.9772,0.9778,0.9783,0.9788,0.9793,0.9798,0.9803,0.9808,0.9812,0.9817],
[0.9821,0.9826,0.9830,0.9834,0.9838,0.9842,0.9846,0.9850,0.9854,0.9857],
[0.9861,0.9864,0.9868,0.9871,0.9875,0.9878,0.9881,0.9884,0.9887,0.9890],
[0.9893,0.9896,0.9898,0.9901,0.9904,0.9906,0.9909,0.9911,0.9913,0.9916],
[0.9918,0.9920,0.9922,0.9925,0.9927,0.9929,0.9931,0.9932,0.9934,0.9936],
[0.9938,0.9940,0.9941,0.9943,0.9945,0.9946,0.9948,0.9949,0.9951,0.9952],
[0.9953,0.9955,0.9956,0.9957,0.9959,0.9960,0.9961,0.9962,0.9963,0.9964],
[0.9965,0.9966,0.9967,0.9968,0.9969,0.9970,0.9971,0.9972,0.9973,0.9974],
[0.9974,0.9975,0.9976,0.9977,0.9977,0.9978,0.9979,0.9979,0.9980,0.9981],
[0.9981,0.9982,0.9982,0.9983,0.9984,0.9984,0.9985,0.9985,0.9986,0.9986],
[0.99865,0.99869,0.99874,0.99878,0.99882,0.99886,0.99889,0.99893,0.99896,0.99900],
[0.99903,0.99906,0.99910,0.99913,0.99916,0.99918,0.99921,0.99924,0.99926,0.99929],
[0.99931,0.99934,0.99936,0.99938,0.99940,0.99942,0.99944,0.99946,0.99948,0.99950],
[0.99952,0.99953,0.99955,0.99957,0.99958,0.99960,0.99961,0.99962,0.99964,0.99965],
[0.99966,0.99968,0.99969,0.99970,0.99971,0.99972,0.99973,0.99974,0.99975,0.99976],
[0.99977,0.99978,0.99978,0.99979,0.99980,0.99981,0.99981,0.99982,0.99983,0.99983],
[0.99984,0.99985,0.99985,0.99986,0.99986,0.99987,0.99987,0.99988,0.99988,0.99989],
[0.99989,0.99990,0.99990,0.99990,0.99991,0.99991,0.99992,0.99992,0.99992,0.99992],
[0.99993,0.99993,0.99993,0.99994,0.99994,0.99994,0.99994,0.99995,0.99995,0.99995],
[0.99995,0.99995,0.99996,0.99996,0.99996,0.99996,0.99996,0.99996,0.99997,0.99997],
[0.99997,0.99997,0.99997,0.99997,0.99997,0.99997,0.99998,0.99998,0.99998,0.99998]
   ]
   ligne=int(abs(x)*10)
   colonne=int(abs(x)*100-int(abs(x)*10)*10)
   # ligne=int(abs(x)*100)//10
   # colonne=int(abs(x)*100)%10
   nbligne=len(u2btable)
   nbcolonne=len(u2btable[0])
   print(ligne,colonne,nbligne,nbcolonne)
   if ligne<nbligne and colonne<nbcolonne:
       return ligne,colonne,u2btable[ligne][colonne]
   else:
       return ligne,colonne,"hors table loi N"


pa=0
pb=0
sa=0
sb=0
ua=0
ub=0
cvppa=0
cvppaa=0
cvppaaa=0
cvppaaaa=0
uo=0
ui=0
s=0
n=0
px=0
udb=0
cvpa=0
cvpaa=0


k=float(input("k = "))
if k==0:
 print("attention, utilisez les bonnes valeurs!")
 print("ne pas mettre πo pour π1 sinon c faux!!")
 print("")
 po=float(input("πo = "))
 py=float(input("π1 = "))
 pu=float(input("Puissance = "))
 udb=udbfromPuissance(pu)
 #udb=float(input("u2b = "))
 n=((1.96*sqrt(po*(1-po))+udb*sqrt(py*(1-py)))**2)/((po-py)**2)
 cvpa=abs(n*po)
 cvpaa=abs(n*(1-po))
 if cvpa>=5 and cvpaa>=5 and po<=1 and py<=1:
   print ("Nombre sujets = ",n)
 else:
   print("conditions PAS RESPÉCTÉES (ou mauvaise saisie)")
   print("(on trouvait n = ",n,")")

elif k==1:
 print("attention, utilisez les bonnes valeurs!")
 print("ne pas mettre πo pour π1 sinon c faux!")
 print("")
 po=float(input("πo = "))
 py=float(input("π1 = "))
 n=float(input("n = "))
 udb=(sqrt(n*(po-py)**2)-1.96*sqrt(po*(1-po)))/(sqrt(py*(1-py)))
 if udb>=0:
   ligne,colonne,puissance=PuissanceLigneColonne(udb)
   print("ligne table loi N",ligne)
   print("colonne table loi N",colonne)
   print("avec ",n," personnes")
   print("u2b = ",udb)
   if puissance == "hors table loi N":
    print("Puissance ",puissance)
   else:
    print("et Puissance = ",puissance*100,"%")
 else:
    print("avec ",n," personnes u2b=",udb)
    print("ATTENTION, PUISSANCE TROP FAIBLE <50%")
elif k==2:
 uo=float(input("mu o = "))
 uy=float(input("mu 1 = "))
 pu=float(input("Puissance = "))
 udb=udbfromPuissance(pu)
 #udb=float(input("u2b = ?"))
 s=float(input("s = ?"))
 n=((1.96+udb)**2)*(s**2)/((uo-uy)**2)
 if n>=30:
   print("Sujets nécessaire: ",n)
 else:
   print("Condit° Validité NON respéctée")
   print("30 > ",n)
elif k==3:
 uo=float(input("mu o = "))
 uy=float(input("mu 1 = "))
 n=float(input("n = "))
 s=float(input("s = "))
 udb=sqrt((n*((uo-uy)**2))/(s**2))-1.96
 if udb>=0:
   ligne,colonne,puissance=PuissanceLigneColonne(udb)
   print("ligne table loi N",ligne)
   print("colonne table loi N",colonne)
   print("avec n=",n," u2b=",udb)
   if puissance == "hors table loi N":
    print("Puissance ",puissance)
   else:
    print("et Puissance = ",puissance*100,"%")
 else:
   print("avec n=",n," u2b=",udb)
   print("ATTENTION, PUISSANCE TROP FAIBLE <50%")
elif k==4:
 pa=float(input("πa = "))
 pb=float(input("πb = "))
 pu=float(input("Puissance = "))
 udb=udbfromPuissance(pu)
 #udb=float(input("u2b = "))
 px=(pa+pb)/2
 n=((1.96+udb)**2)*((2*px*(1-px))/((pa-pb)**2))
 cvppa=abs(n*pa)
 cvppaa=abs(n*(1-pa))
 cvppaaa=abs(n*(pb))
 cvppaaaa=abs(n*(1-pb))
 if cvppa>=5 and cvppaa>=5 and cvppaaa>=5 and cvppaaaa>5 and pa<=1 and pb<=1:
   print("Sujets dans CHAQUE GROUPE: ",n)
   print("au total, il faut:",2*n)
 else:
   print("condition pas respéctée ou saisie erronée")
elif k==5:
 pa=float(input("πa = "))
 pb=float(input("πb = "))
 n=float(input("Sujets PAR GROUPE = "))
 px=(pa+pb)/2
 udb=sqrt((n*((pa-pb)**2))/(2*px*(1-px)))-1.96
 if pa<=1 and pb<=1:
   if udb>=0:
     ligne,colonne,puissance=PuissanceLigneColonne(udb)
     print("ligne table loi N",ligne)
     print("colonne table loi N",colonne)
     print("u2b=",udb)
     if puissance == "hors table loi N":
         print("Puissance ",puissance)
     else:
         print("et Puissance = ",puissance*100,"%")
        
   else:
       print("ATTENTION, PUISSANCE TROP FAIBLE <50%")
       print("u2b=",udb)

 else:
   print("erreur valeurs πa et πb")
elif k==6:
 ua=float(input("mu a = "))
 ub=float(input("mu b = "))
 pu=float(input("Puissance = "))
 udb=udbfromPuissance(pu)
 #udb=float(input("u2b = "))
 sa=float(input("sa = "))
 sb=float(input("sb = "))
 n=((1.96+udb)**2)*(((sa**2)+sb**2)/((ua-ub)**2))
 if n>=30:
   print("Sujets dans CHAQUE GROUPE: ",n)
   print("au total, il faut:",2*n)
 else:
   print("Conditions NON RESPECTÉES")
   print("sujets par groupes:")
   print("30 > ",n)
elif k==7:
 ua=float(input("mu a = "))
 ub=float(input("mu b = "))
 n=float(input("n PAR GROUPE = "))
 sa=float(input("sa = "))
 sb=float(input("sb = "))
 udb=sqrt((n*((ua-ub)**2))/((sa**2)+(sb**2)))-1.96
 if udb>=0:
   ligne,colonne,puissance=PuissanceLigneColonne(udb)
   print("ligne table loi N",ligne)
   print("colonne table loi N",colonne)
   print("u2b= ",udb)
   if puissance == "hors table loi N":
    print("Puissance ",puissance)
   else:
    print("et Puissance = ",puissance*100,"%")
 else:
   print("ATTENTION, PUISSANCE TROP FAIBLE <50%")
   print("u2b= ",udb)
else:
 print("erreur valeur k")
