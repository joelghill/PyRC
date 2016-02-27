from Tkinter import *

WIDTH = 640
HEIGHT = 480
COLOR = "Green"
SIZE = 4

def paint( event ):
   x1, y1 = ( event.x - SIZE/2 ), ( event.y - SIZE/2 )
   x2, y2 = ( event.x + SIZE/2 ), ( event.y + SIZE/2 )
   w.create_oval( x1, y1, x2, y2, fill = COLOR, border=0 )

master = Tk()
master.title( "Painting using Ovals" )

w = Canvas(master, width=WIDTH,height=HEIGHT)
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )

message = Label( master, text = "Press and Drag the mouse to draw" )
message.pack( side = BOTTOM )
    
mainloop()
