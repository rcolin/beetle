
class Paw(object):
     
    def __init__(self, stat=0, x=0, y=0):
        self.stat = stat;
        self.x = x;
        self.y = y;

    def __str__(self):
        return 'stat : ' + str(self.stat) + ' | x : ' + str(self.x) + ' | y : ' + str(self.y)    

class Beetle(object):
    
    def __init__(self, name="No Name"):
        self.name = name
        self.paws = []
        self.paws.append(Paw(0, 0, 0))
        self.paws.append(Paw(0, 0, 1))
        self.paws.append(Paw(0, 1, 0))
        self.paws.append(Paw(0, 1, 1))
        self.paws.append(Paw(0, 2, 0))
        self.paws.append(Paw(0, 2, 1))

    def __str__(self):
        bufferstr = 'Beetle name : ' + self.name + '\n'
        for i in range(0, 6):
            bufferstr += str(self.paws[i])
            bufferstr += '\n'
        return bufferstr
