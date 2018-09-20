#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.master.title("Data Monitor")
    app.master.geometry("640x480")
    app.mainloop()