# Imports
import matplotlib.pyplot as plt
import numpy as np

def stepbystepPlot(active,steps,title,label,color,marker):
    plt.xlabel('Step')
    plt.ylabel('Percentage of Active Nodes')
    plt.title(title)
    plt.axis([0, len(steps) + 1, 0, 105])
    plt.plot(steps, active, ls = "-", color = color, label = label,marker = marker)
    if(len(label) > 0):
        legend = plt.legend(loc = 'best', shadow = False)
        frame = legend.get_frame()
        frame.set_facecolor('0.90')

def multiplePlots(active,steps,i,title,label):
        if(i == 0):
                color = "b"
                marker = "o"
        elif(i == 1):
                color = "g"
                marker = "s"
        elif(i == 2):
                color = "r"
                marker = "x"
        elif(i == 3):
                color = "c"
                marker = "+"
        elif(i == 4):
                color = "m"
                marker = "."
        elif(i == 5):
                color = "k"
                marker = "v"
        elif(i == 6):
                color = "chartreuse"
                marker = "^"
        elif(i == 7):
                color = "sienna"
                marker = "*"
        elif(i == 8):
                color = "grey"
                marker = "<"
        else:
                color = "darkgreen"
                marker = ">"
        plt.xlabel('Step')
        plt.ylabel('Percentage of Active Nodes')
        plt.title(title)
        plt.axis([0, len(steps) + 1, min(active) - 1, 105])
        plt.plot(steps, active, ls = "-",color = color, label = label,marker = marker)
        legend = plt.legend(loc = 'best', shadow = False)
        frame = legend.get_frame()
        frame.set_facecolor('0.90')
