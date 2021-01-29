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

MAX_ITERATIONS = 100000
POPULATION_SIZE = 2000
NUMBER_OF_SELECTED = 400
MUTATION_POSABILITY = 0.1
CROSSOVER_POSABILITY = 0.8

def optimiztionFunction(x):
    F = 2 ** 26 - sum((x * files))
    if F >= 0:
        return F
    else:
        return 2 ** 26
    
def selection(population):
    population.sort(key = lambda x: optimiztionFunction(x))
    selected = []
    for i in range(NUMBER_OF_SELECTED):
        selected.append(population[i])
    population.clear()
    return selected
    
def crossover(selected_ones):
    first = []
    second = []
    kids = []
    for i in range(0,NUMBER_OF_SELECTED,2):
        for z in range(5):
            position = np.random.randint(0,64)
            #Switching
            for j in range(position):
                first.append(selected_ones[i][j])
                second.append(selected_ones[i+1][j])
            for j in range(position,64):
                first.append(selected_ones[i+1][j])
                second.append(selected_ones[i][j])
            kids.append(first)
            kids.append(second)
            first = []
            second = []
    
    return kids

def mutation(population):
    for i in range(POPULATION_SIZE):
        mutation_chance = np.random.randint(0,10) / 10
        if(mutation_chance <= MUTATION_POSABILITY):
            position = np.random.randint(0,64)
            population[i][position] = 1 if population[i][position] == 0 else 0
    return population
    
def simulation(init_population):
    new_population = init_population
    result = []
    current_best = optimiztionFunction(new_population[0])
    current_best_array = new_population[0]
    """
    for i in range(POPULATION_SIZE):
        if optimiztionFunction(new_population[i]) < current_best:
            current_best = optimiztionFunction(new_population[i])
        result.append(current_best)
    """
    for i in range(50):
        new_population = selection(new_population)
        new_population = crossover(new_population)
        new_population = mutation(new_population)
        for i in range(POPULATION_SIZE):
            if optimiztionFunction(new_population[i]) < current_best:
                current_best = optimiztionFunction(new_population[i])
                current_best_array = new_population[i]
            result.append(current_best)
            
        if (current_best <= 32):
            print("Good result -> ")
            print(current_best)
            print("State -> : ", current_best_array)
            
    return result
    
###Main
t = np.arange(0, 100000, 1)
r = []
population = []


for i in range(20):
    
    for j in range(POPULATION_SIZE):
        x = np.random.randint(0, 2, 64)
        population.append(x)
          
    r.append(simulation(population))
    plt.plot(t, r[i])
    population.clear()
    
plt.title("Minimums")
plt.xlabel("Iterations")
plt.ylabel("Values")
plt.xscale("log")
plt.yscale("log")
plt.show() 


mean = []
for j in range(100000):
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