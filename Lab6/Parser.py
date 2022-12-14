import time

from ConfigurationClass import ConfigurationClass


class Parser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.configuration = ConfigurationClass(self.grammar.S)

    def expand(self):
        #print("expand")
        nonTerminal = self.configuration.input_stack.pop(0)
        self.configuration.work_stack.append(nonTerminal + " 1")
        string = self.grammar.getProductionsForNonTerminal(nonTerminal)[0][0][0].split(' ')
        string.reverse()
        for i in string:
            self.configuration.input_stack.insert(0, i)

    def advance(self):
        #print("advance")
        self.configuration.index += 1
        terminal = self.configuration.input_stack.pop(0)
        self.configuration.work_stack.append(terminal)

    def momentary_insuccess(self):
        #print("mi")
        self.configuration.state["q"] = False
        self.configuration.state["b"] = True

    def back(self):
        #print("back")
        self.configuration.index -= 1
        terminal = self.configuration.work_stack.pop()
        self.configuration.input_stack.insert(0, terminal)

    def success(self):
        #print("success")
        self.configuration.state["q"] = False
        self.configuration.state["f"] = True

    def another_try(self):
        #print("at")
        nonTerminal = self.configuration.work_stack.pop()
        number = nonTerminal.split(' ')[1]
        production = self.grammar.getProductionsForNonTerminal(nonTerminal.split(' ')[0])[0][int(number)-1][0].split(' ')
        totalProductions = len(self.grammar.getProductionsForNonTerminal(nonTerminal.split(' ')[0])[0])

        for i in range(len(production)):
            self.configuration.input_stack.pop(0)

        if self.configuration.index == int(number) and len(self.configuration.work_stack) == 0 and totalProductions <= int(number):
            self.configuration.state["e"] = True
            self.configuration.state["b"] = False

        elif totalProductions > int(number):
            self.configuration.state["q"] = True
            self.configuration.state["b"] = False
            self.configuration.work_stack.append(nonTerminal.split(' ')[0] + " " + str(int(number) + 1))
            string = self.grammar.getProductionsForNonTerminal(nonTerminal.split(' ')[0])[0][int(number)][0].split(' ')
            string.reverse()
            for i in string:
                self.configuration.input_stack.insert(0, i)

        elif len(self.configuration.work_stack) == 0 and len(self.configuration.input_stack) == 0:
            self.configuration.state["e"] = True
            self.configuration.state["b"] = False
        elif totalProductions <= int(number):
            self.configuration.input_stack.insert(0, nonTerminal.split(' ')[0])

    def run(self, sequence):
        running = True
        while running:
            #print(self.configuration.input_stack)
            #print(self.configuration.work_stack)
            #print(len(self.configuration.work_stack))
            #print("---------------")
            if len(self.configuration.input_stack) == 0 and self.configuration.state["q"] is True and self.configuration.index - 1 == len(sequence):
                self.success()
            elif self.grammar.isNonTerminal(self.configuration.input_stack[0]) and self.configuration.state["q"] is True:
                self.expand()
            elif self.configuration.state["q"] is True and self.grammar.isTerminal(self.configuration.input_stack[0]):
                if self.configuration.index > len(sequence):
                    self.momentary_insuccess()
                else:
                    if sequence[self.configuration.index - 1] == self.configuration.input_stack[0]:
                        self.advance()
                    else:
                        self.momentary_insuccess()
            elif self.configuration.state["b"]:
                if len(self.configuration.work_stack) == 0:
                    self.back()
                elif self.grammar.isTerminal(self.configuration.work_stack[-1]):
                    self.back()
                else:
                    self.another_try()

            if self.configuration.state["f"]:
                running = False
                print("Success " + str(self.configuration.input_stack) + " " + str(self.configuration.work_stack))
                return self.configuration.work_stack
            if self.configuration.state["e"]:
                running = False
                print("Error. Sequence not accepted")
