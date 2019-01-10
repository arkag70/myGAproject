import numpy as np
import pandas as pd

# initialisation
generations=30
points = 30
n = 2
mutation_rate = 0.1

#methods
def get_cols():
    cols = ''
    for i in range(n):
        cols = cols+' x'+str(i+1)
    return cols.split()

def get_sum(x,p,n):
    s=np.zeros(p)
    for i in range(p):
        for j in range(n):
            s[i]+=x[i,j]**2 - 10*np.cos(2*np.pi*x[i,j])
    return s

def initialise(p,n):
    x=10.24*np.random.rand(p,n)-5.12
    y = 10*n + get_sum(x,p,n)
    return (x,y)

def crossover(x):
    for i in range(points):
        for j in range(n):
            while True:
                a = np.random.randint(points)
                b = np.random.randint(points)
                if(a!=b):
                    break
            while True:
                fail = 0
                try:
                    x[i][j] = np.random.randint(np.abs(x[b][j]-x[a][j])*1000)/1000 + np.min([x[a][j],x[b][j]])
                except:
                    fail=1
                finally:
                    if fail == 0:
                        break

    y = 10*n + get_sum(x,points,n)
    return (x,y)

def mutate(x):
    for i in range(points):
        for j in range(n):
            if np.random.randint(10000)/10000 < mutation_rate:
                x[i][j] = 10.24*np.random.rand()-5.12
    y = 10*n + get_sum(x,points,n)
    return (x,y)

def regenerate(pop):
    half = (int) (points/2)
    #sort the data by its y values in ascending order
    pop_temp = pop.sort_values(by='y')

    #eliminate the bottom half with poorer values
    pop_temp = pop_temp[0:half]

    #get new values
    xnew,ynew = initialise(half,n)

    #create x matrix from the existing data frame
    x = np.matrix(pop_temp.drop(columns='y'))
    x = np.concatenate((x,xnew))
    y = 10*n + get_sum(x,points,n)

    return x,y

def show(x,y):
    pop = pd.DataFrame(data = x , columns = get_cols())
    pop['y'] = y
    #print(pop)
    return pop

def genetic_train(x,iterations):
    print(f'{iterations}')
    x,y = crossover(x)
    x,y = mutate(x)
    pop = show(x,y)
    x,y = regenerate(pop)
    if iterations == generations-1:
        print(f'\nPopulation after generation {iterations}:\n')
        print(show(x,y))
    return x
