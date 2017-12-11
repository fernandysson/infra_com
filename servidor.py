#!/usr/bin/python2.7

import socket
import os

porta = 25251
prompt = ">> "
p2 = "<< "

contador = 0

class conexao:
    
    def __init__ (self, port):
        self.login = ""
        self.dir = ""
        self.prompt_usr = (self.login + ":" + self.dir + prompt)
        ##self.login = ""
        self.aceito = 0
	self.cont = 0
        #self.dir = ""
        #create an INET, STREAMing socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #bind the socket to a public host,
        # and a well-known port
        self.s.bind(('localhost', port))
        #become a server socket
        self.s.listen(5)

    def comunica(self, msg):
        self.clisock.send(msg)
    
    def recebe(self):
        self.msg_r = self.clisock.recv(100)

    def resposta(self):
        print(p2 + self.msg_r)

    def cad (self):
        self.comunica("Tem cad?")
        self.recebe()
       
        self.resposta()
       
        if self.msg_r == 'n':
            self.comunica("vou lhe cadastra, bb...")
            self.recebe()
            self.resposta()
            self.cadastra()
        else:
            self.comunica("fazer o login entao...")
            self.recebe()
            self.resposta()
            self.log()

    def log (self):
        st = "0"
        achei = 0
        

        self.comunica("login?")
        self.recebe()
        #Login
        self.resposta()
        ##

        ##########################################
        #######################   CRITICO AJEITTAR
        ##########################################
        arq = open ("usrs.txt", "a+")
        arq.seek(0,0)
        
        while(st != ""):
            print ("login da vez >> " + st + "\n")
            print ("login procurado >> " + self.msg_r + "\n")
            st = arq.readline()
            st = st.replace("\n", "")
            if(st == (self.msg_r)):
                print ("Achei seu login")
                self.login = st
                self.dir = ("usr/" + self.login)
                achei = 1
                self.comunica("Voce esta logado")
		self.comandos()
            if achei == 0:
            	print("login nao achado")
            	self.cadastra()
       
	
	arq.close()

    
	

    def cadastra (self):

        self.comunica("login?")
        self.recebe()

        #Login...
        self.resposta()

        self.login = self.msg_r

        arq = open ("usrs.txt", "a+")

        arq.write(self.login + "\n")
        arq.close()

	
        os.system("mkdir usr/" + self.login + " && cd usr/" + self.login)
      
        self.dir = ("usr/" + self.login)
    	self.comunica(self.prompt_usr)
        self.recebe()
            ##Ok.
	self.comunica(" Cadastrado ! \n")
        self.resposta()
            ##self.desconecta()
        self.comandos()

    def espera(self):
        self.clisock, (self.remhost, self.remport) = self.s.accept()
        self.aceito += 1
        return self.clisock.recv(100)

    def desconecta(self):
        self.clisock.close()

    def comandos(self):

      #  self.comunica(self.msg_r)
        self.recebe()

        print (self.s)
        print("recebi: " + self.msg_r)

        if(self.msg_r == "q"):
            print("adeus")
        
        elif(self.msg_r == "ls"):
	    
            os.system("ls " + self.dir + " > retorno")
            arq = open("retorno", "r")
            self.comunica(arq.read())
            arq.close()
        
        elif(self.msg_r == "mkdir"):
         
            self.comunica("Digite o nome do diretorio, pareia... \n")
            self.recebe()
	    print(self.dir)
            os.system("mkdir " + self.dir + "/" + self.msg_r)            
        
        elif(self.msg_r == "rename"):
      

            self.comunica("Digite o nome do arquivo antigo, pareia... \n" + prompt)
            self.recebe()
            tmp0 = self.dir + "/" + self.msg_r
            tmp1 = (self.dir + "/ZzZzZ")
            os.system("mv " + tmp0 + " " + tmp1)
            self.comunica("Digite o nome do novo arquivo, pareia...")
            self.recebe()
            tmp0 = self.dir + "/" + self.msg_r
            os.system("mv " + tmp1 + " " + tmp0)            

        elif(self.msg_r == "rm"):
       
            self.comunica("Digite o nome do arquivo a ser deletado, pareia... \n")
            self.recebe()
            os.system("rm -r " + self.dir + "/" + self.msg_r)    
 
   # elif(self.msg_r == "upload"):
        ##
  ##      elif(self.msg_r == "download"):
        ##
    ##    elif(self.msg_r == "share"):
        ##

os.system("clear")
servidor = conexao(porta)
print(servidor.espera())
servidor.cad()

###LOOOOPPP
for i in range (1,100):
    servidor.comandos()
###

servidor.desconecta()
