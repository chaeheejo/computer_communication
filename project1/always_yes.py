import zmq

zcontext = zmq.Context()
pubsub = 'tcp://127.0.0.1:6700' #address to use when publish and subscribe
pushpull = 'tcp://127.0.0.1:6702' #address to use when push and pull

"""Coordinates in the lower-left quadrant are inside the unit circle."""
isock = zcontext.socket(zmq.SUB) #input socket to subscribe
isock.connect(pubsub) #sub socket do connect to address
isock.setsockopt(zmq.SUBSCRIBE, b'00') #subscribe to b'00'

osock = zcontext.socket(zmq.PUSH) #output socket to push to tally
osock.connect(pushpull) #push socket do connect to address

while True:
    isock.recv_string() #receive string from publisher
    osock.send_string('Y') #send Y to tally
