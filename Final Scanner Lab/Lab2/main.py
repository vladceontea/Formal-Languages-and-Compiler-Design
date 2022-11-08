from SymbolTable import SymbolTable

symbolTable = SymbolTable(20)

symbolTable.add("d")
symbolTable.add("a")
symbolTable.add("c")
symbolTable.add("a2")
symbolTable.add("abc")
symbolTable.add(3)
symbolTable.add("a")
symbolTable.add("\"hello\"")

symbolTable.to_string()
assert symbolTable.search("a") == (17, 0)
assert symbolTable.search("d") == (0, 0)
assert symbolTable.search("\"hello\"") == (0, 1)
assert symbolTable.search(3) == (11, 0)
assert symbolTable.search(5) == (-1, -1)

