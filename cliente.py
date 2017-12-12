#!/usr/bin/python2.7
#teste

import socket
import os

prompt = ">> "
porta = 2525
class Cliente:

    def __init__ (self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(('localhost', porta))

    def comunica (self, msg):
        self.s.send(msg)

    def chegada (self):
        #00000000000000000000000000000000
        self.comunica("Ola servidor, quero acessar uma pasta para meus arquivos...")
        self.recebe()
        msg = raw_input(self.msg_r + " (Digite [s / n]) >> ")
        #000
        self.comunica(msg)
        if msg == "n" :
            #02
            self.recebe()
            self.s.send("Tudo bem.")
            self.recebe()
            msg = raw_input( self.msg_r + "\n" + prompt)
            #04
            self.comunica(msg)
            self.recebe()
            self.resp()
	    self.comando()
        else:
            self.recebe()
            msg = raw_input( self.msg_r + " " + prompt)
            #002
            self.comunica(msg)  
            self.recebe()
            self.resp()
            if (self.msg_r == "Login nao encontrado"):
                self.chegando()

    def saida (self):
        self.s.close()

    def recebe(self):
        self.msg_r = self.s.recv(100)

    def resp(self):
        print(self.msg_r)

    def comando (self):
        ##o servidor esta esperando umas mensagem / / o comando ##
	
        while 1:
            msg = raw_input("   Digite seu comando >> ")
            
            if (msg == "ls"):
                self.comunica(msg)
                self.recebe()
		self.resp()
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
