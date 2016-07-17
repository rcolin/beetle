#!/usr/bin/python

import os
from beetle import Beetle

def inputdata():
    print('number of pool : ');
    nPool = input();
    print('number of iterations : ');
    nIterations = input();
    return (nPool, nIterations);

if __name__ == '__main__':
    os.system('clear');
    print('\n************** Genetic algorithm of beetle moving **************\n');
    
    nPool, nIterations = inputdata();
    
    print ' #Pool : ' + str(nPool) + ' | #Iterations : ' + str(nIterations);
   
    for x in range(0, nPool):
        b = Beetle("b" + str(x));
        print(b.name);
        