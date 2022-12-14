class Grammar:

    def __init__(self, N, E, P, S):
        self.N = N
        self.E = E
        self.P = P
        self.S = S

    def checkCFG(self):
        for key in self.P.keys():
            if key not in self.N:
                return False
            for move in self.P[key]:
                for char in move:
                    if char not in self.N and char not in self.E and char != 'E':
                        return False
        return True

    @staticmethod
    def parseLine(line):
        return [value.strip() for value in line.strip().split('==')[1].strip()[1:-1].strip().split(';')]

    @staticmethod
    def fromFile(fileName):

        with open(fileName, 'r') as file:
            N = Grammar.parseLine(file.readline())
            E = Grammar.parseLine(file.readline())
            S = file.readline().split('==')[1].strip()
            P = Grammar.parseRules(Grammar.parseLine(''.join([line for line in file])))

            return Grammar(N, E, P, S)

    @staticmethod
    def parseRules(rules):
        result = {}
        index = 1

        for rule in rules:
            lhs, rhs = rule.split('->')
            lhs = lhs.strip()
            rhs = [value.strip() for value in rhs.split('|')]

            for value in rhs:
                if lhs in result.keys():
                    result[lhs].append((value, index))
                else:
                    result[lhs] = [(value, index)]
                index += 1

        return result

    def splitRhs(self, prod):
        return prod.split(' ')

    def isNonTerminal(self, value):
        return value in self.N

    def isTerminal(self, value):
        return value in self.E

    def printProductionsForNonTerminal(self, nonTerminal):
        if not self.isNonTerminal(nonTerminal):
            raise Exception('Can only show productions for non-terminals')
        for key in self.P.keys():
            if key == nonTerminal:
                print(key + " -> ", end='')
                for element in self.P[key][:-1]:
                    print(element[0] + " | ", end='')
                print(self.P[key][-1][0])

    def getProductionsForNonTerminal(self, nonTerminal):
        nonTerminals = []
        if not self.isNonTerminal(nonTerminal):
            raise Exception('Can only show productions for non-terminals')
        for key in self.P.keys():
            if key == nonTerminal:
                nonTerminals.append(self.P[key])

        return nonTerminals

    def printNonTerminals(self):
        print('N == { ' + ', '.join(self.N) + ' }')

    def printTerminals(self):
        print('E == { ' + ', '.join(self.E) + ' }')

    def printProductions(self):
        print('P = { ')
        for production in self.P:
            print(production + " -> ", end='')
            for element in self.P[production][:-1]:
                print(element[0] + " | ", end='')
            print(self.P[production][-1][0] + ';')
        print('}')

    def __str__(self):
        return 'N = { ' + ', '.join(self.N) + ' }\n' \
               + 'E = { ' + ', '.join(self.E) + ' }\n' \
               + 'P = { ' + ', '.join([' -> '.join(prod) for prod in self.P]) + ' }\n' \
               + 'S = ' + str(self.S) + '\n'
