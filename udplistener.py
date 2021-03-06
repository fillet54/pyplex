import threading
import socket

class udplistener(threading.Thread):
    def __init__(self, queue):
        super(udplistener, self).__init__()
        self.queue = queue
        self._stop = threading.Event()

    def run(self):
        print "Started UDP listener"
       
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
        sock.bind(("0.0.0.0",9777))
        sock.settimeout(2)
        while not self.stopped():
            try:
                data, addr = sock.recvfrom(1024)
                index = data.rindex("\x02");
                command = data[index+1:-1]
                print "Got UDP Command %s" % command
                self.queue.put((command, [u'']))
            except socket.timeout:
                pass

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()
