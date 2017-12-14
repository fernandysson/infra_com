  1 import socket
  2 import os
  3 import Comunicacao
  4 
  5 porta = 2525
  6 n=1024
  7 
  8 class Cliente():
  9 
 10         def __init__ (self):
 11                 self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 12                 self.s.connect(('localhost', porta))
 13                 self.msg = ""
 14 
 15         def recv_send(self):
 16                 self.msg = self.s.recv(n)
 17                 raw_input(self.msg)
 18                 self.s.send(msg)
 19 
 20 
 21         def send_recv(self, msg):
 22                 self.s.send(msg)
 23                 self.msg = self.s.recv(n)
 24                 print self.msg
 25 
 26         def recv_send_cmd(self, msg):
 27                 self.msg = self.s.recv(n)
 28                 msg = raw_input(self.msg)
 29                 self.s.send(msg)
 30                 ##
 31                 self.cmd(msg)
 32                 
 33 
 34         def cmd(self, msg):
 35                 if (msg == 'Q'):
 36                         self.desconecta()
 37 
 38                 elif (msg == "cd"):
 39                         self.recv_send()
 40                 elif (msg == "ls"):
 41                         pass 
 42 
 43 
 44         def desconecta():
 45                 self.s.recv(n)
 46                 self.s.close()
 47 
 48 S = Cliente()
 49 S.send_recv("Quero conexao!")
 50 msg = raw_input(">> ")
 51 S.send_recv(msg)
 52 ## login enviado!
 53 for i in range (1,5):
 54         S.recv_send_cmd()
 55         S.s.recv(n)
 56         print(self.msg)
 57         raw_input("Digite ENTER para continuar.")
