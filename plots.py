# Imports
import matplotlib.pyplot as plt
import numpy as np

def activePlot(active1,active2,active3,active4,active5,x):

    flattend1 = [val for sublist in active1 for val in sublist]
    flattend2 = [val for sublist in active2 for val in sublist]
    flattend3 = [val for sublist in active3 for val in sublist]
    flattend4 = [val for sublist in active4 for val in sublist]
    flattend5 = [val for sublist in active5 for val in sublist]
    flattendx = [val for sublist in x for val in sublist]
    plt.ylabel('active set size')
    plt.xlabel('iteration')
    
    plt.plot(flattendx, flattend1, ls = "--", label="Random Threshold")
    plt.plot(x, flattend2, ls = "-", label="Random Threshold/ Out Degree")
    plt.plot(x, flattend3, ls = "-.", label="Degree Centrality Threshold")
    plt.plot(x, flattend4, ls = ":", label="Betweeness Centrality Threshold")
    plt.plot(x, flattend5, ls ="-",label="Mixed Centrality Threshold")
    
    legend = plt.legend(loc='best', shadow=False)
    frame = legend.get_frame()
    frame.set_facecolor('0.90')
    plt.show()

def timePlot(time1,x):
    flattend1 = [val for sublist in time1 for val in sublist]
    flattendx = [val for sublist in x for val in sublist]
    plt.plot(flattendx, flattend1, ls = "--", label="Random Threshold")
    legend = plt.legend(loc='best', shadow=False)
    frame = legend.get_frame()
    frame.set_facecolor('0.90')
    plt.show()

def stepbystep(active,steps,title,label):
    plt.xlabel('Step')
    plt.ylabel('Percentage of Active Nodes')
    plt.title(title)
    plt.axis([0, len(steps) + 1, min(active) - 1, 105])
    plt.plot(steps, active, ls = "-",color = 'red', label = label)
    legend = plt.legend(loc = 'best', shadow = False)
    frame = legend.get_frame()
    frame.set_facecolor('0.90')
    plt.show()

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
