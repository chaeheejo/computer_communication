import zmq

zcontext = zmq.Context()
toclient = 'tcp://127.0.0.1:67003' #address to use when socket sent to client from tally
fromclient = 'tcp://127.0.0.1:67004' #address to use when socket sent to bitsource from client

osock=zcontext.socket(zmq.PUSH) #output socket to push
osock.connect(fromclient) #connect to the address 'fromclient'
num = int(input('number of data : '))

if num<0 :
    print('the number must be positive')

osock.send_string(str(num)) #send the 'num' received

isock=zcontext.socket(zmq.PULL) #input socket to pull
isock.bind(toclient) #bind to the address 'toclient'

while True:
    result = isock.recv_string() #receive string from isock
    print(result) #print number of iterations and pi-value from tally
