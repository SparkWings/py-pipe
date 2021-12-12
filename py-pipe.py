import os, argparse
from socket import *
from threading import Thread

# Command line option handling
parser = argparse.ArgumentParser(prog=os.path.basename(__file__), description='A simple Python TCP port forwarding tool inspired by fpipe. Accepts a connection from Computer-A and port forwards all traffic to Computer-C, making it appear as if Computer-B (this computer) sent the traffic!')

# Optional arguments
parser.add_argument('-v', '--verbose', '--debug', dest='debug', help='verbose mode: sent and received packets will appear in stdout', default=False, action='store_true')
parser.add_argument('-i', '--ip', metavar='X.X.X.X', dest='laddr', help='listens on the specified IP instead of globally. IP Address must be assigned locally!', default='0.0.0.0')

# Required arguments
required_args = parser.add_argument_group('required arguments')
required_args.add_argument('-lport', metavar='<port>', dest='lport', help='local port to listen on', required=True, type=int)
required_args.add_argument('-raddr', metavar='<X.X.X.X>', dest='raddr', help='remote IPv4 Address to forward to', required=True)
required_args.add_argument('-rport', metavar='<port>', dest='rport', help='remote port to forward to', required=True, type=int)
args = parser.parse_args()

# Variable Assignment
lport = args.lport
raddr = args.raddr
rport = args.rport
debug = args.debug
laddr = args.laddr

# Listening socket
redirect = socket(AF_INET, SOCK_STREAM)
redirect.bind((laddr, lport))
redirect.listen(1)
print('[*] Listening on ' + laddr + ':' + str(lport))
client,address = redirect.accept()
print('[*] Client connection received on ' + laddr + ':'+str(lport))
# Forwarding socket
forwardclient = socket(AF_INET, SOCK_STREAM)
forwardclient.connect((raddr, rport))
print('[*] Connected! Forwarding ' + laddr + ':' + str(lport) + ' to ' + raddr + ':' + str(rport))

# Forwarding data handler
def serve_client():
    while 1:
        data = client.recv(1024)
        forwardclient.sendall(data)
        
        if debug:
            print('-> ' + str(data))
        
        if not data:
            print('[*] Connection terminated by client')
            os._exit(0)
            
        if data == 'bye\n':
            print('[*] Exit command received, closing connection')
            os._exit(0)
    
# Client data handler    
def serve_forward():
    while 1:
        backdata = forwardclient.recv(1024)
        client.sendall(backdata)
        
        if debug:
            print('<- ' + str(backdata))
        
        if not backdata:
            print('[*] Connection terminated by remote host')
            os._exit(0)
      
# Client thread creation      
client_thread = Thread(target=serve_client)
client_thread.setDaemon(True)
client_thread.start()
  
# Forwarding thread creation  
forward_thread = Thread(target=serve_forward)
forward_thread.setDaemon(True)
forward_thread.start()            

# Keep-alive loop
while 1:
    pass
