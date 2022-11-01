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
        for i in range(0, 41):
            self.token_list.append(lines[i][:-1])
        file.close()

    def read_separators(self):
        file = open('Token.txt', 'r')
        lines = file.readlines()
        for i in range(0, 22):
            self.separator_list.append(lines[i][:-1])
        file.close()

    def scan(self):
        file = open(self.file, 'r')
        self.read_tokens()
        self.read_separators()
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
        #print(separator_string)
        lines = [line for line in file.readlines() if line.strip()]
        for line in lines:
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
                '''   
                index = index + 1
                if len(word) > 1:
                    word_separators = []
                    for separator in self.separator_list:
                        if separator in word:
                            word_separators.append(separator)
                    if word_separators:
                        print(word)
                        tokens = self.split_token(word, word_separators)
                        word = tokens[0]
                        words[index:index] = tokens[1:]
                        
                '''
                if word in self.token_list:
                    self.pif_table.append(word)
                elif self.is_identifier(word) or self.is_constant(word):
                    self.symbol_table.add(word)
                    self.pif_table.append(self.symbol_table.search(word))
                elif word == '\n':
                    break
                else:
                    print(list[word])
                    print("Lexical error at line " + str(line))

    def split_token(self, word, separators):
        tokens = []
        prev_end = 0
        i = 0
        while i < len(word):
            if word[i] in separators:
                print(str(i) + word[i])
                if abs(prev_end - i) != 0:
                    tokens.append(word[prev_end:i])
                tokens.append(word[i])
                prev_end = i + 1
            i = i + 1
        if word[i-1] != "\n" and word[i-1] not in separators:
            if abs(prev_end - i) != 0:
                tokens.append(word[prev_end:i])
            else:
                tokens.append(word[i-1])

        return tokens

    def is_identifier(self, word):
        allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
        if not word[0].isalpha():
            return False
        if not all(ch in allowed for ch in word):
            return False
        return True

    def is_constant(self, word):
        if word[1:].isnumeric() and word[0]=='-':
            return True
        if word.isnumeric():
            return True
        if word[0] == "\"" and word[-1] == "\"":
            return True

        return False



