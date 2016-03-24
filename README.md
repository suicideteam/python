# Jabber && Moha

1.	Au démarrage du programme :
-	Veuillez renseigner l’adresse IP de la cible à attaquer
-	Veuillez renseigner le port de la cible à attaquer

2.	Vous arrivez sur « Command » :
-	Vous aurez 5 choix possibles :
a.	Accept (permet d’accepter la connexion entre les clients et le serveur C&C)
b.	List (permet de lister les PC clients, adresse IP…)
c.	Tcpfloodall (permet de lancer l’attaque tcpflood sur les clients) 
d.	Quit (permet de quitter le programme)
e.	Help (permet d’afficher l’aide)

-	Si vous tapez « Accept » :
Le master va demander au serveur d’accepter les connexions en attente, un message apparait « connexion accepter ».
-	Si vous tapez « List » :
Le contrôleur qui a accepté les connexions envoie une liste des pc zombies au master. 
Un tableau apparait avec l’adresse IP des PC zombies ainsi que la destination source.
-	Si vous tapez « Tcpfloodall » :
Le master va envoyer l’ordre d’exécuter l’attaque au serveur C&C, le serveur va lui envoyer l’ordre aux pc zombies d’attaquer la cible ajouté au début du script.
-	Si vous tapez « Quit » :
Le serveur va fermer le programme.
-	Si vous tapez « Help » :
Toutes les commandes possibles apparaissent avec une explication de chaque fonction.
-	Si vous tapez autre choses :
Vous aurez un message d’erreur « Commande Invalide ».
