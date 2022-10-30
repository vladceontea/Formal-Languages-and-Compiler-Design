
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

    def read_separators(self):
        file = open('Token.txt', 'r')
        lines = file.readlines()
        for i in range(0, 8):
            self.separator_list.append(lines[i][:-1])

    def scan(self):
        file = open(self.file, 'r')
        self.read_tokens()
        self.read_separators()
        lines = [line for line in file.readlines() if line.strip()]
        for line in lines:
            index = 0
            words = line.split(' ')
            for word in words:
                if len(word) > 1:
                    word_separators = []
                    for separator in self.separator_list:
                        if separator in word:
                            word_separators.append(separator)
                    if word_separators:
                        tokens = self.split_token(word, word_separators)
                        word = tokens[0]
                        words[index+1:index+1] = tokens[1:]
                        index = index + 1

                print(word)
                if word in self.token_list:
                    self.pif_table.append(word)
                elif self.is_identifier(word) or self.is_constant(word):
                    self.symbol_table.add(word)
                    self.pif_table.append(self.symbol_table.search(word))
                else:
                    print("Lexical error")


    def split_token(self, word, separators):
        tokens = []
        prev_end = 0
        for i in range(len(word)):
            if word[i] in separators:
                if abs(prev_end - i) != 0:
                    tokens.append(word[prev_end:i])
                tokens.append(word[i])
                prev_end = i + 1
        #print(tokens)
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



