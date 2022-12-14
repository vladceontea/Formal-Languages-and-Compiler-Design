from Grammar import Grammar
from Parser import Parser
from Output import Output


def readPif(Filename):
    sequence = []
    file = open(Filename, 'r')
    lines = file.readlines()

    for line in lines[1:]:
        key = line.split(' ')[0]
        sequence.append(key)
    return sequence


def test_parser():
    grammar = Grammar.fromFile('g1.txt')
    parser = Parser(grammar)

    assert parser.configuration.input_stack == ['S']

    parser.expand()
    assert parser.configuration.work_stack == ['S 1']
    assert parser.configuration.input_stack == ['a', 'S', 'b', 'S']

    parser.advance()
    assert parser.configuration.work_stack == ['S 1', 'a']
    assert parser.configuration.input_stack == ['S', 'b', 'S']

    index = parser.configuration.index

    parser.back()
    assert parser.configuration.index == index - 1
    assert parser.configuration.work_stack == ['S 1']
    assert parser.configuration.input_stack == ['a', 'S', 'b', 'S']

    parser.advance()
    parser.expand()
    parser.advance()
    parser.expand()
    parser.momentary_insuccess()
    assert parser.configuration.work_stack == ['S 1', 'a', 'S 1', 'a', 'S 1']
    assert parser.configuration.input_stack == ['a', 'S', 'b', 'S', 'b', 'S', 'b', 'S']

    parser.another_try()
    assert parser.configuration.work_stack == ['S 1', 'a', 'S 1', 'a', 'S 2']
    assert parser.configuration.input_stack == ['a', 'S', 'b', 'S', 'b', 'S']

    grammar = Grammar.fromFile('g1.txt')
    parser = Parser(grammar)

    parser.run('aacbc')
    assert parser.configuration.state["f"] is True

    grammar = Grammar.fromFile('g1.txt')
    parser = Parser(grammar)

    parser.run('ggg')
    assert parser.configuration.state["e"] is True


if __name__ == '__main__':

    test_parser()

    grammar = Grammar.fromFile('g1.txt')
    parser = Parser(grammar)

    seq = readPif('seq.txt')

    work_stack = parser.run(seq)
    if work_stack is not None:
        print("Table/Tree representation")
        output = Output(parser, 'out1.txt')
        output.start(work_stack)
