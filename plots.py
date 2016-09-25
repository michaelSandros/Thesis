# Imports
import matplotlib.pyplot as plt
import numpy as np

def stepbystepPlot(active,steps,title,label,color,marker,ls):
    # xlabel
    plt.xlabel('Step',size = 30)
    plt.xticks(size = 30)
    # ylabel
    plt.ylabel('Percentage of Active Nodes',size = 30)
    plt.yticks(size = 30)
    # title
    plt.title(title,size = 40)
    # x and y axis range
    plt.axis([0, len(steps) + 5, 0, 105])
    #plt.figure(figsize=(8, 6))
    # plot the line
    plt.plot(steps, active, ls = ls, color = color, label = label,marker = marker)
    # if there is a label, show it
    if(len(label) > 0):
        legend = plt.legend(loc = 'best', shadow = False)
        frame = legend.get_frame()
        frame.set_facecolor('0.90')

def multiplePlots(active,steps,i,title,label):
        # different colors and markers
        if(i == 0):
                color = "b"
                marker = "o"
                ls = "-"
        elif(i == 1):
                color = "g"
                marker = "s"
                ls = "--"
        elif(i == 2):
                color = "r"
                marker = "x"
                ls = "-."
        elif(i == 3):
                color = "k"
                marker = "+"
                ls = ":"
        elif(i == 4):
                color = "m"
                marker = "."
                ls = "-"
        elif(i == 5):
                color = "c"
                marker = "v"
                ls = "-"
        elif(i == 6):
                color = "chartreuse"
                marker = "^"
                ls = "-"
        elif(i == 7):
                color = "sienna"
                marker = "*"
                ls = "-"
        elif(i == 8):
                color = "grey"
                marker = "<"
                ls = "-"
        else:
                color = "darkgreen"
                marker = ">"
                ls = "-"
        # xlabel
        plt.xlabel('Step', size = 30)
        plt.xticks(size = 30)
        # ylabel
        plt.ylabel('Percentage of Active Nodes', size = 30)
        plt.yticks(size = 30)
        # title
        plt.title(title, size = 30)
        # x and y label axis range
        plt.axis([0, len(steps) + 5, min(active) - 1, 105])
        # plot the line
        plt.plot(steps, active, ls = ls,color = color, label = label,marker = marker)
        # show legend with labels
        legend = plt.legend(loc = 'best', shadow = False)
        frame = legend.get_frame()
        frame.set_facecolor('0.90')
