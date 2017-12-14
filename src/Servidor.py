import threading
import socket 
import os 
import Comunicacao

n = 100
m = "Digite o parametro."
p = ">> "
e = "ERRO..."
b = "/"
pp = "<< "

class Servidor(threading.Thread):
	
	def __init__(self, threadName, clisock, remote):
		threading.Thread.__init__(self)
		selfName = threadName
		self.clisock = clisock
		self.remote = remote
		self.msg = ""
		self.login = ""
		self.dir = ""
		self.exit = ""		

	def run(self):
		self.autenticar()

	def autenticar (self):
		self.recv_send("Digite o login...")
		self.recv_send("Vou buscar...\n  ...\n    ...\n      ...")
		##
		self.login = self.msg
		self.dir = ("usr/"+self.login)
		if ( self.busca() == 0 ):
			self.cadastrar()
		while (self.exit != "QUIT"):
			self.receberComandos()
			self.clisock.send(self.msg)
		self.desconectar()

	def desconectar (self):
		self.clisock.send("Adeus!")
		self.clisock.close()

	def busca(self):
		st = "0"
		arq = open ("log/usrs.txt", "r")
		while(st != ""):
			st = arq.readline()
			st = st.replace("\n", "")
			if(st == (self.login)):
				return 1
		return 0

	def cadastrar(self):
		arq = open ("log/usrs.txt", "a+")
		arq.write(self.login + "\n")
		arq.close()
		os.system("mkdir " + self.dir)

	def recv_send(self, msg):
		self.msg = self.clisock.recv(n)
		self.clisock.send(msg)
		print pp + self.msg

	def send_recv(self, msg):
		self.clisock.send(msg)
		##!!
		self.msg = self.clisock.recv(n)
		print pp + self.msg
	
	def test (self, arquivo, tipo):
		aux = os.system("test" + tipo + arquivo)
		if (aux == 0):
			return 1
		else:
			return 0

	def receberComandos(self):
		self.send_recv("Digite um comando.\n" + p)
		##
		if (self.msg == "Q"):
			self.desconectar()
		elif (self.msg == "cd"):
			self.send_recv(m)
			if (self.test (self.msg, " -d ")):
				self.dir = self.dir + self.msg
				self.msg = self.dir + p
			else:
				self.msg = e
		
		elif (self.msg == "ls"):
			os.system("ls " + self.dir + " > log/retorno.txt")
			arq = open ("log/retorno.txt", "r")
			self.msg = arq.read()
			arq.close()
			





