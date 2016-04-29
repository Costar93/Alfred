from Action import Action

class Lights(Action):
    """Lights for Alfred"""
    def __init__(self, cfg):
        super(Lights, self).__init__(cfg)
        self.triggers = ["lights"]

    def do(self, command):
        print "Will set lights in", " ".join(command)
        return "DONE SIR"

    def is_for_you(self, word):
        if word in self.triggers:
            return True
        return False
