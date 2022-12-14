from Grammar import Grammar

grammar = Grammar.fromFile("g1.txt")
grammar.printTerminals()
grammar.printNonTerminals()
grammar.printProductions()
grammar.printProductionsForNonTerminal('S')