#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

# New frame
class AlertApplication(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(expand=0, fill='both', padx=0, pady=0)

# Main frame
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        
        self.pack(expand=0, fill='both', padx=0, pady=0)

        frameA = Frame(master, bg='#c1c1c1', height=50, padx=10, pady=10)
        frameA.pack(fill='both')

        frameB = Frame(master, bg='#e1e1e1', height=100)
        frameB.pack(fill='both')

        StartButton = Button(frameA)
        StartButton["text"] = "Alarm"
        StartButton["command"] = self.getAlert
        StartButton.pack({"side": "left"})

    def getAlert(self):
        rootA = Tk()
        app = AlertApplication(master=rootA)
        app.master.title("Alert Window")
        app.master.geometry("320x240")
        app.mainloop()


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.master.title("Data Monitor")
    app.master.geometry("640x480")
    app.mainloop()