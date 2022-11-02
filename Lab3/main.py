
from SymbolTable import SymbolTable
from Scanner import Scanner

symbol_table = SymbolTable(16)
scanner = Scanner(symbol_table, 'p1err.py')
scanner.scan()


pif = open("PIF.out", "a")
pif.truncate(0)
pif.write("PIF Table\n")
for i in range(len(scanner.pif_table)):
    pif.write(str(scanner.pif_table[i][0]) + " " + str(scanner.pif_table[i][1]))
    pif.write("\n")
pif.close()

st = open("ST.out", "a")
st.truncate(0)
st.write(str(scanner.symbol_table.to_string()))
st.close()





