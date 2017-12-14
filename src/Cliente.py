import socket 
import os 
import Comunicacao

porta = 2525
n=1024

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

	def send_recv_cmd(self, msg):
		self.s.send(msg)
		self.cmd(msg)
		self.msg = self.s.recv(n)
		print self.msg	
	
	def cmd(self, msg):
		if (msg == 'Q'):
			self.desconecta()

		elif (msg == "cd"):
			self.recv_send()

	def desconecta():
		self.s.recv(n)
		self.s.close()

S = Cliente()
S.send_recv("Quero conexao!")
msg = raw_input(">> ")
S.send_recv(msg)
msg = raw_input("Digite um comando...\n>> ")
for i in range (1,5):
	S.send_recv_cmd(msg)




