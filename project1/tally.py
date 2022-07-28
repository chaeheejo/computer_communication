import zmq

zcontext = zmq.Context()
toclient = 'tcp://127.0.0.1:67003' #address to use when socket sent to client from tally
pushpull = 'tcp://127.0.0.1:6702' #address to use when push and pull

"""Tally how many points fall within the unit circle, and print pi."""
isock = zcontext.socket(zmq.PULL) #input socket to pull from judge and always_yes
isock.bind(pushpull) #pull socket do bind to address
p = q = 0

osock = zcontext.socket(zmq.PUSH) #output socket to push the result to client
osock.connect(toclient) #push socket do bind to address

while True:
    decision = isock.recv_string() #receive string from judge and always_yes
    q += 1 #increase the number of iterations
    if decision == 'Y':
        p += 4
    osock.send_string(str(q)+' '+str(p/q)) #send q(number of iterations) and p/q(pi-value) to client
