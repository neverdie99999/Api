       
###

__list_ = [
b'\x12\x15\x00\x00\x00\xa0nL\x18\x9f\x07\xe8#j\xd9\xbaz\xfd\xd3\xfb\xb6,8\xcc/\x1aF{+\x18J\x03\xe1\xd3\x08C\xa6\xbd2\\\xeb|}\xaa\xe9\xb1\xefE\xe1\xc7\x8d\xd8\x8a\xdb\xe8U\x83\x92"8\xd0\xa6.\x9e\xd3x-\xeb\x97\xb9t\x871\xde\x94\r\xddO\x90<-\x9c\x12N\xac\xc9\x0cq\x10\x97\t\xc8\'\x114\xbf\xd3\x9b%\xab\xe5\x89\xdd,i\xf1\x83\x07\xb1\x82\xe5gV\xe8\x99\x00\n\xe7\xcb\x98Y\x14\x80\x0b2\x0b\x0f9\xcc+l+\x03\xe7\xa3\xd8U|\xc8\xea\xb0\xb8\x080"\x1c{t\xff\xcc\xd1X\xdb\xb4\xb6\xc9\xc2"\x1c\xcdA4\xdex\x87%'
,
b'\x12\x15\x00\x00\x00\xa0\xfd\xaf\xa7\x0b\x88K\t#l\x8b\x1ak\xe2\xf5\xfd\x10\xd8\xfc\xdf\xb9\xbc\xc2\xcd\x1c\x95\xc5\xe9\xfe\xf3\xe1\xb5\xc0\xd4u\x88\xd4\x00\xcf\xa3S\x8bj\x10\xe8\xb0)\n\xb8zo\xa7\xcb\xf0xF\xd6\x1c""\xe4\xe9\x9d\x8bn\x995\x11m\x89{\xaeVC\\b\x9ad\xbcl \xdb\xa9\x1b\xf8xq\x84\x16\rk\xb2\x8f\r\t\xcf}\xa5\x94\xad\xfd2\x1b\x0f+\xb8oM\xa7\x0b,\x11c\xe91\xdb`t\xb7\x0b\x117&\x8a\xe1L\x13\r\xe4/H\xce\xae\x00\xd8\xe6\x15\xf0\x87\xed-Q\x9e\xfe\xf4\x8f\x92\x19\xe1\x93\x9e|\x12k\x86\xc5c$\x9b\xb3f'
]

###
def getreg(Id):    
    # global Id
     
    url = "https://shop2game.com/api/auth/player_id_login"
    headers = {
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
   
    'Origin': 'https://shop2game.com',
    'Referer': 'https://shop2game.com/app',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'accept': 'application/json',
    'content-type': 'application/json',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'x-datadome-clientid': '6h5F5cx_GpbuNtAkftMpDjsbLcL3op_5W5Z-npxeT_qcEe_7pvil2EuJ6l~JlYDxEALeyvKTz3~LyC1opQgdP~7~UDJ0jYcP5p20IQlT3aBEIKDYLH~cqdfXnnR6FAL0',
    }
    payload = {
        "app_id": 100067,
        "login_id": f"{Id}",
        "app_server_id": 0,
    }
    response = requests.post(url, headers=headers, json=payload)
    try:
        if response.status_code == 200:
            return response.json()['region']
        else:
            return(f"ERROR")
    except:
        return("عذرا , لم يتم إيجاد حسابك !!")


def getname(Id):    
    url = "https://shop2game.com/api/auth/player_id_login"
    headers = {
       'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
   
    'Origin': 'https://shop2game.com',
    'Referer': 'https://shop2game.com/app',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'accept': 'application/json',
    'content-type': 'application/json',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'x-datadome-clientid': '6h5F5cx_GpbuNtAkftMpDjsbLcL3op_5W5Z-npxeT_qcEe_7pvil2EuJ6l~JlYDxEALeyvKTz3~LyC1opQgdP~7~UDJ0jYcP5p20IQlT3aBEIKDYLH~cqdfXnnR6FAL0',
    }
    payload = {
        "app_id": 100067,
        "login_id": f"{Id}",
        "app_server_id": 0,
    }
    response = requests.post(url, headers=headers, json=payload)
    try:
        if response.status_code == 200:
            return response.json()['nickname']
        else:
            return(f"ERROR")
    except:
        return("عذرا , لم يتم إيجاد حسابك !! ")
        
def get_status(Id):
    r= requests.get('https://ff.garena.com/api/antihack/check_banned?lang=en&uid={}'.format(Id)) 
    a = "0"
    if  a in r.text :
        return("الحساب مش مبند ")
    else: 
        return("تم تعليقه !!")

def gen_packet(data : str):
    PacketLenght = data[7:10]
    PacketHedar1= data[10:32]
    PayLoad= data[32:34]
    NameLenghtAndName=re.findall('1b12(.*)1a02' , data)[0]
    Name = NameLenghtAndName[2:]
    NameLenght = NameLenghtAndName[:2]
    NewName="5b46463030305d4d6f64652042792040594b5a205445414d"
    NewNameLenght = len(NewName)//2
    NewPyloadLenght=int(int('0x'+PayLoad , 16) - int("0x"+NameLenght , 16))+int(NewNameLenght)
    NewPacketLenght = (int('0x'+PacketLenght , 16)-int('0x'+PayLoad , 16)) + NewPyloadLenght
    packet = data.replace(Name , str((NewName)))
    packet = packet.replace(str('1b12'+NameLenght) , '1b12'+str(hex(NewNameLenght)[2:]))
    packet = packet.replace(PayLoad , str(hex(NewPyloadLenght)[2:]))
    packet = packet.replace(PacketLenght[0] , str(hex(NewPacketLenght)[2:]) )
    return packet


def gen_msgv2_clan(packet  , replay):
    replay  = replay.encode('utf-8')
    replay = replay.hex()
    hedar = packet[0:8]
    packetLength = packet[8:10] #
    paketBody = packet[10:32]
    pyloadbodyLength = packet[32:34]#
    pyloadbody2= packet[34:64]
    pyloadlength = packet[64:66]#
    pyloadtext  = re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
    pyloadTile = packet[int(int(len(pyloadtext))+66):]
    NewTextLength = (hex((int(f'0x{pyloadlength}', 16) - int(len(pyloadtext)//2) ) + int(len(replay)//2))[2:])
    if len(NewTextLength) ==1:
        NewTextLength = "0"+str(NewTextLength)
    NewpaketLength = hex(((int(f'0x{packetLength}', 16) - int(len(pyloadtext)//2) ) - int(len(pyloadlength))) + int(len(replay)//2) + int(len(NewTextLength)))[2:]
    NewPyloadLength = hex(((int(f'0x{pyloadbodyLength}', 16) - int(len(pyloadtext)//2)) -int(len(pyloadlength)) )+ int(len(replay)//2) + int(len(NewTextLength)))[2:]
    finallyPacket = hedar + NewpaketLength +paketBody + NewPyloadLength +pyloadbody2+NewTextLength+ replay + pyloadTile
    return finallyPacket



def gen_msgv2(packet  , replay):
    replay  = replay.encode('utf-8')
    replay = replay.hex()
    hedar = packet[0:8]
    packetLength = packet[8:10] #
    paketBody = packet[10:32]
    pyloadbodyLength = packet[32:34]#
    pyloadbody2= packet[34:60]
    pyloadlength = packet[60:62]#
    pyloadtext  = re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
    pyloadTile = packet[int(int(len(pyloadtext))+62):]
    NewTextLength = (hex((int(f'0x{pyloadlength}', 16) - int(len(pyloadtext)//2) ) + int(len(replay)//2))[2:])
    if len(NewTextLength) ==1:
        NewTextLength = "0"+str(NewTextLength)
    NewpaketLength = hex(((int(f'0x{packetLength}', 16) - int((len(pyloadtext))//2) ) ) + int(len(replay)//2) )[2:]
    NewPyloadLength = hex(((int(f'0x{pyloadbodyLength}', 16) - int(len(pyloadtext)//2))  )+ int(len(replay)//2) )[2:]
    finallyPacket = hedar + NewpaketLength +paketBody + NewPyloadLength +pyloadbody2+NewTextLength+ replay + pyloadTile
    return str(finallyPacket)





 


###
wlcm = True
ca = False
command=False
inviteB = False
back = False
offline = False
spy = False
msg= False
tsq = False
sqd4 = False
sqd2 = False
sqd5 = False
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
        idinfo = True
            
        while True:
            r, w, e = select.select([client, remote], [], [])
            
            if client in r or remote in r:
                global op
                
                if client in r:
                    dataC = client.recv(99999)
                    global stat
                    global getin
                    stat = True
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
                        

                    
                    if "39699" in str(remote) :
                       self.op = remote
         
                    if port ==39699:
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
                    global tsq
                    global sqd4
                    global sqd2
                    global sqd5
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
                        
                        if b"0f00" in dataS and wlcm == True :
                            
                            threading.Thread(target=loop_send  ).start()
                            
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

                        if '1200' in dataS.hex()[0:4]:
                           if b"Foxy-free" in dataS:

                            time.sleep(3.0)
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[00FF00][b][c]تم التفعيل , يمكنك إستخدام البوت الأن .")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[00FF00][b][c]تم التفعيل , يمكنك إستخدام البوت الأن ."))))
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[4dd0e1][b][c]ملاحضة : قد يتم تغير الكود لذالك حسابنا انستقرام")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[4dd0e1][b][c]ملاحضة : قد يتم تغير الكود لذالك حسابنا انستقرام"))))
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[FF0000][b][c]@the_foxy999")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[FF0000][b][c]@the_foxy999"))))
                            command=True
                            
                            
#Back Last Player !
                        if '1200' in dataS.hex()[0:4]:
                           if b"/rec" in dataS:
                            revoe.send(lste)
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[00FF00][b][c]تم إعادته لك !!")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[00FF00][b][c]تم إعادته لك !!"))))
                            
                            
#Back Last Sqoud !
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b"/back" in dataS:
                            back=True
                            threading.Thread(target=self.foxy , args=(self.data_join,)).start()
                            time.sleep(3.0)
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[00FF00][b][c]تم سترجاعك للوضع المكشوف !!")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[00FF00][b][c]تم سترجاعك للوضع المكشوف !!"))))
                            
                            
#back Spam Last Sqoud
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b"/ca" in dataS:
                            ca=True
                            threading.Thread(target=self.walid , args=(self.data_join,)).start()

                            
                            
                            
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b"/ca" in dataS:
                            time.sleep(30.0)
                            ca=False
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[FF0000][b][c]توقف تلقائي للحماية .")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[FF0000][b][c]توقف تلقائي للحماية ."))))
                            

#Spy Normal Last Sqoud !
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b'/spy' in dataS:       
                            time.sleep(1.0)
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[00FF00][b][c]3")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[00FF00][b][c]3"))))
                            time.sleep(1.0)
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[00FF00][b][c]2")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[00FF00][b][c]2"))))
                            time.sleep(1.0)
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[00FF00][b][c]1")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[00FF00][b][c]1"))))
                            time.sleep(1.0)
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[00FF00][b][c]انت غير مكشوف !")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[00FF00][b][c]انت غير مكشوف !"))))
                            
                            client.send(dataS)
                            socktion.send(packet)
                            
                            
#Spam Messag !
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b'/lag' in dataS:     
                            msg=True
                            
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[00FF00][b][c]رسالتك من فضلك :")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[00FF00][b][c]رسالتك من فضلك :"))))
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[4dd0e1][b][c]ملاحضة : لاتترك دردشة على شاشة !!")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[4dd0e1][b][c]ملاحضة : لاتترك دردشة على شاشة !!"))))


#Spam Messag Off !
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b'/-lag' in dataS:
                            msg=False
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[FF0000][b][c]تم توقيفه !")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[FF0000][b][c]تم توقيفه !"))))


#Spam Invite !
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b'/des' in dataS:
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[00FF00][b][c]تم , قم بختيار الفريق !!")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[00FF00][b][c]تم , قم بختيار الفريق !!"))))
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[4dd0e1][b][c]ملاحضة : تتوقف بشكل تلقائيا !!")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[4dd0e1][b][c]ملاحضة : تتوقف بشكل تلقائيا !!"))))
                            inviteB=True
                            time.sleep(30.0)
                            inviteB=False
                            
                            
#spam Invite Off !
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b'/-des' in dataS:
                            inviteB=False
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[FF0000][b][c]تم توقيفه !")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[FF0000][b][c]تم توقيفه !"))))
                            

#tsq  !
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b'/tsq' in dataS:
                            tsq=True
                            threading.Thread(target=self.play , args=(self.data_join,)).start()
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[00FF00][b][c]يمكنك الإستمتاع الأن .")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[00FF00][b][c]يمكنك الإستمتاع الأن ."))))
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[4dd0e1][b][c]ملاحضة : لو تم طردك يمكنك المراسلة عبر الفريق !!")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[4dd0e1][b][c]ملاحضة : لو تم طردك يمكنك المراسلة عبر الفريق !!"))))
                            
                            
#5 sqoud !
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b'/s5' in dataS:
                            sqd5=True
                            threading.Thread(target=self.sqoud5 , args=(self.data_join,)).start()
                            time.sleep(3.0)
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[00FF00][b][c]تحويل الوضع 5 للسكواد .")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[00FF00][b][c]تحويل الوضع 5 للسكواد ."))))
                            

#4 sqoud !
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b'/s4' in dataS:
                            sqd4=True
                            threading.Thread(target=self.sqoud4 , args=(self.data_join,)).start()
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[00FF00][b][c]تحويل الوضع 4 للسكواد .")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[00FF00][b][c]تحويل الوضع 4 للسكواد ."))))


#2 sqoud !
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b'/s2' in dataS:
                            sqd2=True
                            threading.Thread(target=self.sqoud2 , args=(self.data_join,)).start()
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[00FF00][b][c]تحويل الوضع 2 للسكواد .")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[00FF00][b][c]تحويل الوضع 2 للسكواد ."))))
                            
                          
#anti kick !
                        if '1200' in dataS.hex()[0:4] and command==True:
                           if b"/no" in dataS:
                            offline=True
                            client.send(bytes.fromhex(gen_msgv2(dataS.hex() ,"[00FF00][b][c]فوكسي يحميك من الطرد الأن :)")))
                            client.send(bytes.fromhex(str(gen_msgv2_clan(dataS.hex() ,"[00FF00][b][c]فوكسي يحميك من الطرد الأن :)"))))
                            
                            
#info player
                        if idinfo == False:
                            getin.send(bytes.fromhex(gen_msgv2(f"[00FF00][b][c]جلب معلومات لاعب !!",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2_clan(f"[00FF00][b][c]جلب معلومات لاعب !!",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2(f"[4dd0e1][b][c]الإسم : ",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2_clan(f"[4dd0e1][b][c]الإسم : ",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2(f"[ff5722][b][c]{getname(number)}",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2_clan(f"[ff5722][b][c]{getname(number)}",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2(f"[00ff00][b][c] جاري تحميل . . .",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2_clan(f"[00ff00][b][c] جاري تحميل . . .",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2(f"[4dd0e1][b][c]السيرفر : ",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2_clan(f"[4dd0e1][b][c]السيرفر : ",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2(f"[ff5722][b][c]{getreg(number)}",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2_clan(f"[ff5722][b][c]{getreg(number)}",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2(f"[00ff00][b][c] جاري تحميل . . .",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2_clan(f"[00ff00][b][c] جاري تحميل . . .",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2(f"[4dd0e1][b][c]تحقق البند  : ",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2_clan(f"[4dd0e1][b][c]تحقق البند  : ",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2(f"[ff5722][b][c]{get_status(number)}",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2_clan(f"[ff5722][b][c]{get_status(number)}",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2(f"[00FF00][b][c]-----------------------------------",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2_clan(f"[00FF00][b][c]-----------------------------------",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2(f"[FF0000][b][c] insta : @the_foxy999",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2_clan(f"[FF0000][b][c] insta : @the_foxy999",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2(f"[FF0000][b][c] FoxyBot (Demo)",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2_clan(f"[FF0000][b][c] FoxyBot (Demo)",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2(f"[00FF00][b][c]-----------------------------------",newdataS2)))
                            getin.send(bytes.fromhex(gen_msgv2_clan(f"[00FF00][b][c]-----------------------------------",newdataS2)))
                            idinfo = True
    
                           
            
                        if '1200' in dataS.hex()[0:4] and b'++' in dataS and idinfo == True:
                            print(dataS)
                            newdataS2 = dataS.hex()
                            getin = client          
                            idinfo = False
                            text = str(bytes.fromhex(newdataS2))
                            match = re.search(r'\+\+(.*?)\(', text)
                            number = match.group(1)

                            

                        if  '0500' in dataS.hex()[0:4] and hide == True  :
                            socktion =client
                        
                            
                            if len(dataS.hex())<=30:
                    
                                hide =True
                            if len(dataS.hex())>=31:
                                packet = dataS
                              
                                hide = False

                        if  '0f00' in dataS.hex()[0:4] and msg==True :

            
                            msg = False
                                
                        if  '0f00' in dataS.hex()[0:4] and offline==True :

            
                            connection.close()
                        if  '0f00' in dataS.hex()[0:4] and wlcm == True:

                            wlcm = True
     
                                
                        if client.send(dataS) <= 0:
                            break

    def sqoud5( self , data_join):
        global sqd5
       
        while sqd5==True:
            try:
                self.op.send(b'\x05\x03\x00\x00\x01\xd0\x1f\xb5x11P\x90[\xab\xce\xf5\x1d\xd2N\xd7_\xd0\xa2K\x02K\xd1B\x96F\x11K\xc2.`J\xfd5\xa9o\xbcHq\x0b-\x9c\xfe\xc47\x82\x87\xec\x82\x9e3\xa7\x86\x08\xfd-\xd18\xd4\xd2J\x19\xc0\x0f\xbf\xdc\x9f\x15\xc7\x7f\xf8mc\x8b4\xde\x95\xbd\x88n0u\xe8-?J8\x88\xf9\xb6\x944c\x02,C\xfb\x90\xe2)\xf0\xea\xf8\xa7\x88\xf6\xf7f\xd8\x91\xd9\x9e\xb2\xc3{\'qD\x922\x12\x81\x0b<\x80\xd1\xc5!y\x01T\xed\'\x0fRA\xad\xc16\xf2\xa2(\x16\xe0\xbc\x84\xfc\xafy8k\'U\x9d\xe9f\xaax\x8c\x18M5\xbb\xbf\xaa\x03\xa5\xf0\x87F\xf8\xdb\x0es\xb2\xc9\x1e\xc4Q]a\xf6\x89\xa0\xca\xd3\n|\xbdl2QQ\xe8y\xda\xbcC\xd5\x06\xb3$\n\xbeA\xbc\rkD\x16\xc1\x8fh\xefJ\xf2\xd0L8\x1b\xe6\xbfXok%r|\x0c\x85\xc0:W\x917\xe4\xa6\xc6\x02\xefm\x83=\xab\xda\xb3\xeb\xa3\xa5&nZG1\xfb\xfb\x17 \xb6\x0f\x12L\xd8\xfdO\xa2l\xc7\xa9\xfbn\n!\x8d\x88\t\xf5{ M"\xfa\x97R\n\xeb\x99\x00|{q\xc7\t\xe5>\xcch\x8c\x99c\xe0xi\t\x15/\xa9?\x06\xdc\x93\x08Th\xda\xe3N\x16\t\xf3?}\xee"\x8f\xb0X\xc6\xef\xd6\x84kP\xacT\xdb\n\xeb\xb8\xf5\xbc/gQ\xf9\xe2\x88m\xba\xb4\x1c\xba\xf5\xa1\xd8\xcd\x88\xe6\xc1:**V\xb6\x13\xa2\xd3!y\xdc?x\x14\x93\xa5\x02s"\xac\x0c\xb1\xa2\xd3\xc7\x9dI\xfb\x12\xed&#\x0e\x15a\xdfC\xd3\x15\xa2{\xe1{]\xeb\xdb\xa7W\x803\x05%+TC\xf3\xd7|\xd3\x19\xdd\xe9\xc4\x9ar\xc66\xd9=\x02\xbd\xd9Yqh\xf3x\xaanA\xd0\xfdTZ\xbf\x8b\xc0\x88?=\xac\x11\xea\'\x16f\x83\xc7\x11\x1a\x0f2\x9b\xf6\xb6\xa5')
                sqd5 = False
                            

            except Exception as e:
                pass

    def sqoud2( self , data_join):
        global sqd2
       
        while sqd2==True:
            try:
                self.op.send(bytes.fromhex("05150000002098a0bdfd5abbd47ea20d1652a8fa374c78f2fe11f3bf6f5a15ac2dff2ecfd436"))
                sqd2 = False
                            

            except Exception as e:
                pass


    def sqoud4( self , data_join):
        global sqd4
       
        while sqd4==True:
            try:
                self.op.send(bytes.fromhex("05150000002000b54843b3c467145c9b8ddcfa4cb489167bd09880be3611b67fec8f0ca66023"))
                sqd4 = False

            except Exception as e:
                pass
                

    def play( self , data_join):
        global tsq
       
        while tsq==True:
            try:
                self.op.send(bytes.fromhex("051500000020c11276a71758d617ce3164fa4f9ffaa161c8ce760d5624595cf741e6df06ff7a"))
                tsq = False

            except Exception as e:
                pass
                            
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

