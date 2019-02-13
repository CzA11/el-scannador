import socket

#(Using IPv4 address, Using TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)


###port limit = 65535
for portx in range(1, 65536):
    try:
        s.connect(('ad.samsclass.info', portx))
        r = s.recv(1024)
        #When connected to port, sample server should return Congratulations
        if 'Congratulations' in r.decode('utf8'):
            print('[!] HIDDEN SERVICE FOUND: %s ~ %s' % (portx, r.decode('utf8')))
            s.close()
            break
        else:
            print('%s ~ %s' % (portx, r.decode('utf8')))
            s.close()
    except socket.error as err:
        print('%s ~ %s' % (portx, err))
