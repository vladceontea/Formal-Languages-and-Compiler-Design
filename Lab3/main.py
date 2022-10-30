
from SymbolTable import SymbolTable
from Scanner import Scanner

symbol_table = SymbolTable(16)
scanner = Scanner(symbol_table, 'p1.py')
scanner.scan()

print(scanner.symbol_table.to_string())
print(scanner.pif_table)





