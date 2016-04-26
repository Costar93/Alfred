import json

class Channel(object):
    """Channel class"""
    def __init__(self, cfg, name):
        super(Channel, self).__init__()
        self.name = name
        self.cfg = cfg
        #print json.dumps(self.cfg, ident=4)

    def respond(self, response):
        print "RESPONSE: ", response
