import socket

#(Using IPv4 address, Using TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)


port = 1000
for portx in range(1, 100):
    try:
        s.connect(('ad.samsclass.info', port))
        r = s.receive(1024)
        #When connected to port, sample server should return Congratulations
        if 'Congratulations' in r.decode('utf8'):
            print('[!] HIDDEN SERVICE FOUND: %s ~ %s' % (port, r.decode('utf8')))
            break
            s.close()
        else:
            print('%s ~ %s' % (port, r.decode('utf8'))
            #s.close()
    except socket.error as e:
        print('%s ~ %s' % (port, err))

    port += 1000
                  
