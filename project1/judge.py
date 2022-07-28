import zmq
B = 32  # number of bits of precision in each random integer

zcontext = zmq.Context()
pubsub = 'tcp://127.0.0.1:6700' #address to use when publish and subscribe
reqrep = 'tcp://127.0.0.1:6701' #address to use when request and reply
pushpull = 'tcp://127.0.0.1:6702' #address to use when push and pull

isock = zcontext.socket(zmq.SUB) #input socket to subscribe
isock.connect(pubsub) #sub socket do connect to address
for prefix in b'01', b'10', b'11':
    isock.setsockopt(zmq.SUBSCRIBE, prefix) #subscribe to b'01', b'10', b'11'

psock = zcontext.socket(zmq.REQ) #push socket to request pythagoras
psock.connect(reqrep) #req socket do connect to address

osock = zcontext.socket(zmq.PUSH) #output socket to push to tally
osock.connect(pushpull) #push socket do connect to address

unit = 2 ** (B * 2)

"""Determine whether each input coordinate is inside the unit circle."""
while True:
    bits = isock.recv_string() #receive string from publisher
    n, m = int(bits[::2], 2), int(bits[1::2], 2)
    psock.send_json((n, m)) #request a message to pythagoras
    sumsquares = psock.recv_json() #receive a reply from pythagoras
    osock.send_string('Y' if sumsquares < unit else 'N') #send string to tally
