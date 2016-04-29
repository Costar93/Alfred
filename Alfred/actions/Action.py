class Action(object):
    """Action to be carried by Alfred"""
    def __init__(self, cfg):
        super(Action, self).__init__()
        self.cfg = cfg

    def do(self, command):
        pass

    def is_for_you(self, word):
        pass
