import getpass
import socket
import urllib.request

print('Current user is %s'%(getpass.getuser()))
publicip_addr = urllib.request.urlopen('https://api.ipify.org/').read().decode('utf8')
print('Your public ip address is %s'%(publicip_addr))
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('1.1.1.1', 53))
privateip_addr = s.getsockname()[0]
print('Your private ip address is %s'%(privateip_addr))
