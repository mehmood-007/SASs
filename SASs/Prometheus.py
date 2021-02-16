import Monitor

class prometheus(Monitor.monitor):
    """A child prometheus class of monitoring """
    host = '127.0.0.1'  # server host address

   #def __init__(self, host):
    #    self.host = host

    def server(self):
        """A prometheus client configuration"""
        print ("prometheus Server")