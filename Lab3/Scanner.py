import re

class Scanner:

    def __init__(self, symbol_table, file):
        self.symbol_table = symbol_table
        self.file = file
        self.token_list = []
        self.separator_list = []
        self.pif_table = []

    def read_tokens(self):
        file = open('Token.txt', 'r')
        lines = file.readlines()
        for i in range(0, 40):
            self.token_list.append(lines[i][:-1])
        file.close()

    def read_word_separators(self):
        file = open('Token.txt', 'r')
        lines = file.readlines()
        for i in range(0, 22):
            self.separator_list.append(lines[i][:-1])
        file.close()

    def scan(self):
        file = open(self.file, 'r')
        self.read_tokens()
        self.read_word_separators()
        separator_string = "("
        for separator in self.separator_list:
            if separator == "[":
                separator_string += "[\\" + separator + "]"
            else:
                separator_string += "[" + separator + "]"
            if len(separator) > 1:
                separator_string += "+"
            separator_string += "|"
        separator_string = separator_string[:-1] + ")"
        lines = file.readlines()
        for number, line in enumerate(lines):
            index = 0
            words = line.split(' ')
            words = list(filter(('').__ne__, words))
            for word in words:
                index = index + 1
                tokens = [s for s in
                         re.split(separator_string, word) if s]
                word = tokens[0]
                if len(tokens) > 1:
                    words[index:index] = tokens[1:]

                if word in self.token_list:
                    self.pif_table.append((word, -1))
                elif self.is_identifier(word):
                    self.symbol_table.add(word)
                    self.pif_table.append(("identifier", self.symbol_table.search(word)))
                elif self.is_constant(word):
                    self.symbol_table.add(word)
                    self.pif_table.append(("constant", self.symbol_table.search(word)))
                elif word == '\n':
                    break
                else:
                    print("Lexical error at line " + str(number) + ": " + str(word))
                    print(line)

    def is_identifier(self, word):
        allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
        if not word[0].isalpha():
            return False
        if not all(ch in allowed for ch in word):
            return False
        return True

    def is_constant(self, word):
        allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
        if word[1:].isnumeric() and word[0]=='-':
            return True
        if word.isnumeric():
            return True
        if word[0] == "\"" and word[-1] == "\"" and all(ch in allowed for ch in word[1:-1]):
            return True

        return False



