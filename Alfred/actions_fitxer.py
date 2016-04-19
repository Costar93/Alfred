

class Action(object):
    """Action to be carried by Alfred"""
    def __init__(self):
        super(Action, self).__init__()

    def do(self, command):
        pass

    def is_for_you(self, word):
        pass

class MusicPlayer(Action):
    """MusicPlayer for Alfred"""
    def __init__(self):
        super(MusicPlayer, self).__init__()
        self.triggers = ["music","audio"]

    def do(self, command):
        print "*Will", " ".join(command), "music*"
        return "DONE"

    def is_for_you(self, word):
        if word in self.triggers:
            return True
        return False

class Lights(Action):
    """Lights for Alfred"""
    def __init__(self):
        super(Lights, self).__init__()
        self.triggers = ["lights"]

    def do(self, command):
        print "*Will set lights in", " ".join(command), "*"
        return "OK"

    def is_for_you(self, word):
        if word in self.triggers:
            return True
        return False
