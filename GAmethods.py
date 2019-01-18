import numpy as np
import string
import operator
import matplotlib.pyplot as plt

standard='The quick brown fox jumps over the lazy dog'
N=len(standard)
pop=50
mu = 0.02
letters = ' '+string.ascii_letters+string.punctuation

def get_word():

    word=''
    for i in range(N):
        word += letters[np.random.randint(len(letters))]
    return word

def calculate_fitness(word):
    count=0
    for j in range(N):
            if word[j] == standard[j]:
                count+=1
    return count

def f(x):
    y=[]
    for i in range(len(x)):
        y.append(calculate_fitness(x[i]))
    return y

#relative fitness
def g(y):
    z=[]
    total_fitness = sum(y)
    for i in y:
        try:
            z.append(i/total_fitness)
        except:
            z.append(0)
    return z

def initialise():
    x=[]
    for i in range(pop):
        x.append(get_word())
    return x

def crossover(x,z):
    for i in range(len(x)):
        child=[]
        a = np.random.randint(pop)
        b = np.random.randint(pop)

        cut_point = (int)(N/2)

        A = x[a][:cut_point]
        B = x[a][cut_point:]
        C = x[b][:cut_point]
        D = x[b][cut_point:]

        child.append(A+D)
        child.append(C+B)
        child.append(D+A)
        child.append(B+C)

        cy = f(child)
        x[i] = child[operator.indexOf(cy,max(cy))]
    return x

def calculate_mut(p):
    p_lst=[]
    for i in p:
        p_lst.append(i)
    for i in range(len(p_lst)):
        if np.random.rand()<mu:
            p_lst[i] = letters[np.random.randint(len(letters))]
    return ''.join(p_lst)

def mutation(x):
    for i in range(len(x)):
        x[i] = calculate_mut(x[i])
    return x
