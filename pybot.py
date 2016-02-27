#!/usr/bin/env python

import muirc

class pyrcAI:
    
    channel = ""
    
    def __init__(self, connection, channel):
        self.channel = channel
        self.conn = connection
        
    def handleMessage(self, message):
        """
        message: message object from muirc to handle 
        conn: connection object. See muirc and main.py
        """
        if message["command"] == "PRIVMSG" and message["params"][1] == "go away":
            self.conn.quit("Bye, World! :-(")

        if self.messageContains(message, "red"):
            #self.sendMessage("\001ACTION You said red! I like red!\001", self.channel)
            self.sendAction("You said red! I like red!", self.channel)
        
        if self.messageIsFrom(message, "joelghill"):
            self.sendMessage("HI JOEL", "joelghill")
            
    def messageContains(self, message, string):
        """
        message: Message to check contents of
        string: string o text to test against message
        returns: true if message contains string, false otherwise
        """
        if message["command"] != "PRIVMSG": return False
        if(message["params"][1].find(string) == -1):
            return False
        else:
            return True


    def messageIsFrom(self, message, nick):
        """
        message: message to check
        nick: nickname of user
        return: true if message is from nickname given, false otherwise
        """
        return message["nick"] == nick
   
    def quit(self, exitmessage):
        """
        quits irc with exit message
        """
        self.conn.quit(exitmessage)
    
    def sendMessage(self, message, chan = channel):
        """
        sends message to current channel, or person if specified
        """
        self.conn.privmsg(chan, message)
        
    def sendAction(self, action, chan):
        """
        send action command to channel or person
        """
        actionstring = "\001ACTION "+ action + "\001"
        self.sendMessage(actionstring, chan)
        
    