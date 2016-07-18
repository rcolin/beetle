import os
from beetle import Beetle

class Utils(object):
    @staticmethod
    def intro():
        os.system('clear');
        print('\n************** Genetic algorithm of beetle moving **************\n');

    @staticmethod
    def printBeetle(beetle):
        print('Name : ' +beetle.name)
        print('            ')
        print('  +     +   ')
        print('   \___/    ')
        print('    | |   / ')
        print(' /-------/  ')
        print('/ |     |   ')
        print('__|     |___')
        print('  |     |   ')
        print('  |     |   ')
        print(' /-------\  ')
        print('/         \ ')
        print('            ')