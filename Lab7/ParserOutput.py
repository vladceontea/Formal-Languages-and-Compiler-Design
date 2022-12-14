
from Parser import Parser

class TableElement:
    def __init__(self, element, pos):
        self.element = element #production elem ('S 1', 0)
        self.parent = -1
        self.left = -1
        self.right = -1
        self.pos = pos

    def __str__(self) -> str:
        return "ID: " + str(self.pos) + " -> Element: " + str(self.element) + ", parent " + str(self.parent) + " ,left: " + str(self.left) + " ,right: " + str(self.right)


class ParserOutput:
    def __init__(self, parser: Parser, fileName):
        self.parser = parser
        self.table = {}
        self.fileName = fileName

    def start(self, work_stack):
        self.table[0] = TableElement(work_stack[0], 0)
        index = 1
        current = self.table[0]
        self.parse(current, work_stack, index)
        file = open(self.fileName, 'w')
        for val in self.table.values():
            print(val, file=file)
            print(val)

    def parse(self, node, work_stack, index):
        non_terminal = node.element.split(' ')[0]
        production_nr = int(node.element.split(' ')[1])
        production = self.parser.grammar.getProductionsForNonTerminal(non_terminal)[0][production_nr-1][0]
        production = production.split()
        left = -1
        for el in production:
            if el in self.parser.grammar.E:
                current = TableElement(el, index)
                term = True
            else:
                current = TableElement(work_stack[index], index)
                term = False
            self.table[index] = current

            current.parent = node.pos
            current.left = left
            left = current.pos
            if self.table[index].left != -1:
                self.table[self.table[index].left].right = index
            index += 1

            if not term:
                index = self.parse(current, work_stack, index)

        return index
