from Tkinter import *

SIZE = 10
COLOR = "yellow"

def callback(event):
    x = (event.x)/10
    y = (event.y)/10
    x1, y1 = ( x*10 ), ( y*10 )
    x2, y2 = ( x*10 + SIZE ), ( y*10 + SIZE )
    
    if rectangles[x][y] == 0:
        rectangles[x][y] = canvas.create_oval( x1, y1, x2, y2, fill = COLOR)
    else:
        #if rectangles[x-1][y] > 0:
        canvas.delete(rectangles[x][y])
        rectangles[x][y] = 0
        
    #print rectangles[x][y]

WIDTH, HEIGHT = 640, 480

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#ffffff")
canvas.bind("<Button-1>", callback)
canvas.pack()

img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

rectangles = [[0 for x in range(48)] for x in range(64)]

#for i in range(0,64):
    #for j in range(0,48):
        #rectangles[i][j] = canvas.create_rectangle(i*10, j*10, 10, 10,fill="black")

mainloop()
