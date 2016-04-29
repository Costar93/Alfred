from Action import Action

class MusicPlayer(Action):
    """MusicPlayer for Alfred"""
    def __init__(self, cfg):
        super(MusicPlayer, self).__init__(cfg)
        self.triggers = ["music","audio"]

    def do(self, command):
        print "Will", " ".join(command), "music"
        return "DONE SIR"

    def is_for_you(self, word):
        if word in self.triggers:
            return True
        return False
