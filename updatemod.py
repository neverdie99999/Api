from time          import sleep
from threading     import Thread

import re
import socket
import threading
import select
import requests



SOCKS_VERSION = 5
data_join=b''
op=None
squad = False
hide=None
class Proxy:
    def __init__(self):
        self.username = "username"
        self.password = "username"
        self.spam_level=False
        self.spam_chat= False
        self.botcomendenable=False
        self.inviteB = False
        self.back=False
        self.spy = False
        self.spamantikick=False
        self.command=False
        t = threading.Thread(target=self.udp_server)
        t.start()
        self.__list_ = []
    def handle_client(self, connection):
        # greeting header
        # read and unpack 2 bytes from a client
        version, nmethods = connection.recv(2)

        # get available methods [0, 1, 2]
        methods = self.get_available_methods(nmethods, connection)

        # accept only USERNAME/PASSWORD auth
        if 2 not in set(methods):
            # close connection
            connection.close()
            return

        # send welcome message
        connection.sendall(bytes([SOCKS_VERSION, 2]))

        if not self.verify_credentials(connection):
            return

        # request (version=5)
        version, cmd, _, address_type = connection.recv(4)

        if address_type == 1:  # IPv4
            address = socket.inet_ntoa(connection.recv(4))
        elif address_type == 3:  # Domain name
            domain_length = connection.recv(1)[0]
            address = connection.recv(domain_length)
            address = socket.gethostbyname(address)

        # convert bytes to unsigned short array
        port = int.from_bytes(connection.recv(2), 'big', signed=False)

        try:
            if cmd == 1:  # CONNECT
                remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        

                remote.connect((address, port))


                bind_address = remote.getsockname()
                print("* Connected to {} {}".format(address, port))
            else:
                connection.close()

            addr = int.from_bytes(socket.inet_aton(bind_address[0]), 'big', signed=False)
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
            # return connection refused error
            print(e)
            reply = self.generate_failed_reply(address_type, 5)

        connection.sendall(reply)

        # establish data exchange
        if reply[1] == 0 and cmd == 1:
            
            self.exchange_loop(connection, remote)

        connection.close()

    
    def exchange_loop(self, client:socket.socket, remote:socket.socket):
        while True:
            # wait until client or remote is available for read
            
            r, w, e = select.select([client, remote], [], [])
            
            if client in r:

                data = client.recv(4096)
                #spam chat 
                if '1215' in data.hex()[0:4] and self.spam_chat ==True:
                        
                        b = threading.Thread(target=self.Spam_Chat, args=(data))
                        b.start()
                #Get ip 4 spam
                if "39698" in str(remote) :
                    self.spam_ip = remote
                #Spam Invite 
                if '0515' in data.hex()[0:4] and len(data.hex()) >=820 and self.inviteB==True :
                        try:
                        
                            for i in range(3):
                                threading.Thread(target=self.Spam_Invite , args=(data )).start()
        
                        except:
                            pass

                #AntiKick
                if '0515' in data.hex()[0:4] and len(data.hex()) >= 141 :
                    
                    self.data_join=data
                        
                if '0515' in data.hex()[0:4] and len(data.hex()) <50 :
                    
                    
                    self.data_back=data
        



                if remote.send(data) <= 0:
                    break

            if remote in r:
                data = remote.recv(4096)
                #----Welcom_Msg_send ----
                if '0300' in data.hex()[0:4] :
                    if b"http" in data  :
                        threading.Thread(target=self.Welcom_Msg_send  ).start()
                #----Target ip---
                
                #----Commend Part----
                if '1200' in data.hex()[0:4]:
                    if b"#foxy-free" in data:
                        client.send(bytes.fromhex(self.MakeMsg4NormalChat(data.hex() ,"[00FF00][b]!Welcome")))
                        client.send(bytes.fromhex(str(self.MakeMsg4Clan(data.hex() ,"[00FF00][b]!Welcome"))))
                        client.send(bytes.fromhex(self.MakeMsg4NormalChat(data.hex() ,"[4dd0e1][b]FoxyBot Activ..")))
                        client.send(bytes.fromhex(str(self.MakeMsg4Clan(data.hex() ,"[4dd0e1][b]FoxyBot Activ.."))))
                        client.send(bytes.fromhex(self.MakeMsg4NormalChat(data.hex() ,"[FF0000][b][c]@the_foxy999")))
                        client.send(bytes.fromhex(str(self.MakeMsg4Clan(data.hex() ,"[FF0000][b][c]@the_foxy999"))))
                        self.command=True
                        self.BackSpam_ip = client

                    
                    
                #fo
                if '1200' in data.hex()[0:4]:
                   if b"Dev" in data:
                    client.send(bytes.fromhex(self.MakeMsg4NormalChat(data.hex() ,"[00FF00][b]فوكسي مطور لعبة!")))
                    client.send(bytes.fromhex(str(self.MakeMsg4Clan(data.hex() ,"[00FF00][b]فوكسي مطور لعبة!"))))
                    
                    
  
                    
                #back Spam Last Sqo
                if '1200' in data.hex()[0:4] and self.command==True:
                   if b"/ca" in data:
                    self.spamantikick=True
                    threading.Thread(target=self.SpamAntiKick ).start()
                    
                    
                    
                   
                #Spy Normal Last Squd 
                if '1200' in data.hex()[0:4] and self.command==True:
                   if b'/spy' in data:       
                    
                    client.send(bytes.fromhex(self.MakeMsg4NormalChat(data.hex() ,"[00FF00][b][c]3")))
                    client.send(bytes.fromhex(str(self.MakeMsg4Clan(data.hex() ,"[00FF00][b][c]3"))))
                    
                    client.send(bytes.fromhex(self.MakeMsg4NormalChat(data.hex() ,"[00FF00][b][c]2")))
                    client.send(bytes.fromhex(str(self.MakeMsg4Clan(data.hex() ,"[00FF00][b][c]2"))))
                    
                    client.send(bytes.fromhex(self.MakeMsg4NormalChat(data.hex() ,"[00FF00][b][c]1")))
                    client.send(bytes.fromhex(str(self.MakeMsg4Clan(data.hex() ,"[00FF00][b][c]1"))))
                    
                    client.send(bytes.fromhex(self.MakeMsg4NormalChat(data.hex() ,"[00FF00][b]هاقد عدت يااغبياء")))
                    client.send(bytes.fromhex(str(self.MakeMsg4Clan(data.hex() ,"[00FF00][b]هاقد عدت يااغبياء"))))
                    
                    client.send(bytes.fromhex(self.MakeMsg4NormalChat(data.hex() ,"[00FF00][b]اصمت , انت مخفي !")))
                    client.send(bytes.fromhex(str(self.MakeMsg4Clan(data.hex() ,"[00FF00][b]اصمت ,انت مخفي !"))))
                    
                    client.send(self.packet_back)
                    
                    
                    
                #Spam Messag
                if '1200' in data.hex()[0:4] and self.command==True:
                   if b'/lag' in data:     
                    self.spam_chat=True
                    client.send(bytes.fromhex(self.MakeMsg4NormalChat(data.hex() ,"[00FF00][b][c]رسالتك من فضلك :")))
                    client.send(bytes.fromhex(str(self.MakeMsg4Clan(data.hex() ,"[00FF00][b][c]رسالتك من فضلك :"))))
                #Spam Messag Off
                if '1200' in data.hex()[0:4] and self.command==True:
                   if b'/-lag' in data:
                    self.spam_chat=False
                    client.send(bytes.fromhex(self.MakeMsg4NormalChat(data.hex() ,"[FF0000][b][c]تم توقيفه!")))
                    client.send(bytes.fromhex(str(self.MakeMsg4Clan(data.hex() ,"[FF0000][b][c]تم توقيفه!"))))
                #Spam Invite
                if '1200' in data.hex()[0:4] and self.command==True:
                   if b'/des' in data:
                    client.send(bytes.fromhex(self.MakeMsg4NormalChat(data.hex() ,"[00FF00][b]الفريق من فضلك!")))
                    client.send(bytes.fromhex(str(self.MakeMsg4Clan(data.hex() ,"[00FF00][b]الفريق من فضلك!"))))
                    client.send(bytes.fromhex(self.MakeMsg4NormalChat(data.hex() ,"[4dd0e1][b]توقف : 60 ثانية")))
                    client.send(bytes.fromhex(str(self.MakeMsg4Clan(data.hex() ,"[4dd0e1][b]توقف : 60 ثانية"))))
                    self.inviteB=True               
                #spam Invite Off
                if '1200' in data.hex()[0:4] and self.command==True:
                   if b'/-des' in data:
                    self.inviteB=False
                    client.send(bytes.fromhex(self.MakeMsg4NormalChat(data.hex() ,"[FF0000][b][c]تم توقيفه!")))
                    client.send(bytes.fromhex(str(self.MakeMsg4Clan(data.hex() ,"[FF0000][b][c]تم توقيفه!"))))
                    
   
                #5 sqoud
                if '1200' in data.hex()[0:4] and self.command==True:
                   if b'/s5' in data:
                    self.spam_ip.send(b'\x05\x03\x00\x00\x01\xd0\x1f\xb5x11P\x90[\xab\xce\xf5\x1d\xd2N\xd7_\xd0\xa2K\x02K\xd1B\x96F\x11K\xc2.`J\xfd5\xa9o\xbcHq\x0b-\x9c\xfe\xc47\x82\x87\xec\x82\x9e3\xa7\x86\x08\xfd-\xd18\xd4\xd2J\x19\xc0\x0f\xbf\xdc\x9f\x15\xc7\x7f\xf8mc\x8b4\xde\x95\xbd\x88n0u\xe8-?J8\x88\xf9\xb6\x944c\x02,C\xfb\x90\xe2)\xf0\xea\xf8\xa7\x88\xf6\xf7f\xd8\x91\xd9\x9e\xb2\xc3{\'qD\x922\x12\x81\x0b<\x80\xd1\xc5!y\x01T\xed\'\x0fRA\xad\xc16\xf2\xa2(\x16\xe0\xbc\x84\xfc\xafy8k\'U\x9d\xe9f\xaax\x8c\x18M5\xbb\xbf\xaa\x03\xa5\xf0\x87F\xf8\xdb\x0es\xb2\xc9\x1e\xc4Q]a\xf6\x89\xa0\xca\xd3\n|\xbdl2QQ\xe8y\xda\xbcC\xd5\x06\xb3$\n\xbeA\xbc\rkD\x16\xc1\x8fh\xefJ\xf2\xd0L8\x1b\xe6\xbfXok%r|\x0c\x85\xc0:W\x917\xe4\xa6\xc6\x02\xefm\x83=\xab\xda\xb3\xeb\xa3\xa5&nZG1\xfb\xfb\x17 \xb6\x0f\x12L\xd8\xfdO\xa2l\xc7\xa9\xfbn\n!\x8d\x88\t\xf5{ M"\xfa\x97R\n\xeb\x99\x00|{q\xc7\t\xe5>\xcch\x8c\x99c\xe0xi\t\x15/\xa9?\x06\xdc\x93\x08Th\xda\xe3N\x16\t\xf3?}\xee"\x8f\xb0X\xc6\xef\xd6\x84kP\xacT\xdb\n\xeb\xb8\xf5\xbc/gQ\xf9\xe2\x88m\xba\xb4\x1c\xba\xf5\xa1\xd8\xcd\x88\xe6\xc1:**V\xb6\x13\xa2\xd3!y\xdc?x\x14\x93\xa5\x02s"\xac\x0c\xb1\xa2\xd3\xc7\x9dI\xfb\x12\xed&#\x0e\x15a\xdfC\xd3\x15\xa2{\xe1{]\xeb\xdb\xa7W\x803\x05%+TC\xf3\xd7|\xd3\x19\xdd\xe9\xc4\x9ar\xc66\xd9=\x02\xbd\xd9Yqh\xf3x\xaanA\xd0\xfdTZ\xbf\x8b\xc0\x88?=\xac\x11\xea\'\x16f\x83\xc7\x11\x1a\x0f2\x9b\xf6\xb6\xa5')
                    
                    client.send(bytes.fromhex(self.MakeMsg4NormalChat(data.hex() ,"[00FF00][b]تحويل سكواد 5 تم!")))
                    client.send(bytes.fromhex(str(self.MakeMsg4Clan(data.hex() ,"[00FF00][b][c]تحويل سكواد 5 تم!"))))
                    
                #4 sqoud
                if '1200' in data.hex()[0:4] and self.command==True:
                   if b'/s4' in data:
                    self.op.send(bytes.fromhex("05150000002000b54843b3c467145c9b8ddcfa4cb489167bd09880be3611b67fec8f0ca66023"))
                    client.send(bytes.fromhex(self.MakeMsg4NormalChat(data.hex() ,"[00FF00][b]تحويل سكواد 4 تم!")))
                    client.send(bytes.fromhex(str(self.MakeMsg4Clan(data.hex() ,"[00FF00][b]تحويل سكواد 4 تم!"))))
                #2 sqoud
                if '1200' in data.hex()[0:4] and self.command==True:
                   if b'/s2' in data:
                    self.spam_ip.send(bytes.fromhex("05150000002098a0bdfd5abbd47ea20d1652a8fa374c78f2fe11f3bf6f5a15ac2dff2ecfd436"))
                    client.send(bytes.fromhex(self.MakeMsg4NormalChat(data.hex() ,"[00FF00][b][c]تحويل سكواد 2 تم!")))
                    client.send(bytes.fromhex(str(self.MakeMsg4Clan(data.hex() ,"[00FF00][b]تحويل سكواد 2 تم!"))))
                #----Player Info by ID----    
                if '1200' in data.hex()[0:4] and '33736279' in data.hex() :
                    self.newdataS2=data.hex()
                    self.BackSpam_ip = client
                    self.Target_id= (bytes.fromhex(re.findall(r'33736279(.*?)28' , data.hex()[50:])[0])).decode("utf-8")
                    Thread(target=self.Send_full_information).start()
  
                #----Spy Packet----
                if  '0500' in data.hex()[0:4] and hide == True  :
                    socktion =client
                
                    
                    if len(data.hex())<=30:
            
                        pass
                    if len(data.hex())>=31:
                        self.packet_back = data
                    
                if client.send(data) <= 0:
                    break
                

    
    def generate_failed_reply(self, address_type, error_number):
        return b''.join([
            SOCKS_VERSION.to_bytes(1, 'big'),
            error_number.to_bytes(1, 'big'),
            int(0).to_bytes(1, 'big'),
            address_type.to_bytes(1, 'big'),
            int(0).to_bytes(4, 'big'),
            int(0).to_bytes(4, 'big')
        ])


    def verify_credentials(self, connection):
        
        version = ord(connection.recv(1)) # should be 1


        username_len = ord(connection.recv(1))
        username = connection.recv(username_len).decode('utf-8')
        
        password_len = ord(connection.recv(1))
        
        password = connection.recv(password_len).decode('utf-8')

        if username  and password :
            # success, status = 0
            response = bytes([version, 0])
            connection.sendall(response)
            return True

        # failure, status != 0
        response = bytes([version, 0xFF])
        connection.sendall(response)
        connection.close()
        return False


    def get_available_methods(self, nmethods, connection):
        try:
            methods = []
            for i in range(nmethods):
                methods.append(ord(connection.recv(1)))
            return methods
        except:
            pass

    def run(self, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen()

        print("* Socks5 proxy server is running on {}:{}".format(host, port))

        while True:
            conn, addr = s.accept()
            
            t = threading.Thread(target=self.handle_client, args=(conn,))
            t.start()
    def udp_server(self):
    
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = ('127.0.0.1', 3000)  
        sock.bind(server_address)
        # Listen for incoming datagrams
        print(f'Server listening on {server_address}')

        while True:
            
            data ,addre = sock.recvfrom(1024)  
            if b"/5s" in data:
                Thread(target=self.Sqoud5mode).start()
            if b"/spamchat" in data:
                self.spam_chat=True
            if b"/-spamchat" in data:
                self.spam_chat=False
            if b"/antikick" in data:
                self.spamantikick=True
                Thread(target=self.SpamAntiKick).start()
            if b"/-antikick" in data:
                self.spamantikick=False

            
            # Print the received message
            print(f'Received message: {data}')

        #120000003f08aee0ab841d101220022a3308aee0ab841d10aee0ab841d2204626f74732896d8e3a3064a0f0a09746573745f626f745f20013802520261726a0410011802
    def MakeMsg4NormalChat(self , packet ,replay  ):
        
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
        #120000004108aee0ab841d101220022a3508aee0ab841d10e2aabee50318012204626f747328dfd7e3a3064a0f0a09746573745f626f745f20013802520261726a0410011802
    def MakeMsg4Clan(self ,  packet , replay  ):
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
    def GetIdStatu(self ,Id):
        r= requests.get('https://ff.garena.com/api/antihack/check_banned?lang=en&uid={}'.format(Id)) 
        a = "0"
        if  a in r.text :
            return("الحساب مش مبند ")
        else: 
            return("تم تعليقه !!")
    def GetNameById(self, Id )  :
        
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
    def GetIdRegion(Id):    
        
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
    def Spam_Invite(self , data):
        while self.inviteB==True:
            try:
                self.spam_ip.send(data)
                sleep(0.08)
            except:
                pass
    def Spam_Chat(self , data):
        while self.spam_chat==True:
            try:
                self.spam_ip.send(data)
                sleep(0.08)
            except:
                pass
    def Sqoud5mode(self ) :

        self.spam_ip.send(b'\x05\x03\x00\x00\x01\xd0\x1f\xb5x11P\x90[\xab\xce\xf5\x1d\xd2N\xd7_\xd0\xa2K\x02K\xd1B\x96F\x11K\xc2.`J\xfd5\xa9o\xbcHq\x0b-\x9c\xfe\xc47\x82\x87\xec\x82\x9e3\xa7\x86\x08\xfd-\xd18\xd4\xd2J\x19\xc0\x0f\xbf\xdc\x9f\x15\xc7\x7f\xf8mc\x8b4\xde\x95\xbd\x88n0u\xe8-?J8\x88\xf9\xb6\x944c\x02,C\xfb\x90\xe2)\xf0\xea\xf8\xa7\x88\xf6\xf7f\xd8\x91\xd9\x9e\xb2\xc3{\'qD\x922\x12\x81\x0b<\x80\xd1\xc5!y\x01T\xed\'\x0fRA\xad\xc16\xf2\xa2(\x16\xe0\xbc\x84\xfc\xafy8k\'U\x9d\xe9f\xaax\x8c\x18M5\xbb\xbf\xaa\x03\xa5\xf0\x87F\xf8\xdb\x0es\xb2\xc9\x1e\xc4Q]a\xf6\x89\xa0\xca\xd3\n|\xbdl2QQ\xe8y\xda\xbcC\xd5\x06\xb3$\n\xbeA\xbc\rkD\x16\xc1\x8fh\xefJ\xf2\xd0L8\x1b\xe6\xbfXok%r|\x0c\x85\xc0:W\x917\xe4\xa6\xc6\x02\xefm\x83=\xab\xda\xb3\xeb\xa3\xa5&nZG1\xfb\xfb\x17 \xb6\x0f\x12L\xd8\xfdO\xa2l\xc7\xa9\xfbn\n!\x8d\x88\t\xf5{ M"\xfa\x97R\n\xeb\x99\x00|{q\xc7\t\xe5>\xcch\x8c\x99c\xe0xi\t\x15/\xa9?\x06\xdc\x93\x08Th\xda\xe3N\x16\t\xf3?}\xee"\x8f\xb0X\xc6\xef\xd6\x84kP\xacT\xdb\n\xeb\xb8\xf5\xbc/gQ\xf9\xe2\x88m\xba\xb4\x1c\xba\xf5\xa1\xd8\xcd\x88\xe6\xc1:**V\xb6\x13\xa2\xd3!y\xdc?x\x14\x93\xa5\x02s"\xac\x0c\xb1\xa2\xd3\xc7\x9dI\xfb\x12\xed&#\x0e\x15a\xdfC\xd3\x15\xa2{\xe1{]\xeb\xdb\xa7W\x803\x05%+TC\xf3\xd7|\xd3\x19\xdd\xe9\xc4\x9ar\xc66\xd9=\x02\xbd\xd9Yqh\xf3x\xaanA\xd0\xfdTZ\xbf\x8b\xc0\x88?=\xac\x11\xea\'\x16f\x83\xc7\x11\x1a\x0f2\x9b\xf6\xb6\xa5')
    def SpamAntiKick( self , data_join):
        
        
        while self.spamantikick==True:
            try:
                self.spam_ip.send(data_join)
                sleep(1.2)
                self.spam_ip.send(self.data_back)
            except Exception as e:
                pass     
    def Welcom_Msg_send(self):
        
        for data in self.__list_:
            sleep(0.8)
            self.spam_ip.send(data)  
    def Send_full_information(self):
        self.BackSpam_ip.send(bytes.fromhex(self.MakeMsg4NormalChat(self.newdataS2,f"[00FF00][b][c]لحضة  !!")))
        self.BackSpam_ip.send(bytes.fromhex(self.MakeMsg4Clan(self.newdataS2,f"[00FF00][b][c]لحضة  !!")))
        
        
    
        self.BackSpam_ip.send(bytes.fromhex(self.MakeMsg4NormalChat(self.newdataS2,f"[4dd0e1][b][c]جاري تسجيل دخول الحساب.. ")))
        self.BackSpam_ip.send(bytes.fromhex(self.MakeMsg4Clan(self.newdataS2,f"[4dd0e1][b][c]جاري تسجيل دخول الحساب.. ")))                           
        
        
        self.BackSpam_ip.send(bytes.fromhex(self.MakeMsg4NormalChat(self.newdataS2,f"[ff5722][b][c]{self.GetIdStatu(self.Target_id)}")))
        self.BackSpam_ip.send(bytes.fromhex(self.MakeMsg4Clan(self.newdataS2,f"[ff5722][b][c]{self.GetIdStatu(self.Target_id)}")))                           
        
        self.BackSpam_ip.send(bytes.fromhex(self.MakeMsg4NormalChat(self.newdataS2,f"[00FF00][b][c]-----------------------------------")))
        self.BackSpam_ip.send(bytes.fromhex(self.MakeMsg4Clan(self.newdataS2,f"[00FF00][b][c]-----------------------------------")))    
        
        
        self.BackSpam_ip.send(bytes.fromhex(self.MakeMsg4NormalChat(self.newdataS2,f"[FF0000][b][c] FoxyBot (Beta)")))
        self.BackSpam_ip.send(bytes.fromhex(self.MakeMsg4Clan(self.newdataS2,f"[FF0000][b][c] FoxyBot (Beta)")))    
        
        
        self.BackSpam_ip.send(bytes.fromhex(self.MakeMsg4NormalChat(self.newdataS2,f"[00FF00][b][c]@the_foxy999")))
        self.BackSpam_ip.send(bytes.fromhex(self.MakeMsg4Clan(self.newdataS2,f"[00FF00][b][c]@the_foxy999")))  
        pass
    
def start_bot():
    try :
        Proxy().runs('127.0.0.1',3000)
    except Exception as e:
        sea=2