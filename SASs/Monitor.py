

class monitor:
    """A monitoring component base class"""
    host = '127.0.0.1'  # server host address

    #def __init__(self, host):
    #    self.host = host

    def server(self):
        """A monitoring client configuration"""
        print ("Server")

    def client(self):
        """A monitoring server configuration"""
        print ("Client")