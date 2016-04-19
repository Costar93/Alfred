from Action import Action

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
