import numpy as np
import math
import random as rand

S=[2.424595205726587e-01, 1.737226395065819e-01, 1.315612759386036e-01,
   1.022985539042393e-01, 7.905975891960761e-02, 5.717509542148174e-02,
   3.155886625106896e-02, -6.242228581847679e-03, -6.565183775481365e-02,
   -8.482380513926287e-02, -1.828677714588237e-02, 3.632382803076845e-02,
   7.654845872485493e-02, 1.152250132891757e-01, 1.631742367154961e-01,
   2.358469152696193e-01, 3.650430801728451e-01, 5.816044173713664e-01,
   5.827732223753571e-01, 3.686942505423780e-01]

R = 15
F = 0.8
CR = 0.9

def optimizationFunction(x):
    sum = 0
    if ((math.sqrt(pow(x[0],2) + pow(x[1],2)) < R) and (math.sqrt(pow(x[2],2) + pow(x[3],2)) < R)):
        for i in range (20):    
            sum += pow(
                    (x[4]/math.sqrt(pow((15*math.cos(2*math.pi*i/20) - x[0]),2) + pow((15*math.sin(2*math.pi*i/20) - x[1]),2)) 
                    + x[5]/math.sqrt(pow((15*math.cos(2*math.pi*i/20) - x[2]),2) + pow((15*math.sin(2*math.pi*i/20) - x[3]),2)) - S[i]),2)
    else:
        sum = 100
        
    return sum

def crossOver(x, y, z):
    for i in range(50):
        randomIndex = rand.randint(0,5)
        for j in range(6):
            if (randomIndex==j):
                y[i][j] = z[i][j]
            else:
                if (CR > rand.uniform(0,1)):
                    y[i][j] = z[i][j]
                else:
                    y[i][j] = x[i][j]
    return y

def differentialEvolution():
    result = []
    finished = False
    finishedIndex = 0
    lastBest = 1
    
    x = np.zeros((50,6))
    z = np.zeros((50,6))
    y = np.zeros((50,6))
    
    #Generate init values
    for i in range(50):
        for j in range(6):
            x[i][j] = rand.randint(-15, 15)
            
    while(not finished):
        #Check current population
        for i in range(50):
            currentOptimization = optimizationFunction(x[i])
            if(currentOptimization < pow(10,-14)):
                finished = True
                if(currentOptimization < lastBest):
                    ###print("Current best = " , currentOptimization)
                    lastBest = currentOptimization
                    finishedIndex = i
        if(finished == True):
            continue
        
        #Calculateing all the z
        for i in range(50):
            #Get 3 random unique indexs
            repeat = True
            selected = []
            while(repeat):
                repeat = False
                selected = rand.sample(range(0, 50), 3)
                for j in range(3):
                    if (selected[j] == i):
                        repeat = True
                        break
            z[i] = x[selected[0]] + F*(x[selected[1]] - x[selected[2]])
            
        crossOver(x, y, z)
        for i in range(50):
            if (optimizationFunction(x[i]) > optimizationFunction(y[i])):
                    x[i] = y[i]
                
    result = x[finishedIndex]
    return result



###MAIN
finalResult = differentialEvolution()
print("[Xp1, Yp1, Xp2, Yp2, A1, A2] <==> ",finalResult)
print("Optimization function value = ", optimizationFunction(finalResult))
        