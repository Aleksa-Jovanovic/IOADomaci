import numpy as np
import matplotlib.pyplot as plt
import random as rd

NUMBER_OF_POINTS = 10000
pointsFirstX = []
pointsFirstY = []
pointsSecondX = []
pointsSecondY = []

def optimizationFunc1(x1, x2):
    return 2 * pow(x1, 2) + pow(x2, 2)


def optimizationFunc2(x1, x2):
    return -1 * pow((x1 - x2), 2)

def generatePointsFirst():
    for i in range(NUMBER_OF_POINTS):
        x1 = rd.uniform(-1,1)
        x2 = rd.uniform(-1,1)
        pointsFirstX.append(optimizationFunc1(x1,x2))
        pointsFirstY.append(optimizationFunc2(x1,x2))

    return (pointsFirstX, pointsFirstY)   

def generatePointsSecond():
    for i in range(NUMBER_OF_POINTS):
        x1 = rd.uniform(-1,1)
        x2 = rd.uniform(-1,1)
        
        while(True):
            if(not x1 * x2 + 1/4 < 0):
                break
            x1 = rd.uniform(-1, 1)
            x2 = rd.uniform(-1, 1)
        
        pointsSecondX.append(optimizationFunc1(x1,x2))
        pointsSecondY.append(optimizationFunc2(x1,x2))

    return (pointsSecondX, pointsSecondY)     

def findPoints(pointsX, pointsY):
    
    resultsX = []
    resultsY = []
    paretoFrontX = []
    paretoFrontY = []
    
    for i in range(NUMBER_OF_POINTS):
        foundResult = False
        for j in range(NUMBER_OF_POINTS):
            if pointsX[i] > pointsX[j] and pointsY[i] > pointsY[j]:
                foundResult = True
                break
            
        if  foundResult:
            resultsX.append(pointsX[i])
            resultsY.append(pointsY[i])
        else:
            paretoFrontX.append(pointsX[i])
            paretoFrontY.append(pointsY[i])
            
    return (resultsX, resultsY, paretoFrontX, paretoFrontY)

def simulate():
    (pointsFirstX, pointsFirstY) = generatePointsFirst()
    (pointsSecondX, pointsSecondY) = generatePointsSecond()
    
    ###First problem
    print("Simulation - First problem")
    blueX = []
    blueY = []
    redX = []
    redY = []
    
    (blueX, blueY, redX, redY) = findPoints(pointsFirstX, pointsFirstY)
    
    plt.figure(1)
    plt.grid()
    plt.scatter(blueX, blueY, s=0.5, c='lightblue', label='Domain')
    plt.scatter(redX, redY,s=0.5, c='red', label='Pareto front')
    plt.legend()
    
    
    ###Second problem
    print("Simulation - Second problem")
    blueX = []
    blueY = []
    redX = []
    redY = []
    
    (blueX, blueY, redX, redY) = findPoints(pointsSecondX, pointsSecondY)
    
    plt.figure(2)
    plt.grid()
    plt.scatter(blueX, blueY, s=0.5, c='lightblue', label='Domain')
    plt.scatter(redX, redY,s=0.5, c='red', label='Pareto front')
    plt.legend()
    
    plt.show()
    return
    
###MAIN
simulate()