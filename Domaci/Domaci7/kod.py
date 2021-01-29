import matplotlib.pyplot as plt
import numpy as np

files = np.array([173669, 275487, 1197613, 1549805, 502334, 217684, 1796841, 274708,
        631252, 148665, 150254, 4784408, 344759, 440109, 4198037, 329673, 28602,
        144173, 1461469, 187895, 369313, 959307, 1482335, 2772513, 1313997, 254845,
        486167, 2667146, 264004, 297223, 94694, 1757457, 576203, 8577828, 498382,
        8478177, 123575, 4062389, 3001419, 196884, 617991, 421056, 3017627, 131936,
        1152730, 2676649, 656678, 4519834, 201919, 56080, 2142553, 326263, 8172117,
        2304253, 4761871, 205387, 6148422, 414559, 2893305, 2158562, 465972, 304078,
        1841018, 1915571])

HAMMING_MIN = 0
HAMMING_MIN = 64
MAX_ITERATIONS = 100000
INIT_TEMP = 32 * 1024 * 1024
ALFA = 0.9998

def hammingDistance(h_min, h_max, curr_iterations, max_iterations):
    return (h_min - h_max) / (max_iterations - 1) * (curr_iterations - 1) + h_max

def optimiztionFunction(x):
    F = 2 ** 26 - sum((x * files))
    if F >= 0:
        return F
    else:
        return 2 ** 26
    
def simulation(init_state):    
    current_state = init_state
    current_temp = INIT_TEMP
    current_iterations = 0
    results = []
    
    current_best = INIT_TEMP
    
    while True:
        if current_iterations > MAX_ITERATIONS or current_temp <= 0:
            break
        
        hamming_distance_result = hammingDistance(HAMMING_MIN, np.random.randint(0, 16), current_iterations, MAX_ITERATIONS)
        random_position = np.random.randint(0, 63, int(hamming_distance_result))
        for i in random_position:
            if (current_state[i] == 0):
                current_state[i] = 1
            else:
                current_state[i] = 0
                
        if optimiztionFunction(current_state) < current_best:
            current_best = optimiztionFunction(current_state)
        results.append(current_best)
        current_temp = current_temp * ALFA
        current_iterations += 1
        
        if (optimiztionFunction(current_state) <= 32):
            print("Good result -> ")
            print(optimiztionFunction(current_state))
            print("State -> : ", current_state)
            
 
    print("NAKON GOTOVE PETLJE IMAMO temp = ", current_temp)
    print("BROJ ITERACIJA = ", current_iterations)
    return results
    

###Main
t = np.arange(0, 100001, 1)
r = []


for i in range(20):
    x = np.random.randint(0, 2, 64)
    r.append(simulation(x))
    plt.plot(t, r[i])
 
plt.title("Minimums")
plt.xlabel("Iterations")
plt.ylabel("Values")
plt.xscale("log")
plt.yscale("log")
plt.show()

mean = []
for j in range(100001):
    temp = 0
    for i in range(20):
        temp += r[i][j]
    mean.append(temp / 20)


plt.figure()
plt.xscale("log")
plt.yscale("log")
plt.title("Avarage")
plt.xlabel("Iterations")
plt.ylabel("Values")
plt.plot(t, mean)
plt.show()