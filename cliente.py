#!/usr/bin/python2.7
#teste

import socket
import os

prompt = ">> "
porta = 25251
class Cliente:

    def __init__ (self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(('localhost', porta))

    def comunica (self, msg):
        self.s.send(msg)

    def chegada (self):

        self.comunica("oi, estou chegando...")
        self.recebe()
        msg = raw_input(self.msg_r + "... (s ou n)\n" +  prompt)
        self.comunica(msg)
        self.recebe()
        self.s.send("show...")

        print(self.msg_r)

        if msg == "n" :
            msg = raw_input(self.s.recv(100)+ "\n" + prompt)
            self.comunica(msg)
            self.recebe()
            print(self.msg_r+prompt)
            self.s.send("OK")
	    self.recebe()
	    print(self.msg_r + "\n")
	    self.comando()
        else:
            msg = raw_input(self.s.recv(100) + "\n" + prompt)
            self.comunica(msg)  
            self.recebe()
	    print(self.msg_r + "\n")
	    self.comando()       
    

    def saida (self):
        self.s.close()

    def recebe(self):
        self.msg_r = self.s.recv(100)

    def resp(self):
        print(self.msg_r)

    def comando (self):
        ##o servidor esta esperando umas mensagem / / o comando ##
	
        while 1:
	    print(" Digite seu comando :\n " )
            msg = raw_input(prompt)

            if (msg == "ls"):
                self.comunica(msg)
                self.recebe()
                print(self.msg_r)
		raw_input("Press enter to continue")
		os.system("clear")
		

            elif (msg == "mkdir"):
                ##
		self.comunica(msg)
                self.recebe()
                self.comunica(raw_input(self.msg_r))
		raw_input("Press enter to continue")
		os.system("clear")
		

            elif (msg == "rename"):
                ##
                self.comunica(msg)
                self.recebe()
                self.comunica(raw_input(self.msg_r))
                self.recebe()
                self.comunica(raw_input(self.msg_r))
		raw_input("Press enter to continue")
		os.system("clear")
		

            elif (msg == "rm"):
                ##
                self.comunica(msg)
                self.recebe()
                self.comunica(raw_input(self.msg_r))   
                raw_input("Press enter to continue")
		os.system("clear")
		

      ##      elif (msg == "upload"):
                ##
        ##    elif (msg == "download"):
                ##
          ##  elif (msg == "share"):
                ##



            elif (msg == "q"):
		self.comunica(msg)
                print("FLWWWWWWWw! \n ")
		break

            else:
		 os.system("clear")  
		 print("	Digite um comando valido!	 \n")
		 raw_input("Press enter to continue")
		 os.system("clear")  

##s.send(cmd)
##print s.recv(100)
os.system("clear")
cliente = Cliente()
cliente.chegada()
cliente.comando()
cliente.saida()
