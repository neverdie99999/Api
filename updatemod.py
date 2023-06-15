   








 


###
wlcm = False
foxybot = False
ca = False
command=False
inviteB = False
back = False
offline = False
spy = False
msg= False
socktion =None

op = None
invite= None



spams = False
spampacket= b''
sendpackt=False
global statues
statues= True
SOCKS_VERSION = 5
packet =b''
spaming =True
###
listt =[]
remote_send=None
botcomendenable=False
###

global spam
def spam(server,packet):
    while True:
        time.sleep(0.012)
        server.send(packet)
        global msg
        if  msg ==False:
            break              
            

def loop_send():
    global botcomendenable
    print(remote_send)
    for data in __list_:
        time.sleep(0.8)
        remote_send.send(data)

    botcomendenable=True

import os
from time import sleep
import sys
import time
import socket
import threading
import select
import re
import requests

SOCKS_VERSION= 5


class Proxy:


 
    def __init__(self):
        self.username = "username"
        self.password = "username"
        self.packet = b''
        self.sendmode = 'client-0-'
        
        self.Spam_Message = [

        ]
            
            
        self.Activ_Code1 = [
        
        
b'\x12\x15\x00\x00\x01\x10?\xa9\xf0 \xed\x80\x95G\xd1\xba\xad\x1c\xd7$\x06\xee"o\x0f^\xa2\xcf!]\xa4\xd0p\x95\xde\xf5\x8f\x88`\xed23\xa8N\'\x0437\x9f\'\x177%7#\xb6\xf1m\xc2\x1f\xd6\xf6\xdb\xddR\x99p]\xd1\xa0\x8e\xd4F\xd5%\x85<n\x87\xf7\xd1\xaa\xa2\xef\xd3z\x03\x83\x0b\x8e\xb6\x93\xdc\xaa)Rl6.[~\x10BN\x85\xff\x8c{\x90\x02A"\xd0\xffj\xf7\xf2\xcf\xd4\x92}\x9a0_\x92\x12(Ga\x07Hi\xcf\x0b\x0f\x932\xcf\x03>O\xefD\xf1\x95\x9aKL\xf5\xcd\x024\xd5\xd3"\xb77\xff\xe1\xef\x9d\xe2\xa8\x1e\xb9\x94\x81\xf0r\xff\xe2\x07\x18\x1e\x0e\x9c\xb8\x1cQ\xe3\x04\xc6\xb2\xf1\x14/8\x7fL|3\xef\x83\xe3\x1f\x95U\x88i2\x89\x8ez>q\xd5o\xc4\x16$\xe7\xc1\x82/c\x1c\x92*\xeb4\x01\x94\xcc\xb3MS7>\xf8\xa8To\xd9L\xf6\x0c\x10\x8b\xe6<\xde\x83\xe3]\xe7\xaf9\x9c\xb5\xb2qK2r\x02\xea\xdd\xeby\xc8\xc7\x03t\xab\x8fu\x81s2\xe9V\xc7\xea\x88\xf0\x7f\x15>'
,
b"\x12\x15\x00\x00\x01\x00t\x0b\x999\xbac\x87\x89\x19\xed\x1d\xbf[\xcctl\xb0q>\x19\xf3\xc3\xd4>\x0c\xffWR\x86\x8b\xe4\xaf\x8az\xc7\xf1\x11U\x04F\x0e\x10\xb9\xb7K\xbe\x1f!\xef\xf5x\x03$LlZ/\xd0\xd1xZ;\xca\xfeD\x80\xa1V\xcb\x1af\x9b\xa2\x02K\xc0$\xb1\x18\x90\xd4\xbb\x13\\\xb0\xf6\x16z\xbev'ws\xeaG^\xe1\xc9V\x95\x7f\xd4B\x83\x1d1\x96x\x06\x0f\xc4\xc1\xb4\xe5w\x14\x9b\xc2U\x17\xa5L\x91\x13\xe5\xc7\x89\xa9\x07\xe5L<`\x1e9\xd6\x81\xd3\x0cac\xe8\x97\\]R\xd2iX\x98\xd2\x10b\x87\xa0\xeem\xe1\xe6_Y\xea\xfe\xc7\x04*6bcB\xb1\xee\x11\x9e#\xf0\xec\x15\x06E\x16|@\xf2L\xec\x94\x92\x12!I\x0f\xf6}\xbd\x9e\xaf\x820\x0f\xc0\x13QN1'\xa4\xe9\xeb;\x03\xec\x0b\xe5\xfc\xc7\xb8\x8d+\xec\xd8\xa7d\xf3z\xeawX\x99u]\x06\x03\xc6\x19l\x90\x06\x87\xadW\x96\x9c\xa4G\x12V\x92\xb0\xe9V\x84\xca|\xbe\xc4"

        
        
        ]
        
        self.Stop_All = [
b'\x12\x15\x00\x00\x00\xe0I\xc9}\x97]\xae\xfe\\\x8c\xa2t\xdfK\x9e\x0b\xd2%\xb9p\xeb\x86{\xf5n>\xe1f\xb1\xe1\xd2z\x91Q\xde\xb6O\xb4\xe7\x90\xc5}\xd9\x96[\x17\xd0b\xe1m\xe1\x82\x1d\t\xba,H\xa4\xf1\x96\x00\x95O\xfe\xfeF\xe7\xf7\xf4\xb7\xdc\xcf\x13v\xcf\x83\xce\x9e\x9eH`\xd8\x08\xf1\xf2\t\xd8\x99\x16\xfd~\xa6\xa6/\'\x1b\xdf\xdc`K\x14V\x92\xe2\x96\x1aL\xce\xb7\\7e\x9fL(\xc0y\xfa\xfa\xef\x92&\xa4\xaa\xb47\x8d:oX\xae\xa6\x89N)\x8f\xa2 \x85s\x16\x12\xfc\x85\x01\xe0\xb2xEm\x10\xfe\x8d\x86>\xb3\\\x03\x93`}"\xe5\xfdl\'1\x1e\x92\xde\\\xf5bAg3\xce\xaf\xc6u[xy\xc8\x93p\xd31l\x94\xcb\x01\xe2\x18\xd5\x92c\xee\t\x01\x12\xb0\xb1\xf5\xd8\xcd\xfe\x04\xa2\xc7\xc9\xc8\x13*7MON\xa0\x9b\xf7\x99KK\xdc'

        
        ]
        
        self.running = [
        
b'\x12\x15\x00\x00\x00\xe0I\xc9}\x97]\xae\xfe\\\x8c\xa2t\xdfK\x9e\x0b\xd2U\x9es\xd5L\xafK\xbdp\xd6=\x94\xd1\xb4\xaa6g\x99\xb1-\x90@\x88\xf5\xfe\xb96\xd6GN\x9b=\xbf\x8c;\xe4j/\xd1\x00\x19\x9f7^\xf1Yvv\x19\x8d\x8d\x01*\xa3\xbd\x04]\xbd\xd2\xc3p$\x15\xb4\xe0\xc5p\xbas\xc5\x14\x81rTl\xe8\x8e\x9a\xe7\xd2\x9f\x7f\x02\xa7\xf9\xf7\x00\xadH\xdd\xf5\xb2\t\xef\x18p\xecW\xe4Z\xfa\xe2mF\xee)\x82\xe9"wk\xeb\xfc\xb4\x15\xc8\xa3\xdd\x94\xff\xebB/\xde\x8c.\x19\xf2T\x9b\x82#\x1c\x85AXS \xf8\x0b\xb30\tI+\x80\xcfRg\xc8\xe3\xeb\x9d\x0f\x9c\x84\x98c\xb5>\x85\x8f\x02$\x0e:\xd5\x8d\x1b\x0ey\xd1\x16\x82K\xf4\'\xea\x17\x0c\x8a\xf7\x17\xc7\x8e\xd3M\xc7Ba\x12hA]xom\xb0\x85\xf9\xa7\xffeR\xbaf\xe4\x9e'


        
        
        ]
            
            
        self.update = [
b"\x12\x15\x00\x00\x00\xf0S\xef\x02\xf5\x95H\x1d\\7\xa59\xd8\x1c\x92\xfc=\x88D E\xef\xfc\x86\x02\x11\xe1\xd8l\xafx\xe7\xc0\xb7\xbd\xe1$#\x83,\xaa(\x18\x9e\xee\x9a^\x8e\xe3\xea\xdc-L\x81\xc6\xff\x86\x86\x19\xc0\xdc\xbe2f\x8e\xec\xf7\x8f\xea\x03T\xac\x8ej\xb8\x86\xaa\xbcb\xe4'\xf6\x89\x86\x91J\xd4m%\xe8\xa4._\xa1\xd6\xbf\x9cvB\x1f\x9b\xc5\xbcQd\x17\xe1\xaa\xf0\x93x\x84\xae2dR\x90\x9b?9\x81xX4\x97:\x9cA`^\xd1\x0e\xd8\xed\xe7\x08\xe5\x1eD\xa9\xf6K\xd2\xb0\x05\xf4\x19\xa8)\xb1\xd7\xe4\x01\xe6\xe6\xb0.\xca\xc0Z\xec\xf5\xf4\x89\x1e\xa70\x98\x90\xb7y\xdcw{W\xf2\xf1\x06\x95\x1a\x8463\x9d\xa3\x8bn\xd2\x95\xe2`J\xbc\x80t\xe4\xcd\xf8F\x0ew\xa59\x8e\xe3\xbf\x10\xd0$}\n$\xd6\xbf^\xa5\xbb\xb3\x02\x81\x95dI\x96+\xb7\x95\xc2\x18\x0c\x18\xe3\x06\xfc\x1d\rL\x9f\xaf\x94\xdf"


        
        
        ]
        
        
            #Welcome
        self.__list_ = [
            b'\x12\x15\x00\x00\x00\xb0\xddt\xa5\xe5;\xf4\'\x02M\xd0G\x83\\\xa5\x8ew\x03\x84\x13O\xef\xcb\x02\xe4-\x86\x0eZ\x92\xbb\x9b\xa6\x9f\xc1S\xd0\xb2S;\xa0{\xcb8\n\xe0+e+4\xc4l\xf8\xea+\x15\xbe\nW\x9d\x08W\x86ky\x9a\xd1\x96\x0e\xa7\x03\xa8\xf6\x97"\x1b/\xf8\xd3\x13\xd0\x06\xf9Y\xf6]\xe3dA\xf7\xd8X\xaf(N\xf1\x9c\x99\xffJ\x13\xde\xe6]%w\x0f#\x00\'_\x8c\xc3^\xb5K|\x0f\xe9r\xa4L\xdb-\xfd\xebD\x1b\xf1B_\xe7\x0eY\xfai\xfd\x97&\xd1gb\xe3*\x171\xbe\xf2^\x13\xf3\xa4\xa7tf\xcb\x97*\xa3a\xe5\xe4JSg\xaab/\x1e\xb1\rb\xd6\x03]l\x88'
            ,
            b"\x12\x15\x00\x00\x00\x80\x13q,\xe8]9\x8a\xd1us'\xc0p\x91v\xdb\x13\xe4\x06\x7f8<0\xe9\xf3\xfb@L\xdf\xe0)K:)p\xdf\xe7\xc3\x15A\xdcH*s5\x15\x19\x89m\x8a\xa4\xce\xc1\x84\x83\x82\xc6\xdb\x85\x1cC-[\xd6\xfap\xcd\xdf\x1b\x1f-\x19t\xb1\x198\xf5>\xead\xd7\x1c7\xd2\x12\xb92\x12\xa1V\xed\x83\x0c\xf9z\x0c\x91{\xd5B\xee1\xd8o\x0b};D\xdc\xb3\x85\xfd?i\x88\xfc]\xbf\x0c\xdcO\xb0tl\xf7\x85\xe9\xa1"
            ,
            b'\x12\x15\x00\x00\x00pT\xea9\x7f\x1f\xcfk\x8d0M\x05\xd8( \xd8\x16\xacN\x01\xbc\xb6\x87\x9b\x9f\xdc\xaff\x0b\x08\xd6\xcd\xddO3\xf2\xcfn\xc9\xa0\x00KDp}v\xdb]\xb4R\xa9.\x0f \x88\xaeK\x8e\xb5Xs\xb9g\xf2#\xfct\x8e\x1c\xc2\x1f\xc1\xd6\x1a\x93\x17\xd4s\x97O\xa5\xe2\xb3\xc8*+\xf8\xda&j\xd8\x85m\x8e\x1b\xfcF\xae\xf5f\n\xd7)n9\xbcE\xa0\x9dW\xd1\xb4\xbd'
            ,
            b'\x12\x15\x00\x00\x00p\x93W\x97\x84-\xf3\xe3\x15\x1d\xd9O)o\xbd\xd5ui\xed\x16\xe8\xc3\xd6_\xf9E\x87\x8f\x85\xad9^i1\x8c\x17\xfa\x94\xb9\xf0\x8c5A\xc8\x9brU\xee\x8d\xac\x10\x99[\x1c\x03@\xdb\x82pwaN\x11\xd4\xbe\xb7\xab\x0e\xa9y4\x80Y\x17\xaeY\x99\xd6\x12\xc2\xf0\x80\x98\x9d\xc2$\x18B\x1c\xe9\x0c5;\xde\x02R\xd5BE\xff\xd7\x1a\x06ng\xb0\xa9\xa5+\xe6|T%'
            ,
            b'\x12\x15\x00\x00\x00\x80[\x1e\x0e\x02\x12\xd9\xac\xac\x00\xd7\xa2\x9eg\x1c|s\xd6+\x984\x14\x86\xb3;\xae\x90\x94\x9e\x99[\x8aN]\x06?3\xd1jR\x99\x0cfd\xdb>sVnc\xd5\x9a\xf6\xfd<\xe3\xa9\x87\xeek\xcd\xa4\x9a\xf6\x19\x89G\xb6\xd3\x8d\xdeJ\xa5\xea\x915\xb0M<\x83\x12\x00Q\t.\x99\x08\x16\xff\n\x939F\x8e\xd5\xc16iNX\x02k{\xaf\xb9\xde\x07\x99d\x11_\x02j\xc6=\xd75e\x8du\x1e\xcd;R\xfd)\xb5\x96H'
            ,
            b"\x12\x15\x00\x00\x00\x80\xa4\xdbE\x9c\xa5V)\x04Yxr\xb6\x08\x9a\xee\x0f\xfe\xa5\xd5\xf5\xab\xa7\xc5J\xe6\x1f==\x96\xb3\xd7\x7fKh\xe4t\xecL9\x95\xa9\xd6\xc6\xed\x91$a>\xfd\xd1SFy\x920\x06\x8a:\xb8HjWI\x0e\xbf\x1abr\xb5\xa5\xc0\x94\xc4\xd9\xd9\xcb\t\xc0F\xaa\x08\xff\x96'\xd4\x07\x97H\xe3\xe4^u5\x17\xf1{lU\xe7\xb2\xb9+\xae\x001a\xad\x9c\xf6\x1aT_\x94`\x16$\xa7\x04\xd4\xe1\xe4\x00\xde\x08\x11\x82\x8dL"
            ,
            b'\x12\x15\x00\x00\x00ph\xf5\x83K\x86\xde\x85,c{\x9e?\x87\x0f\xd06\xd6.\x84"D\x9b\xa8l8\xa5\x7f\x9e\xf0\xaf\x1b\x96\x01\xc3\xa678\x1eb\xb6\xc7&J\x03\x12\x1c:s\xa8\xa20;\xc7\xb9YjK\xdc\x19\xd2#a\xf3\x87\x08\xb0\xd2"\xa2\x9bL\xbfM\xb1\xc2\xeb\x0fJ}V\xc2S\x05A\xf3snn\xf1f\xb6\x0c%\xa1dsh\x87\xc9K\x89\xb5#{/\xf12\x9fsk\xbed'
            ,
            b'\x12\x15\x00\x00\x00p\x047\xfb\xa5\\\x8b\xe8\x1f!7\x16Z\xe3\xf4I\x01\xcfV\xe9;4\xf6\xfc\x1d\xd7m8\xe6\xa2o\xbb\x0c\x03N\x1c$M\xcd\xca%\xa0\xac\xa2U\xee\xb4\x01\x82I\xc3\x0b\x80\xa7\xa0z\xf4SY\xd5\xa1P\x1d`\xaeE\x05\x87T\xd0o\x91\xeb\x0c`\xb9\xd7\x98H\x91\xca"\x93\xc33Dm\xa4\xe1"\x07}\xe1\xb5Vg\xe2=\xaa5uG\xbf\xf6\x01\x0e\x85?`\xb0\x86-\xe1'
            ,
            b"\x12\x15\x00\x00\x00\x80\x13q,\xe8]9\x8a\xd1us'\xc0p\x91v\xdb\x13\xe4\x06\x7f8<0\xe9\xf3\xfb@L\xdf\xe0)K\x9b\xedH\x8dm\xf0\xf8k\x88\xabK\xb3\\\xbc\xees\x9dS\x90\xbd\xfb\xb4\x89\xf2K\x19\t}\xc8g\n\x90\x98\xfb\xcd+`\tF$\xc3\xd2\x06\x08\xd1\xa3\xaaM5H]m\xbd\xbe\xc7\xb5\xca\xe53\xdd\xd1\xd5\xc4\xeb\x9a!\xd8\xb0\xd1,\x93-4\x16C\x99\xc6S\xba\xa3#b\xc8\xa6\xa0\xb4\xf4j\x8f\xd2\x05\x8b\x82\xa2\x8a\xd9"
            ,
            b'\x12\x15\x00\x00\x00p\xad\xd3\xc5\x1eF\xca%\x96\x06\xdaZ\x99\xc4>_\n\x81\x01]\xf8\xd2\x0b\x84\xbe\x074\\=(\x96\xb5\xa4#\xeem\xe2\x08\x06M\xe4d)\x18\xde\x96\xc2uI\xab\xe1\xcb\xd0\x17\xdc\x04\x8d\x0eF\x1b\xc2\x18Z\xd2\xc0\xb1\x9bX\x8b\x04\xdc\x12\xd8+3~\x9e\x8a\xe0\xddj%\\\xbd\x1bQX\xd6L#C\xa0\x1b\xe5\x16`\xeb]`\x98~;\x93R\x89\xe0\t\x9b \x19FC\xa3'
            ,
            b'\x12\x15\x00\x00\x00p\xdf^+\xd65_\xf4\xdb\xf2&\xec\x8d\xfc\xd2\x92\xffa\xcb\xe3\x14I\x8c\x1d\x16(\xa9\xce\xe0=\x0f\x14\x1c\xacV\xe9\xc3\xf9\x1d\xf5\xb3\xfb\xc7\xdfPp\x05d\x1b\x8c4\x86Q\x17?\xaa\x91\xd6\x99\xa3\xe0\x1b\xb4\xbf\xd8\xdd4\xa2\xf2\xbd\x83"\x86p%\x95\xd0X.\x05\xe6MN\x1c\x14\x08k\x95\xac@A|\xf1~t\xc6Ec\x8aZ\xf0\xfb\x82B\xaf\xe6\x16j\xf6\x07F\xad&'
            ,
            b"\x12\x15\x00\x00\x00p\xde\xa3\xe9fr|a\xcb\x01\xbe\xbc\x00\xc7\xc6\xea\r\x8a'\xf8\xad\xefG\x18^ko\x8aX\xe2q\xfbw\xe40\xcf\x8f\xf0\xea\xea\xb3\x9coYo\xdf)\xbac\x1c\xfcm\xd0\xc0\xdf\xdf\xdc\n^|\x1b:\xd3Fz#\x88\xe54\x972#\xdf\xef\xae8:X\xbb~\xfb\x9f\xfc\xb1\xce\x88j|\x8c\x07\xfb\x10\x88d\x1e.mu^\xe3\x13\xe7\x89V\xe6\xa8\xb3\xad\x88\xc8\xd9\x05\x8e"
        ]
        

    def handle_client(self, connection):
  
        
    
        version, nmethods = connection.recv(2)
        methods = self.get_available_methods(nmethods, connection)
 
  

        if 2   in set(methods):
            if 2 in set(methods):

                connection.sendall(bytes([SOCKS_VERSION, 2]))
            else:
                connection.sendall(bytes([SOCKS_VERSION, 0]))
                
    

   

        if not self.verify_credentials(connection,methods):
            return
        version, cmd, _, address_type = connection.recv(4)
        
        

        if address_type == 1:
            address = socket.inet_ntoa(connection.recv(4))
        elif address_type == 3:
            domain_length = connection.recv(1)[0]
            address = connection.recv(domain_length)
            address = socket.gethostbyname(address)
            name= socket.gethostname()
        


        port = int.from_bytes(connection.recv(2), 'big', signed=False)
        port2 = port
        try:
           


       
        
                remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                remote.connect((address, port))
                #print(" connect to {} \n \n \n ".format(address))
                bind_address = remote.getsockname()

                addr = int.from_bytes(socket.inet_aton(
                    bind_address[0]), 'big', signed=False)
                port = bind_address[1]

                reply = b''.join([
                    SOCKS_VERSION.to_bytes(1, 'big'),
                    int(0).to_bytes(1, 'big'),
                    int(0).to_bytes(1, 'big'),
                    int(1).to_bytes(1, 'big'),
                    addr.to_bytes(4, 'big'),
                    port.to_bytes(2, 'big')

            ])
        except Exception as e:
        
            reply = self.generate_failed_reply(address_type, 5)
         

        connection.sendall(reply)

        
        self.botdev(connection, remote, port2)
     

    def generate_failed_reply(self, address_type, error_number):
        return b''.join([
            SOCKS_VERSION.to_bytes(1, 'big'),
            error_number.to_bytes(1, 'big'),
            int(0).to_bytes(1, 'big'),
            address_type.to_bytes(1, 'big'),
            int(0).to_bytes(4, 'big'),
            int(0).to_bytes(4, 'big')
        ])

    def verify_credentials(self, connection,methods):
    
        if 2 in methods:
           
            
            version = ord(connection.recv(1))
        

            username_len = ord(connection.recv(1))
            username = connection.recv(username_len).decode('utf-8')

            password_len = ord(connection.recv(1))
            password = connection.recv(password_len).decode('utf-8')
         #   print(username,password)
            if username == self.username and password == self.password:

                response = bytes([version, 0])
                connection.sendall(response)
         
 
                return True
            
            response = bytes([version, 0])
            connection.sendall(response)
    
            return True
            
        else:

            
            version =1 
            response = bytes([version, 0])
            connection.sendall(response)
            
 
            return True

    def get_available_methods(self, nmethods, connection):
        methods = []
        for i in range(nmethods):
            methods.append(ord(connection.recv(1)))
        return methods

    def run(self, host, port):
        var =  0
        

        

     
        
     
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen()
  
        
  
        while True:
            var =var+1
            
           
            conn, addr = s.accept()
            running = False
          
            t = threading.Thread(target=self.handle_client, args=(conn,))
            t.start()
  




#  
    def botdev(self, client, remote, port):
            
        while True:
            r, w, e = select.select([client, remote], [], [])
            
            if client in r or remote in r:
                global op
                
                if client in r:
                    dataC = client.recv(99999)
                    global foxybot
                    global msg,command,spy,inviteB      
                    global remote_send , botcomendenable
                    
                    ##
                    global hide 
                    hide = False
                    if '1215' in dataC.hex()[0:4] and msg ==True:
                        
                        for i in range(10):
                            remote.send(dataC)
                        global spam
                        time.sleep(1.0)
                        b = threading.Thread(target=spam, args=(remote,dataC))
                        b.start()

                    global spams
                    spams =True
                    
                    if '0515' in dataC.hex()[0:4] and len(dataC.hex()) >= 141:
                        hide = True
                        
                    
                        
                        ##
   
                    if port ==39801 :
                        remote_send=remote
                        self.spam_ip_39800.send(data) 
                        
                    if "39800" in str(remote) :
                       self.spam_ip_39800=remote

                    if "39698" in str(remote) :
                   
                       self.op = remote
                       
                    if port ==39698:
                        op = remote
                        invite= remote
      
     
                        op = remote
                        invite= remote
                  
      
                       

                      
                    if '0515' in dataC.hex()[0:4] and len(dataC.hex()) >=820 and inviteB==True :
                        try:
                        
                            for i in range(3):
                                threading.Thread(target=spam1 , args=(dataC , remote)).start()
        
                        except:
                            pass
                  


   
                                               
                    if '0515' in dataC.hex()[0:4] and len(dataC.hex()) >= 141 :
                    
                        self.data_join=dataC
                        
                    if '0515' in dataC.hex()[0:4] and len(dataC.hex()) <50 :
                    
                        print(remote)
                        self.data_back=dataC
        
 
                        ###
                        
                    


                        



###
                    if remote.send(dataC) <= 0: 
                            break
                if remote in r:
                    global lste
                    global revoe
                    global getin
                    global packet
                    global socktion
                    global back
                    global offline
                    global wlcm
                    global ca
                    global spy
                    dataS = remote.recv(99999)
                    
                    if '1809' in dataS.hex()[26:30]:
                      print('  full team ')
                                #hackg.send(hackw
                    if '0500' in dataS.hex()[0:4] and len(dataS.hex()) > int(1400.1231234234223) and len(dataS.hex()) < int(2000.3242354352345235):
                        lste = dataS
                        revoe = client
                    if '0300' in dataS.hex()[0:4] :
                        #print('yes')
                        C = client
                        
                        if b"http" in dataS and wlcm == True :
                            
                            threading.Thread(target=self.Welcom_Msg_send  ).start()
                            
                            print("Welcome back !!")
                            
           

                   
                        socketsender =client
                        
                        if b'Ranked Mode' in dataS:
                            #print("w")
                            client.send(dataS)
                        else:


                            
                            if b'catbarq' in dataS:
                                vdsf=3
                            else:
                          #                            
                                hackw= dataS
                                hackg= client

                                if len(dataS.hex()) <= 100:
                                    e=2
                                else:
                                    if command ==True:

                                        print("BOT Online !!")

                                    else:
                                        if command ==False:
                                            print("BOT Offline !!")

                    else:
                      if '0500' in dataS.hex()[:4] and b'\x05\x15\x00\x00\x00\x10Z\xca\xf5&T;\x0cA\x01\x16\xe0\x05\xb2\xea\xe4\x0b' in dataC:
                        f=2

                      else: 

##Menuu      
              
#Activation Code !

                        if '1200' in dataS.hex()[0:4] and foxybot==True:
                           if b"#foxy-free" in dataS:
                            command=False
                            threading.Thread(target=self.update1 ).start()
                            
                            foxybot=False

#Back Last Player !
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b"/rec" in dataS:
                            revoe.send(lste)


#/

                            
                            

#foxy



                            
#Back Last Sqoud !
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b"/back" in dataS:
                            back=True
                            threading.Thread(target=self.foxy , args=(self.data_join,)).start()
                            

                            
#back Spam Last Sqoud
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b"/ca" in dataS:
                            ca=True
                            threading.Thread(target=self.walid , args=(self.data_join,)).start()


                            
                            
                            
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b"/ca" in dataS:
                            time.sleep(30.0)
                            ca=False
                            threading.Thread(target=self.Stop_All1).start()
                       

                            

#Spy Normal Last Sqoud !
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b'/spy' in dataS:       
                            client.send(dataS)
                            socktion.send(packet)

                            
                            
#Spam Messag !
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b'/lag' in dataS:     
                            msg=True
                            threading.Thread(target=self.running1 ).start()
                       


#Spam Messag Off !
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b'/-lag' in dataS:
                            msg=False
                            threading.Thread(target=self.Stop_All1 ).start()
                       

#Spam Invite !
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b'/des' in dataS:
                            threading.Thread(target=self.running1 ).start()
                            inviteB=True

                       
#spam Invite Off !
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b'/-des' in dataS:
                            inviteB=False
                            threading.Thread(target=self.Stop_All1 ).start()
                       

#tsq  !
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b'/tsq' in dataS:
                            self.op.send(bytes.fromhex("05150000002000b54843b3c467145c9b8ddcfa4cb489167bd09880be3611b67fec8f0ca66023"))

                            
#5 sqoud !
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b'/s5' in dataS:
                            threading.Thread(target=self.update1 ).start()
                       
                        
                           
                            
                            
                            
                            
                            
                            
                            
                        
                            

#4 sqoud !


                          
#anti kick !
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b"/no" in dataS:
                            offline=True
            
                            


                        if  '0500' in dataS.hex()[0:4] and hide == True  :
                            socktion =client
                        
                            
                            if len(dataS.hex())<=30:
                    
                                hide =True
                            if len(dataS.hex())>=31:
                                packet = dataS
                              
                                hide = False

                        if  '0f00' in dataS.hex()[0:4] and msg==True :

                            threading.Thread(target=self.Stop_All1 ).start()
                       
                            msg = False
                                
                        if  '0f00' in dataS.hex()[0:4] and offline==True :

                            threading.Thread(target=self.running1 ).start()
                       
                            connection.close()
                        if  '0f00' in dataS.hex()[0:4] and wlcm == True:

                            wlcm = False
     
                                
                        if client.send(dataS) <= 0:
                            break



    def Activ_Code(self):
        
        for data in self.Activ_Code1:
            sleep(0.8)
            self.spam_ip_39800.send(data) 
            
            
    def Welcom_Msg_send(self):
        
        for data in self.__list_:
            sleep(0.8)
            self.spam_ip_39800.send(data) 
            
            
    def running1(self):
        
        for data in self.running:
            sleep(0.8)
            self.spam_ip_39800.send(data) 
            
    def Stop_All1(self):
        
        for data in self.Stop_All:
            sleep(0.8)
            self.spam_ip_39800.send(data) 
            
    def update1(self):
        
        for data in self.update:
            sleep(0.8)
            self.spam_ip_39800.send(data) 
            
            
            
            
            

                            
    def foxy( self , data_join):
        global back
       
        while back==True:
            try:
                self.op.send(data_join)
                time.sleep(9999.0)
                #                           0515000000104903408b9e91774e75b990038dddee49
            except Exception as e:
                pass
                            
    #fuction SPAM BACK !
    def walid( self , data_join):
        global ca
        
        while ca==True:
            try:
                self.op.send(data_join)
                time.sleep(1.2)
                self.op.send(self.data_back)
                #                           0515000000104903408b9e91774e75b990038dddee49
            except Exception as e:
                pass

def spam1( data,remote):
    try:
        for i in range(300):
            remote.send(data)
    except:
        pass

#function BOT !
def start_bot():
    try :
        Proxy().run('127.0.0.1',3000)
    except Exception as e:
        sea=2
start_bot()
