from Action import Action
from mpd import (MPDClient, CommandError)

class MusicPlayer(Action):
    """MusicPlayer for Alfred"""
    def __init__(self, cfg):
        super(MusicPlayer, self).__init__(cfg)
        self.triggers = ["music","audio"]
        self.mpd = MPDClient()
        self.mpd.connect("localhost", "6600")

    def _do_update(self, command):
        self.mpd.update()

    def _do_list(self, command):
        llista = self.mpd.list('file')
        print llista
        if len(llista) > 0:
            return "\n".join(llista)
        else:
            return "Empty List SIR"

    def _do_add(self, command):
        song = " ".join(command[1:])
        return self.mpd.addid(song)

    def _do_queue(self,command):
        return "list: %s" % (self.mpd.playlist())

    def _do_clear(self, command):
        return self.mpd.clear()

    def _do_next(self, command):
        return self.mpd.next()

    def _do_previous(self, command):
        return self.mpd.previous()

    def _do_pause(self, command):
        return self.mpd.pause()

    def _do_shuffle(self, command):
        return self.mpd.shuffle()

    def _do_repeat(self, command):
        try:
            if command[1] == "on":
                return self.mpd.repeat(1)
            elif command[1] == "off":
                return self.mpd.repeat(0)
            else:
                return "Error"
        except:
            return "Error"

    def _do_play(self, command):
        try:
            id1 = command[1]
            print id1
            return self.mpd.play(id1)
        except:
            print "no id"
            return self.mpd.play()

    def _do_stop(self, command):
        return self.mpd.stop()

    def do(self, command):
        print "Will", " ".join(command), "music"
        print command
        if command[0] == "update":
            self._do_update(command)
        elif command[0] == "list":
            return self._do_list(command)
        elif command[0] == "add":
            return self._do_add(command)
        elif command[0] == "queue":
            return self._do_queue(command)
        elif command[0] == "play":
            return self._do_play(command)
        elif command[0] == "stop":
            return self._do_stop(command)
        elif command[0] == "clear":
            return self._do_clear(command)
        elif command[0] == "next":
            return self._do_next(command)
        elif command[0] == "previous":
            return self._do_previous(command)
        elif command[0] == "pause":
            return self._do_pause(command)
        elif command[0] == "repeat":
            return self._do_repeat(command)
        elif command[0] == "shuffle":
            return self._do_shuffle(command)
        return "Done SIR"

    def is_for_you(self, word):
        if word in self.triggers:
            return True
        return False
