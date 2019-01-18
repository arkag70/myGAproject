from GAmethods import *

if __name__ == "__main__":
    x = initialise()
    y = f(x)
    z = g(y)
    best = []
    best.append(np.max(y))
    i=1
    while(i):
        x = crossover(x,z)
        x = mutation(x)
        y = f(x)
        z = g(y)
        best.append(np.max(y))
        print(str(i)+"\t"+x[operator.indexOf(y,max(y))]+" : "+str(max(y)))
        i+=1
        if x[operator.indexOf(y,max(y))] == standard:
            break


    plt.plot(best)
    plt.xlabel('Number of generations --->')
    plt.ylabel('Best fitness Score in population --->')
    plt.title('Best Fitness vs Generations')
    plt.show()
