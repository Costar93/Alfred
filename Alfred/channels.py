


class Channel(object):
    """Channel class"""
    def __init__(self, name):
        super(Channel, self).__init__()
        self.name = name

    def respond(self, response):
        print "RESPONSE: ", response

class TextChannel(Channel):
    """Channel class, reads commands from file"""
    def __init__(self, name="TextChannel"):
        super(TextChannel, self).__init__(name)
        self.messages = []
        with open("messages.txt","r") as f:
            for line in f:
                self.messages.append(line)

    def get_msg(self):
        if self.msg_avail():
            return self.messages.pop(0)

    def msg_avail(self):
        return len(self.messages) > 0

import telepot
class AlfredBot(telepot.Bot):
    """AlfredBot is my telegram bot"""
    def __init__(self, token):
        super(AlfredBot, self).__init__(token)
        self.clist = None

    def set_list(self, clist):
        self.clist = clist
        #clist perque no es pot utilitzar list

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == "text":
            command = msg['text']
            if self.clist is not None:
                self.clist.append(command)


class TelegramChannel(Channel):
    """Channel class, recieved commands from Telegram"""
    def __init__(self, name="TelegramChannel"):
        super(TelegramChannel, self).__init__(name)
        self.bot = AlfredBot("209697750:AAHKO6YVX6SUvYKy96hc3NwhfNlDL34kxeg")
        self.messages = []
        self.bot.set_list(self.messages)
        self.bot.notifyOnMessage()

    def get_msg(self):
        if self.msg_avail():
            return self.messages.pop(0)

    def msg_avail(self):
        return len(self.messages) > 0
