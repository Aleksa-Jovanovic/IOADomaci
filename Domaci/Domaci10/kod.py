import math 
import numpy as np
import random as rand

POPULATION_SIZE = 60

#Main points (x,y,z)
A = [1,5,1] 
B = [3,2,0]
C = [5,7,1]
D = [6,3,3]

#Coefficient
W = 0.729
C1 = 1.494
C2 = 1.494
Vmax = 0.2

def optimizationFunction(x):
    return math.sqrt(pow(A[0] - x[0],2) + pow(A[1] - x[1],2) + pow(A[2] - x[2],2)) + math.sqrt(pow(B[0] - x[0],2) + pow(B[1] - x[1],2) + pow(B[2] - x[2],2)) + math.sqrt(pow(x[0] - x[3],2) + pow(x[1] - x[4],2) + pow(x[2] - x[5],2)) + math.sqrt(pow(C[0] - x[3],2) + pow(C[1] - x[4],2) + pow(C[2] - x[5],2)) + math.sqrt(pow(D[0] - x[3],2) + pow(D[1] - x[4],2) + pow(D[2] - x[5],2))


def POS():
    counter = 0
    MAX_REPEAT = 1000
    
    x = np.zeros((POPULATION_SIZE, 6))
    v = np.zeros((POPULATION_SIZE, 6))
    for i in range(POPULATION_SIZE):
        for j in range(6):
            x[i][j] = rand.uniform(0,5)
            v[i][j] = rand.uniform(0,Vmax)

    #Init pBest/qBest   
    pbest = np.zeros((POPULATION_SIZE,6)) #Agents best result
    gbest = np.zeros((1,6)) 
    for i in range(POPULATION_SIZE):
        pbest[i] = x[i]
    temp = x[0]
    for i in range(1,POPULATION_SIZE,1):
        if optimizationFunction(temp) > optimizationFunction(x[i]):
            temp = x[i]
    gbest = temp
    
    #Main loop
    while True:
        for i in range(POPULATION_SIZE):
            v[i] = W*v[i] + C1*rand.uniform(0,1)*(pbest[i] - x[i]) + C2*rand.uniform(0,1)*(gbest - x[i])
            np.clip(v[i], 0, Vmax)
            
            temp = x[i] + v[i]
            x[i] = temp
            if(optimizationFunction(temp) < optimizationFunction(pbest[i])):
                pbest[i] = temp
            if(optimizationFunction(temp) < optimizationFunction(gbest)):
                gbest = temp
                counter = 0
            else:
                counter+=1
            
        if(counter >= MAX_REPEAT):
            break
        
    return gbest
            

###MAIN
result = POS()
print("S1 = ", result[0:3])
print("S2 = ", result[3:7])
print("Minimal distance = ", optimizationFunction(result))