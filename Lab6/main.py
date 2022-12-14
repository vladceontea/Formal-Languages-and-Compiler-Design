from Grammar import Grammar
from Parser import Parser

if __name__ == '__main__':
    grammar = Grammar.fromFile('g1.txt')
    parser = Parser(grammar)

    work_stack = parser.run('aacbc')
