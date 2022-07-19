import sys

print("")
print("--------------------------------------------------------------------------------")
print("Bienvenue sur le convertisseur PYCONVERT !")
print("--------------------------------------------------------------------------------")

convert = 1

while convert < 10:
    print("")
    print("--------------------------------------------------------------------------------")
    print("1. Kilogrammes en grammes")
    print("2. Mètres en centimètres")
    print("3. Litres en centilitres")
    print("4. Ampères en milliampères")
    print("5. Quitter le programme")
    print("")
    print("--------------------------------------------------------------------------------")

    choix = int(input("Veuillez choisir un type de conversion, 1, 2, 3, 4 ou 5 :"))
    print("--------------------------------------------------------------------------------")
    if choix == 1:
        entree1 = int(input("Quelle nombre de kilogrammes souhaitez-vous convertir en grammes ? :"))
        print(f"👉 Le résultats de la conversion de {entree1} kilogrammes en grammes est {entree1*1000}")
    elif choix == 2:
        entree2 = int(input("Quelle nombre de mètres souhaitez-vous convertir en centimètre ? :"))
        print(f"👉 Le résultats de la conversion de {entree2} mètres en centimètres est {entree2*100}")
    elif choix == 3:
        entree3 = int(input("Combien de Litres souhaitez-vous convertir en centilitres ? :"))
        print(f"👉 Le résultats de la conversion de {entree3} Litres en centilitres est {entree3*100}")
    elif choix == 4:
        entree4 = int(input("Combien d'ampères voulez-vous convertir en milliampères ?:"))
        print(f"👉 Le résultats de la conversion de {entree4} ampères en milliampères est {entree4*1000}")
    elif choix == 5:
        print("Processus terminé...")
        sys.exit()
    else:
        print("Veuillez entrer un nombre correct !")
convert += 1
    







