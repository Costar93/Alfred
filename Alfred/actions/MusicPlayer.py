from Action import Action
from mpd import (MPDClient, CommandError)

class MusicPlayer(Action):
    """MusicPlayer for Alfred"""
    def __init__(self, cfg):
        super(MusicPlayer, self).__init__(cfg)
        self.triggers = ["music","audio"]
        self.mpd = MPDClient()
        self.mpd.connect("localhost", "6600")
        self.mpd.consume(0)

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
        self.mpd.add(song)
        return "Song %s Added SIR" % (song)

    def _do_queue(self,command):
        return "list: %s" % (self.mpd.playlist())

    def _do_clear(self, command):
        self.mpd.clear()
        return "Clear Done SIR"

    def _do_next(self, command):
        self.mpd.next()
        return "Next Song Done SIR"

    def _do_previous(self, command):
        self.mpd.previous()
        return "Previous Song Done SIR"

    def _do_pause(self, command):
        self.mpd.pause()
        return "Music Paused SIR"

    def _do_shuffle(self, command):
        self.mpd.shuffle()
        return "Music shuffled SIR"

    def _do_repeat(self, command):
        try:
            if command[1] == "on":
                self.mpd.repeat(1)
                return "Repeat Set On SIR"
            elif command[1] == "off":
                self.mpd.repeat(0)
                return "Repeat Set Off SIR"
            else:
                return "Error SIR"
        except:
            return "Error SIR"

    def _do_play(self, command):
        try:
            songpos = command[1]
            self.mpd.play(int(songpos))
            return "Playing %s Song Done SIR" % (songpos)
        except:
            self.mpd.play()
            return "Music Playing SIR"

    def _do_stop(self, command):
        self.mpd.stop()
        return "Music Stoped SIR"

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
