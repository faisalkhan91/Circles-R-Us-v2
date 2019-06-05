#!/usr/local/bin/python3

import tkinter
import pygame

def changecirclesize(radius) :

	bbox = drawarea.coords(circleid)
	centerx = (bbox[0] + bbox[2]) / 2
	centery = (bbox[1] + bbox[3]) / 2
	ulx = centerx - radiusvar.get()
	uly = centery - radiusvar.get()
	lrx = centerx + radiusvar.get()
	lry = centery + radiusvar.get()
	drawarea.coords(circleid, (ulx, uly, lrx, lry))

def hitleftmousebutton(ev) :

	newcenterx = ev.x
	newcentery = ev.y
	ulx = newcenterx - radiusvar.get()
	uly = newcentery - radiusvar.get()
	lrx = newcenterx + radiusvar.get()
	lry = newcentery + radiusvar.get()
	drawarea.coords(circleid, (ulx, uly, lrx, lry))

def hitd(ev) :
	global circleid

	if ev.char == "d" :
		drawarea.delete(circleid)
	elif ev.char == "a" :
		circleid = drawarea.create_oval(100, 100, 200, 200, outline = "orange", fill = "")

def changeoutlinecolor(color) :

	drawarea.itemconfig(circleid, outline = color)

def changefill() :

	if fillvar.get() == 1 :
		drawarea.itemconfig(circleid, fill = "red")
	else :
		drawarea.itemconfig(circleid, fill = "")

def changedash() :

	if dashvar.get() == 0 :
		drawarea.itemconfig(circleid, dash = tuple())
	elif dashvar.get() == 1 :
		drawarea.itemconfig(circleid, dash = (2,2))
	else :
		drawarea.itemconfig(circleid, dash = (1,3))

def playmusic() :

	pygame.mixer.music.load("pop.mp3")
	pygame.mixer.music.play()

root = tkinter.Tk()
root.title("Circle's R' Us")
root.lift()
root.minsize(600, 600)
root.configure(bg = "blue")

drawarea = tkinter.Canvas(root, height = 400, width = 400, bg = "light blue")
drawarea.grid(row = 0, column = 0)

circleid = drawarea.create_oval(100, 100, 200, 200, outline = "orange", fill = "")

radiusvar = tkinter.IntVar()
radiusbar = tkinter.Scale(root, from_ = 10, to = 100, resolution = 5, orient = tkinter.HORIZONTAL, variable = radiusvar, command = changecirclesize)
radiusbar.grid(row = 1, column = 0, sticky = "news")

drawarea.bind("<Button-1>", hitleftmousebutton)
drawarea.bind("d", hitd)
drawarea.bind("a", hitd)
drawarea.focus_set()

ocolorvar = tkinter.StringVar()
ocolorvar.set("black")
colors = ["black", "blue", "red", "green", "purple", "orange", "yellow", "brown", "pink", "white" ]

outlinecolor = tkinter.OptionMenu(root, ocolorvar, *colors, command = changeoutlinecolor)
outlinecolor.grid(row = 2, column = 0, sticky = "news")
 
fillvar = tkinter.IntVar()
fillvar.set(0)
fillchoice = tkinter.Checkbutton(root, variable = fillvar, text = "Fill Circle", command = changefill)
fillchoice.grid(row = 3, column = 0, sticky = "news")
 
dashvar = tkinter.IntVar()
dashvar.set(0)
dashchoice1 = tkinter.Radiobutton(root, variable = dashvar, text = "Solid", value = 0, command = changedash)
dashchoice2 = tkinter.Radiobutton(root, variable = dashvar, text = "Dashed", value = 1, command = changedash)
dashchoice3 = tkinter.Radiobutton(root, variable = dashvar, text = "Dotted", value = 2, command = changedash)
dashchoice1.grid(row = 4, column = 0, sticky = "news")
dashchoice2.grid(row = 5, column = 0, sticky = "news")
dashchoice3.grid(row = 6, column = 0, sticky = "news")

musicgo = tkinter.Button(root, text = "Play Music", command = playmusic)
musicgo.grid(row = 7, column = 0, sticky = "news")
pygame.mixer.init()

root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)
root.rowconfigure(2, weight = 1)
root.rowconfigure(3, weight = 1)
root.rowconfigure(4, weight = 1)
root.rowconfigure(5, weight = 1)
root.rowconfigure(6, weight = 1)
root.rowconfigure(7, weight = 1)
root.columnconfigure(0, weight = 1)

root.mainloop()

