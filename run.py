#!/usr/bin/python

import os
import sys, getopt
from beetle import Beetle
from beetle import Paw

def inputdata(argv):
    poolsize = '0';
    iterations = '0';
    
    try:
      opts, args = getopt.getopt(argv,"hp:i:",["--poolsize","--iterations"])
    except getopt.GetoptError as err:
      print 'run.py -p <poolsize> -i <iterations>'
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'run.py -p <poolsize> -i <iterations>'
            sys.exit()
        elif opt in ("-p", "--poolsize"):
            poolsize = arg
        elif opt in ("-i", "--iterations"):
            iterations = arg
        else:
            assert False, "unhandled option"
    return (poolsize, iterations)

def intro():
    os.system('clear');
    print('\n************** Genetic algorithm of beetle moving **************\n');

if __name__ == '__main__':
    #display start infos
    intro();
    
    #input data
    poolsize, iterations = inputdata(sys.argv[1:]);
    
    #display input data
    print ' #Pool : ' + poolsize + ' | #Iterations : ' + iterations;
   
    #creat beetle pool
    for i in range(0, int(poolsize)):
        b = Beetle("b" + str(i));
        print(b.name);
        b.paws[5].infos()