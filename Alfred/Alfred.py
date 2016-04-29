#!/usr/bin/env python
# -*- coding: utf-8 -*-

from commandlist import CommandList
import time
import channels as ch
import actions as ac
import yaml
import pprint
import json

class Alfred(object):
    """Class for Alfred Personal Digital Butler
    Will run our house"""

    def __init__(self):
        super(Alfred, self).__init__()
        self.cl = CommandList()

        self._get_config()

        self.channels = []
        self.channels.append(ch.TextChannel())
        self.channels.append(ch.TelegramChannel(self.cfg))

        self.actions = []
        self.actions.append(ac.MusicPlayer(self.cfg))
        self.actions.append(ac.Lights(self.cfg))
        self.actions.append(ac.SensorAction(self.cfg))
        self.actions.append(ac.WakeAction(self.cfg))

    def _get_config(self):
        with open("Alfred.yaml") as f:
            self.cfg = yaml.load(f)

        #print "Configuration:"
        #print json.dumps(self.cfg, indent=4)

    def next_command(self):
        try:
            return self.cl.next()
        except:
            return (None, None)

    def update_channels(self):
        for chan in self.channels:
            while chan.msg_avail():
                self.cl.append((chan, chan.get_msg()))

    def execute_command(self, command):
        print "\n*Will execute", command
        words = command.split()
        first_words = words[0]
        rest_words = words[1:]
        response = None
        for act in self.actions:
            if act.is_for_you(first_words.lower()):
                response = act.do(rest_words)
                break
        else:
            print "Command not found"
        return response

    def mainloop(self):
        #while True:
        #   command = get_command
        #   do_command(command)
        #   update
        while True:
            chan, command = self.next_command()
            if command:
                response = self.execute_command(command)
                chan.respond(response)
            time.sleep(1)
            self.update_channels()

if __name__ == "__main__":
    print "Starting commands!"
    alf = Alfred()
    alf.mainloop()
