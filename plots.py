# Imports
import matplotlib.pyplot as plt
import numpy as np

def stepbystepPlot(active,steps,title,label,color):
    plt.xlabel('Step')
    plt.ylabel('Percentage of Active Nodes')
    plt.title(title)
    plt.axis([0, len(steps) + 1, 0, 105])
    plt.plot(steps, active, ls = "-",color = color, label = label)
    if(len(label) > 0):
        legend = plt.legend(loc = 'best', shadow = False)
        frame = legend.get_frame()
        frame.set_facecolor('0.90')

def multiplePlots(active,steps,i,title,label):
        if(i == 0):
                color = "b"
        elif(i == 1):
                color = "g"
        elif(i == 2):
                color = "r"
        elif(i == 3):
                color = "c"
        elif(i == 4):
                color = "m"
        elif(i == 5):
                color = "k"
        elif(i == 6):
                color = "chartreuse"
        elif(i == 7):
                color = "sienna"
        elif(i == 8):
                color = "grey"
        else:
                color = "darkgreen"
        plt.xlabel('Step')
        plt.ylabel('Percentage of Active Nodes')
        plt.title(title)
        plt.axis([0, len(steps) + 1, min(active) - 1, 105])
        plt.plot(steps, active, ls = "-",color = color, label = label)
        legend = plt.legend(loc = 'best', shadow = False)
        frame = legend.get_frame()
        frame.set_facecolor('0.90')
