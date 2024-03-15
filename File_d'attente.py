#On importe les bibliothèques Python
import time,random
from collections import deque


#On crée les différentes variables du programme 
lprenom= ["Michel", "Bob","Catherine","Cécile","Samantha","Gabrielle","Cedric","Gertrude", "Laetitia","Pascal","Garou","Rodolphe", "Jean" , "Amara" , "Lysandre","Nicolas", "Sarah", "Raphael","Douglas","Brigitte", "Marie", "Gabriel", "Aurélie", "Olivier","Bertrand","Tarzan","Dora","Chippeur","Monique","Marcel","Léo","Elio"]
#La liste qui recense les différents visiteurs dans la file d'attente 
file= deque([])
visiteur={}
#le nombre de visiteurs de départ
nb_depart = random.randint(1,5)
visiteurs_total = 0
temps_attente_totale = 1
#Les variables permettant de calculer la moyenne de satisfaction
moy_satisfaction = 0
nbr_satisfait = 0
#La variable correspondant au temps d'attente des visiteurs
temps_attente = 0


#On ajoute la fonction permettant d'ajouter des visiteurs à la file
def ajouter_visiteur(file):
    global visiteurs_total
    #on détermine aléatoirement la satisfaction du visiteur
    energie= random.randint(50,100)
    #on choisit aléatoirement le nom 
    nom = random.choice(lprenom)
    visiteur= {"nom":nom, "satisfaction": energie}
    #on ajoute le nouveau visiteur à la liste
    file = file.append(visiteur)
    visiteurs_total = visiteurs_total + 1
    time.sleep(1)


#On ajoute la fonction permettant de retirer un visiteur de la file
def retirer_visiteur(file):
    global visiteurs_total
    global moy_satisfaction
    global nbr_satisfait
    #on ajoute de la satisfaction en plus
    file[0]["satisfaction"] += 10
    #on équilibre la satisfaction si elle dépasse le nbr max (100)
    if file[0]["satisfaction"] > 100:
        file[0]["satisfaction"] = 100
    #la personne a fait l'attraction
    print(file[0]["nom"], "a fait l'attraction, et est très satisfait(e) !")
    print(file[0]["nom"], "a une satisfaction de", file[0]["satisfaction"])
    time.sleep(1)
    #on l'enlève de la file
    print(file[0]["nom"], "part de la file.")
    #on ajoute sa satisfaction à la liste
    moy_satisfaction = moy_satisfaction + file[0]["satisfaction"]
    nbr_satisfait = nbr_satisfait + 1
    #on fait la moyenne quand on a un échantillon de 20 personnes 
    if nbr_satisfait == 20:
        moyenne = (moy_satisfaction/ 20) 
        print("La moyenne de satisfaction est de ", moyenne, "%")
    print()
    time.sleep(1)
    #on le retire de la liste
    file.popleft()
    #on ajuste le nbr de visiteurs
    visiteurs_total = visiteurs_total - 1
    
    
#On ajoute la fonction permettant d'afficher le nombre de visiteurs de la file et leur énergie
def afficher_file(file):
    global visiteurs_total
    for i in range(visiteurs_total):
        print("nom: ", file[i]["nom"], ", satisfaction: ", file[i]["satisfaction"])
    #on affiche le nbr total de visiteurs dans la file
    print("Nombre de visiteurs dans la file: ", visiteurs_total)
    


def tour():
    global visiteur
    global visiteurs_total
    afficher_file(file)
    #on ajoute de nouveaux visiteurs
    print()
    print("De nouveaux visiteurs arrivent...")
    time.sleep(1)
    for loop in range(random.randint(1,5)):
        ajouter_visiteur(file)
        print("nom: ", file[-1]["nom"], ", satisfaction: ", file[-1]["satisfaction"])
    print()
    #on affiche le nbr total de visiteurs dans la file
    print("Nombre de visiteurs dans la file: ", visiteurs_total)
    #probabilité de panne
    panne = random.randint(1,4)
    #la panne tombe
    if panne == 1:
        print("L'attraction est en panne ! La file est temporairement fermée...")
        print()
        time.sleep(1)
        #la satisfaction des visiteurs baisse 
        for i in range(visiteurs_total):
            file[i]["satisfaction"] = file[i]["satisfaction"] - random.randint(10,15)
    #pas de panne, les visiteurs font l'attraction normalement
    else:
        #on retire deux visiteurs
        for loop in range(2):
            #il n'y a plus de visiteurs 
            if visiteurs_total == 0:
                print("Il n'y a plus personne ! L'attraction s'arrête.")
                break
            #il y a encore des visiteurs dans la file
            print()
            retirer_visiteur(file)
            print("Nombre de visiteurs dans la file: ", visiteurs_total)
            print()
            time.sleep(1)
    #on affiche à nouveau la liste
    for i in range(visiteurs_total):
        print("nom: ", file[i]["nom"], ", satisfaction: ", file[i]["satisfaction"])
        time.sleep(1)
    #on baisse la satisfaction des personnes dans la file
    for i in range(visiteurs_total):
        file[i]["satisfaction"] = file[i]["satisfaction"] - random.randint(1,5)
    temps_attente = visiteurs_total
    time.sleep(1)
    print()
    #On affiche le temps d'attente moyen pour les nouveaux visiteurs
    print("Temps d'attente moyen =", temps_attente,"minutes")
    time.sleep(1)



#On génère le nbr de visiteurs de départ
for i in range(nb_depart):
        ajouter_visiteur(file)
        time.sleep(1)
visiteurs_total = nb_depart
#On crée la boucle des tours
for i in range(10):
    tour()
    print()
    print()
    if i == 10:
        break
    print("Tour ", i+2, " ! La satisfaction des visiteurs dans la file a diminué:")
    time.sleep(1)

