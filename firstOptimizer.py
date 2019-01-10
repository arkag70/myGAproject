from GAmethods import *

if __name__ == "__main__":
    x,y = initialise(points,n)
    print('\ninitial pop\n')
    print(show(x,y))

    for i in range(generations):
        genetic_train(x,i)
