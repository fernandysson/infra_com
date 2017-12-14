import threading
import socket 
import os 
import Servidor

exitFlag =22 
port = 2525

class Conexao (threading.Thread):
	
	def __init__ (self, threadName):
		threading.Thread.__init__(self)
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.bind(('localhost', port))
		self.s.listen(5)
		self.name = threadName
		self.conexoes = []
		self.count = 0
		self.exitFlag =2 

	def run(self):
		while (self.exitFlag != 0):
			self.clisock, self.remote = self.s.accept()
			threadServer = Servidor.Servidor(("T_Server_" + str(self.count)), self.clisock, self.remote)	
			self.conexoes + [self.count]
			self.count += 1
			threadServer.start()
			self.exitFlag -= 1




