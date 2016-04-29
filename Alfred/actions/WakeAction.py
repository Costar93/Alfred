from Action import Action
import subprocess
from wakeonlan import wol

class WakeAction(Action):
    """MusicPlayer for Alfred"""
    def __init__(self, cfg):
        super(WakeAction, self).__init__(cfg)
        self.triggers = ["wake"]

    def do(self, command):
        print "Will wake the computer", " ".join(command)
        ret = "Unknown PC SIR"
        for arg in command:
            for pc in self.cfg["wol"]["pcs"]:
                if arg == pc["nom"]:
                    print "Wake: ", pc["mac"]
                    wol.send_magic_packet(pc["mac"])
                    ret = "Wake Done SIR"
        return ret

    def is_for_you(self, word):
        if word in self.triggers:
            return True
        return False
