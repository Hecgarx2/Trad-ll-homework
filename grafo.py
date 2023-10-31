class Nodo:
    def __init__(self, op, arg1, arg2):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
    
    def getOp(self):
        return self.op
    
    def getArg1(self):
        return self.arg1
    
    def getArg2(self):
        return self.arg2
    