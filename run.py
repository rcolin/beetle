import os


def testfct():
    print('number of pool : ');
    nPool = input();
    print('number of iterations : ');
    nIterations = input();
    return (nPool, nIterations);

if __name__ == '__main__':
   os.system('clear');
   print(' ************** Genetic algorithm of beetle moving **************');
   nPool, nIterations = testfct();
   print ' #Pool : ' + str(nPool) + ' | #Iterations : ' + str(nIterations);