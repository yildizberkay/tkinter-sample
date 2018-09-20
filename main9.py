#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import csv
import threading
import time

# New frame
class AlertApplication(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        
        self.pack(expand=0, fill='both', padx=0, pady=0)
        
        frameC = Frame(master, bg='red', height=100, width=100, padx=10, pady=10)
        frameC.pack(expand=1, fill='both')

# Main frame
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        
        self.pack(expand=0, fill='both', padx=0, pady=0)

        frameA = Frame(master, bg='#c1c1c1', height=50, padx=10, pady=10)
        frameA.pack(fill='both')

        self.frameB = Frame(master, bg='#e1e1e1', height=100)
        self.frameB.pack(fill='both')

        self.frameD = Frame(master, bg='red', height=100)
        self.frameD.pack(fill='both')

        self.isCycleA = False
        self.isCycleB = False

        StartButton = Button(frameA)
        StartButton["text"] = "Alarm"
        StartButton["command"] = self.getAlert
        StartButton.pack({"side": "left"})

        self.drawPlotA = Button(frameA)
        self.drawPlotA["text"] = "Start Draw A"
        self.drawPlotA["command"] = self.startDrawA
        self.drawPlotA.pack({"side": "left"})

        self.drawPlotB = Button(frameA)
        self.drawPlotB["text"] = "Start Draw B"
        self.drawPlotB["command"] = self.startDrawB
        self.drawPlotB.pack({"side": "left"})

    def getAlert(self):
        rootA = Tk()
        appA = AlertApplication(master=rootA)
        appA.master.title("Alert Window")
        appA.master.geometry("320x240")

    # Graphic A
    def startDrawA(self):
        if self.isCycleA == True:
            self.drawPlotA["text"] = 'Start Draw A'
        else:
            self.drawPlotA["text"] = 'Stop Draw A'

        # self.isCycle bir onceki degerinin tersini aldik.
        self.isCycleA = not self.isCycleA

        thA = threading.Thread(target=self.threadDrawPlotA, args=())
        thA.start()

    def threadDrawPlotA(self):
        while self.isCycleA == True:
            self.drawPlot(self.frameB, "Title 1", "data.csv")
            time.sleep(2)

    # Graphic B
    def startDrawB(self):
        if self.isCycleB == True:
            self.drawPlotB["text"] = 'Start Draw B'
        else:
            self.drawPlotB["text"] = 'Stop Draw B'

        # self.isCycle bir onceki degerinin tersini aldik.
        self.isCycleB = not self.isCycleB

        thA = threading.Thread(target=self.threadDrawPlotB, args=())
        thA.start()

    def threadDrawPlotB(self):
        while self.isCycleB == True:
            self.drawPlot(self.frameD, "Title 2", "data.csv")
            time.sleep(2)

    # - - - - - - - - - - - - - - - - - - - - 
    # - - - - - - - - - - - - - - - - - - - -
    # Common functions
    def drawPlot(self, targetFrame, title, dataFile):
        # Clear widgets inside of frameB
        # https://stackoverflow.com/a/28623781/2094521
        for widget in targetFrame.winfo_children():
            widget.destroy()

        # Source: https://stackoverflow.com/questions/31440167/placing-plot-on-tkinter-main-window-in-python
        # Create sample data with numpy
        x = []
        p = []

        with open(dataFile,'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                x.append(int(row[0]))
                p.append(int(row[1]))

        print x
        print p

        # Define a figure to show data
        fig = Figure(figsize=(6,6))

        # Set plot properties
        a = fig.add_subplot(111)
        a.plot(p, range(max(x)),color='blue')

        a.set_title(title, fontsize=16)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        # Show data on self.frameB
        canvas = FigureCanvasTkAgg(fig, master=targetFrame)
        canvas.get_tk_widget().pack()
        canvas.draw()


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.master.title("Data Monitor")
    app.master.geometry("640x480")
    app.mainloop()