import zmq

zcontext = zmq.Context()
reqrep = 'tcp://127.0.0.1:6701' #address to use when request and reply

"""Return the sum-of-squares of number sequences."""
zsock = zcontext.socket(zmq.REP) #zsock to request
zsock.bind(reqrep) #req socket do bind to address
while True:
    numbers = zsock.recv_json() #receive a request from judge
    zsock.send_json(sum(n * n for n in numbers)) #send a reply calculating number
