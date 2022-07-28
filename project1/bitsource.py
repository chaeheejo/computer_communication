import random, zmq, time
B = 32  # number of bits of precision in each random integer

zcontext = zmq.Context()
fromclient = 'tcp://127.0.0.1:67004' #address to use when socket sent to bitsource from client
pubsub = 'tcp://127.0.0.1:6700' #address to use when publish and subscribe

def ones_and_zeros(digits):
    """Express `n` in at least `d` binary digits, with no special prefix."""
    return bin(random.getrandbits(digits)).lstrip('0b').zfill(digits)


isock = zcontext.socket(zmq.PULL) #input socket to pull from client
isock.bind(fromclient) #pull socket do bind to address

osock = zcontext.socket(zmq.PUB) #output socket to publish
osock.bind(pubsub) #pub socket do bind to address

num = isock.recv_string() #receive num from client
inum=int(num) #change type of num to int type

"""Produce random points in the unit square."""
for i in range(inum): #Repeat the statement for as many times as the num of times
    osock.send_string(ones_and_zeros(B*2)) #send the socket to subscribers
    time.sleep(0.01)

