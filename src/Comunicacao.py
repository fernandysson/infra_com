import socket

def recv_send(self, msg):
	self.clisock.recv(n)
	self.clisock.send(msg)
	print self.msg

def send_recv(self, msg):
	self.clisock.send(msg)
	self.clisock.recv(n)
	print self.msg
