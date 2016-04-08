#!/usr/bin/env python
# -*- coding: utf-8 -*-

from commandlist import CommandList
import time
import channels as ch
import actions as ac

class Alfred(object):
    """Class for Alfred Personal Digital Butler

    Will run our house"""

    def __init__(self):
        super(Alfred, self).__init__()
        self.cl = CommandList()
        self.channels = []
        self.channels.append(ch.TextChannel())
        self.actions = []
        self.actions.append(ac.MusicPlayer())

    def next_command(self):
        try:
            return self.cl.next()
        except:
            return None

    def update_channels(self):
        for chan in self.channels:
            while chan.msg_avail():
                self.cl.append(chan.get_msg())

    def execute_command(self, command):
        print "Will execute", command

    def mainloop(self):
        #while True:
        #   command = get_command
        #   do_command(command)
        #   update
        while True:
            command = self.next_command()
            if command:
                self.execute_command(command)
                #print command
            time.sleep(1)
            self.update_channels()

if __name__ == "__main__":
    print "Here be dragons!"
    alf = Alfred()
    alf.mainloop()
