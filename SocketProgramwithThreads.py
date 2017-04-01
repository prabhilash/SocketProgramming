import socket
import sys
from thread import *

class SocketOperations:
    def __init__(self):
        self.socketAddressType = socket.AF_INET
        self.socketFamily      = socket.SOCK_STREAM
        self.host              = 'localhost'
        self.port              = 8888

    def createSocket(self):
        self.s=socket.socket(self.socketAddressType,self.socketFamily)
        print 'Socket Created'

    def bindSocket(self):
        try:
            self.s.bind((self.host,self.port))
            print "Socket is bind to "+self.host+":"+str(self.port)
        except socket.error as msg:
            print ("Bind Failed Error code"+msg[0]+'Message'+msg[1])
            sys.exit()

    def startListening(self):
        self.s.listen(10)
        # 10 is the backlog connections thge list of  queued connections please !!
        print "Now Listening on the Socket"

    def clientthread(self,conn):
       conn.send('Server is alive Type something Please !!!!!!!!!!')
       while True:
           data  = conn.recv(1024)
           reply = 'Ok .......'+data
           if not data:
               break
           conn.sendall(reply)
       conn.close()

    def creteThreadLogic(self):
       while 1:
           conn,addr =self.s.accept()
           print "Connected with "+addr[0]+":"+str(addr[1])
           start_new_thread(self.clientthread,(conn,))

if __name__=="__main__":
    soc=SocketOperations()
    soc.createSocket()
    soc.bindSocket()
    soc.startListening()
    soc.creteThreadLogic()