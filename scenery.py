from tkinter import *
import math

root = Tk()
root.geometry('900x600')
canvas = Canvas(root, width=900, height=600, background="skyblue")

# tree
canvas.create_line(680, 300, 680, 600, fill="brown", width=20)
canvas.create_line(700, 300, 700, 600, fill="brown", width=20)
canvas.create_line(600, 300, 680, 400, fill="brown", width=20)
canvas.create_line(800, 400, 700, 500, fill="brown", width=20)

canvas.create_polygon(830, 400, 850, 450, 800, 450, 750, 400, fill="green")
canvas.create_polygon(750, 400, 830, 350, 830, 400, fill="#4cbb17")
canvas.create_polygon(830, 400, 830, 350, 880, 420, 850, 450, fill="#7fff00")
canvas.create_polygon(450, 310, 810, 310, 840, 280, 750, 200, fill="#31ba06")
canvas.create_polygon(840, 280, 850, 180, 750, 200, fill="#33c007")
canvas.create_polygon(750, 200, 700, 120, 850, 180, fill="#3de308")
canvas.create_polygon(700, 120, 750, 200, 650, 150, fill="#3dda0c")
canvas.create_polygon(650, 150, 750, 200, 450, 310, fill="#33c007")
canvas.create_polygon(700, 120, 650, 150, 550, 140, fill="#4fff17")
canvas.create_polygon(650, 150, 550, 140, 500, 200, fill="#41ec0a")
canvas.create_polygon(500, 200, 450, 310, 700, 120, fill="#3de308")
canvas.create_polygon(500, 200, 450, 310, 470, 210, fill="#6eff17")
canvas.create_rectangle(0, 580, 900, 600, fill="green", outline="green")

# fruit
canvas.create_oval(700, 280, 710, 290, fill="yellow", outline="yellow")
canvas.create_oval(650, 240, 660, 250, fill="yellow", outline="yellow")
canvas.create_oval(750, 210, 760, 220, fill="yellow", outline="yellow")
canvas.create_oval(510, 280, 520, 290, fill="yellow", outline="yellow")
canvas.create_oval(550, 220, 560, 230, fill="yellow", outline="yellow")

# bird
canvas.create_polygon(720, 400, 740, 395, 720, 415, fill="#acb5bb")
canvas.create_polygon(740, 395, 720, 415, 720, 435, fill="#cad4db")
canvas.create_polygon(720, 400, 720, 415, 710, 415, fill="#fbbd4e", outline="grey")   # beak
canvas.create_oval(723, 403, 728, 408, fill="black")
canvas.create_polygon(730, 460, 720, 435, 750, 420, 770, 480, fill="#cad4db")
canvas.create_polygon(730, 460, 720, 465, 740, 465)
canvas.create_polygon(720, 435, 750, 420, 770, 450, fill="#d6a3fa")
canvas.create_polygon(720, 435, 740, 395, 750, 420, fill="#7806c6")
canvas.create_polygon(750, 420, 780, 440, 730, 430, fill="#7806c6")

# sun
for i in range(0, 360, 20):
    x1 = (40 * math.sin((2 * math.pi * i) / 360)) + 150
    y1 = (40 * math.cos((2 * math.pi * i) / 360)) + 100
    canvas.create_line(150, 100, x1, y1, fill="orange", width=2)
canvas.create_oval(130, 80, 170, 120, fill="orange", outline="orange")

# cow
canvas.create_rectangle(300, 480, 250, 530, fill="white", outline="white")
canvas.create_oval(225, 480, 275, 530, fill="white", outline="white")
canvas.create_rectangle(300, 460, 330, 500, fill="white")
canvas.create_oval(290, 480, 340, 510, fill="black")
canvas.create_polygon(300, 460, 306, 460, 303, 450, fill="black")
canvas.create_polygon(324, 460, 330, 460, 327, 450, fill="black")
canvas.create_oval(305, 470, 310, 475, fill="black")
canvas.create_oval(320, 470, 325, 475, fill="black")
canvas.create_oval(300, 490, 305, 495, fill="grey")
canvas.create_oval(325, 490, 330, 495, fill="grey")
canvas.create_line(285, 530, 285, 580, width=10, fill="white")
canvas.create_line(295, 530, 310, 560, width=10, fill="white")
canvas.create_line(310, 559, 310, 580, width=10, fill="white")
canvas.create_line(235, 510, 230, 578, width=10, fill="white")
canvas.create_line(235, 510, 245, 578, width=10, fill="white")
canvas.create_line(310, 570, 310, 580, width=10, fill="black")
canvas.create_line(285, 570, 285, 580, width=10, fill="black")
canvas.create_line(230, 570, 230, 580, width=10, fill="black")
canvas.create_line(245, 570, 245, 580, width=10, fill="black")
canvas.create_oval(285, 460, 300, 470, fill="white")
canvas.create_oval(330, 460, 345, 470, fill="white")
canvas.create_line(226, 500, 220, 550, width=2, fill="white")
canvas.create_polygon(220, 550, 225, 555, 215, 555, fill="black")

canvas.create_oval(350, 100, 450, 150, fill="white", outline="white")
canvas.create_oval(400, 80, 500, 160, fill="white", outline="white")
canvas.create_oval(450, 100, 550, 150, fill="white", outline="white")

canvas.create_oval(150, 200, 250, 250, fill="white", outline="white")
canvas.create_oval(200, 180, 300, 260, fill="white", outline="white")
canvas.create_oval(250, 200, 350, 250, fill="white", outline="white")

canvas.create_polygon(100, 580, 120, 580, 80, 560, fill="#4cbb17")
canvas.create_polygon(100, 580, 120, 580, 135, 560, fill="#4cbb17")
canvas.create_polygon(100, 580, 120, 580, 110, 550, fill="green")

canvas.create_polygon(400, 580, 420, 580, 380, 560, fill="#4cbb17")
canvas.create_polygon(400, 580, 420, 580, 435, 560, fill="#4cbb17")
canvas.create_polygon(400, 580, 420, 580, 410, 550, fill="green")

canvas.create_polygon(700, 580, 720, 580, 680, 560, fill="#4cbb17")
canvas.create_polygon(700, 580, 720, 580, 735, 560, fill="#4cbb17")
canvas.create_polygon(700, 580, 720, 580, 710, 550, fill="#4cbb17")

canvas.pack()
root.mainloop()
