import socket 
import os 
import Comunicacao

porta = 2525
n=1024
p = ">> "
class Cliente():

	def __init__ (self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect(('localhost', porta))
		self.msg = ""

	def recv_send(self):
		self.msg = self.s.recv(n)
		raw_input(self.msg)
		self.s.send(msg)


	def send_recv(self, msg):
		self.s.send(msg)
		self.msg = self.s.recv(n)
		print self.msg

	def recv_send_cmd(self):
		self.msg = self.s.recv(n)
		##01
		msg = raw_input(p + self.msg)
		self.s.send(msg)
		##comando enviado
		self.cmd(msg)

	
	def cmd(self, msg):
		if (msg == 'Q'):
			self.desconecta()

		elif (msg == "cd"):
			self.recv_send()
		elif (msg == "ls"):
			self.msg = self.s.recv(n)
			print(self.msg)
		

	def desconecta():
		self.s.recv(n)
		self.s.close()

S = Cliente()
S.send_recv("Quero conexao!")
msg = raw_input(">> ")
S.send_recv(msg)
## login enviado!
for i in range (1,5):
	msg = raw_input("Digitar comando: ")
	S.send_recv(msg)
	S.cmd(msg)
	raw_input("Digite ENTER para continuar.")





