#!/usr/bin/env python
# -*- coding: utf-8 -*-

from commandlist import commandlist
import time

class Alfred(object):
    """Class for Alfred Personal Digital Butler

    Will run our house"""

    def __init__(self):
        super(Alfred, self).__init__()
        self.cl = CommandList()

    def next_command(self):
        try:
            return self.cl.next()
        except:
            return None

    def mainloop(self):
        #while True:
        #   command = get_command
        #   do_command(command)
        #   update
        while True:
            command = self.next_command()
            time.sleep(1)

if __name__=="__main__":
    print "Here be dragons!"
