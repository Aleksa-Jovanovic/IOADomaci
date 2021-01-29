import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as scp
import math
import random


def activation(input):
    return math.tanh(input)

def training(input):
    outTraining = 0.5 * math.sin(math.pi * input)
    return outTraining


def outNeural(input, weight):
    sum = 0
    for i in range(5):
        sum += weight[i+5]*activation(weight[i] * input)
    return activation(sum)

def optimization(weight):
    sum = 0
    i = -1
    while i<=1 :
        sum = sum + (outNeural(i,weight) - training(i))**2
        i = i + 0.1
    return math.sqrt(sum)

def checkCorrectWeight(weight):
    flag = True
    for curr in weight:
        if curr > 10 or curr < -10:
            flag = False
            break;
    return flag

#__Main_Start__
correct = False
weight = np.zeros(10)

while 1:
    for i in range(10):
        weight[i] = (random.uniform(-10.0, 10.0))
        
    weight = scp.minimize(optimization, weight, method='nelder-mead').x
    correct = checkCorrectWeight(weight)
    if optimization(weight) < 10**-2 and correct:
        break
    #else:
        #print('Again')
        
        
        
print("Weights: ")
for curr in weight:
    print(curr)
print("Optimization min: ")
print(optimization(weight))

outTraining = []
outFinal = []
t = np.linspace(-1, 1, 20)

#Training
for i in range(20):
    outTraining.append(training(t[i]))
    outFinal.append(outNeural(t[i], weight))

#Make array from list
outTraining = np.array(outTraining)
outFinal = np.array(outFinal)

plt.plot(t, outTraining, label='outTraining')
plt.plot(t, outFinal, label='outNeural')
plt.legend()
plt.grid()
plt.show()  
    
    