#!/usr/bin/python2.7

import socket
import os

porta = 2525
prompt = ">> "
p2 = "<< "

contador = 0

class conexao:
    
    def __init__ (self, port):
        self.login = ""
        self.dire = ""
        self.msg = ""
        self.prompt_usr = (self.login + ":" + self.dire + prompt)
        ##self.login = ""
        self.aceito = 0
	self.cont = 0
        #self.dire = ""
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
        #00
        if (self.msg == "Login nao encontrado"):
            self.recebe()
        self.comunica("Tem cadastro na BD?")
        self.recebe()      
        self.resposta()
        if self.msg_r == 'n':
            #01
            self.comunica("Voce deve se cadastrar para acessar uma pasta no sistema.")
            self.recebe()
            self.resposta()
            self.cadastra()
        else:
            #001
            self.comunica("Qual eh o seu login?")
            self.recebe()
            self.resposta()
            self.log()

    def log (self):
        st = "0"
        achei = 0
        arq = open ("usrs.txt", "a+")
        arq.seek(0,0)
        while(st != ""):
            st = arq.readline()
            st = st.replace("\n", "")
            print ("login da vez >> " + st )
            print ("login procurado >> " + self.msg_r)
            if(st == (self.msg_r)):
                print ("Achei seu login")
                self.login = st
                self.dire = ("usr/" + self.login)
                achei = 1
                self.comunica("Voce esta logado")
                break
        if achei == 0:
            self.msg = "Login nao encontrado"
            print(self.msg)
            self.comunica(self.msg)
            self.cad()
	arq.close()

    
	

    def cadastra (self):
        #03
        self.comunica("Por favor digite o login desejado...")
        self.recebe()
        self.resposta()
        self.login = self.msg_r
        self.dire = ("usr/" + self.login)
        arq = open ("usrs.txt", "a+")
        arq.write(self.login + "\n")
        arq.close()
        os.system("mkdir " + self.dire)
    	#05
        self.comunica("Voce ja pode me dar comandos a serem executados na sua pasta pessoal.\n" + self.prompt_usr)
        self.comandos()

    def espera(self):
        self.clisock, (self.remhost, self.remport) = self.s.accept()
        self.aceito += 1
        return self.clisock.recv(100)

    def desconecta(self):
        self.clisock.close()

    def comandos(self):
        
        self.recebe()
        print ("# # # # #")
        print self.s
        print("recebi: " + self.msg_r + "\n# # # # #")

        if(self.msg_r == "q"):
            print("adeus")
            self.desconecta()
        
        elif(self.msg_r == "ls"):
	    
            os.system("ls " + self.dire + " > retorno")
            arq = open("retorno", "r")
            self.comunica(arq.read())
            arq.close()
        
        elif(self.msg_r == "mkdir"):
         
            self.comunica("Digite o nome do diretorio, pareia... \n")
            self.recebe()
	    print(self.dire)
            os.system("mkdir " + self.dire + "/" + self.msg_r)            
        
        elif(self.msg_r == "rename"):
      

            self.comunica("Digite o nome do arquivo antigo, pareia... \n" + prompt)
            self.recebe()
            tmp0 = self.dire + "/" + self.msg_r
            tmp1 = (self.dire + "/ZzZzZ")
            os.system("mv " + tmp0 + " " + tmp1)
            self.comunica("Digite o nome do novo arquivo, pareia...")
            self.recebe()
            tmp0 = self.dire + "/" + self.msg_r
            os.system("mv " + tmp1 + " " + tmp0)            

        elif(self.msg_r == "rm"):
       
            self.comunica("Digite o nome do arquivo a ser deletado, pareia... \n")
            self.recebe()
            os.system("rm -r " + self.dire + "/" + self.msg_r)    
 
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
