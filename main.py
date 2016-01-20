import muirc
from threading import Thread


def userInput():
    while connected:
        msg = raw_input();
        if connected:
            conn.privmsg("#local", msg)

connected = False;

conn = muirc.Connection(("172.16.1.88", 6667))
conn.nick("AnnoyingBot")
conn.UsEr("a", "a", "a", "a")

state = "wait_motd"
for message in conn:
     if message["command"] == "372":
        print(message["params"][1])
     if message["command"] == "PRIVMSG" and message["params"][1] == "go away":
        conn.quit("Bye, World! :-(")
        connected = False
     
     if message["command"] == "PRIVMSG":
        text = message["user"] + ': ' + message["params"][1]
        print(text)
        
     if state == "wait_motd":
         # 376 => MOTD ends
         if message["command"] == "376":
             state = "end_motd"

     # Join #muirc
     if state == "end_motd":
         conn.join("#local")
         state = "wait_join"

     # Wait for join ack
     if state == "wait_join":
         if message["command"] == "JOIN":
                connected = True
                t = Thread(target=userInput)
                t.start()
                state = "hello_world"

     # Send "Hello, World! :-)" to the #muirc channel
     if state == "hello_world":
         conn.privmsg("#local", "\001ACTION yo\001")
         #conn.action("Is waving like a madman....")