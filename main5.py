#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

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

        StartButton = Button(frameA)
        StartButton["text"] = "Alarm"
        StartButton["command"] = self.getAlert
        StartButton.pack({"side": "left"})

        drawPlotA = Button(frameA)
        drawPlotA["text"] = "Draw"
        drawPlotA["command"] = self.drawPlot
        drawPlotA.pack({"side": "left"})

    def getAlert(self):
        rootA = Tk()
        appA = AlertApplication(master=rootA)
        appA.master.title("Alert Window")
        appA.master.geometry("320x240")

    def drawPlot(self):
        # Source: https://stackoverflow.com/questions/31440167/placing-plot-on-tkinter-main-window-in-python
        
        # Source: https://stackoverflow.com/questions/31440167/placing-plot-on-tkinter-main-window-in-python
        # Create sample data with numpy
        x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        p = np.random.randint(100, size=12)

        # Define a figure to show data
        fig = Figure(figsize=(6,6))

        # Set plot properties
        a = fig.add_subplot(111)
        a.plot(p, range(2 + max(x)),color='blue')

        a.set_title("Estimation Grid", fontsize=16)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        # Show data on self.frameB
        canvas = FigureCanvasTkAgg(fig, master=self.frameB)
        canvas.get_tk_widget().pack()
        canvas.draw()

if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.master.title("Data Monitor")
    app.master.geometry("640x480")
    app.mainloop()