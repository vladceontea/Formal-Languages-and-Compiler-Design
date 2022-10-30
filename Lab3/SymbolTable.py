
class SymbolTable:

    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [[] for i in range(self.capacity)]

    def hash(self, symbol):
        total = 0
        for char in str(symbol):
            total = total + ord(char)

        pos = total % self.capacity
        return pos

    def add(self, symbol):
        added = 0
        for table in self.table:
            if symbol in table:
                added = 1
                #print("Symbol " + str(symbol) + " already in symbol table")
        if added == 0:
            pos = self.hash(symbol)
            self.table[pos].append(symbol)
            #print("Added symbol " + str(symbol) + " at position " + str(pos))

    def search(self, symbol):
        pos = self.hash(symbol)
        pos2 = -1
        if len(self.table[pos]) == 0:
            #print("Symbol " + str(symbol) + " does not exist")
            return -1, -1
        else:
            for i in range(len(self.table[pos])):
                if self.table[pos][i] == symbol:
                    pos2 = i
        return pos, pos2

    def to_string(self):
        print("Symbol Table")
        for i in range(self.capacity):
            if len(self.table[i]) != 0:
                print(str(i) + " " + str(self.table[i]))
