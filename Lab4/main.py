from FiniteAutomata import FiniteAutomata
from Scanner import Scanner
from SymbolTable import SymbolTable


def print_options(condition):
    print("---------------")
    print("1. Print the set of states")
    print("2. Print the alphabet")
    print("3. Print the transitions")
    print("4. Print the initial state")
    print("5. Print the set of final states")
    if condition:
        print("6. Check if string in DFA")
    print("0. Exit")
    print("---------------")

def print_choice():
    print("---------------")
    print("1. Run FA")
    print("2. Run scanner with FA")
    print("---------------")


if __name__ == "__main__":
    print_choice()
    choice = input("Please input your choice: ")
    while not choice.isnumeric():
        print("Not a valid option")
        choice = input("Please input your choice: ")

    choice = int(choice)
    if choice == 1:
        fa = FiniteAutomata('FA.in')
        fa.read_fa()
        dfa = False
        ok = True

        if fa.check_dfa():
            dfa = True

        while ok:
            print_options(dfa)
            option = input("Please input your option: ")
            if option.isnumeric():
                option = int(option)
                if option == 0:
                    ok = False
                elif option == 1:
                    fa.print_set_of_states()
                elif option == 2:
                    fa.print_alphabet()
                elif option == 3:
                    fa.print_transitions()
                elif option == 4:
                    fa.print_initial_state()
                elif option == 5:
                    fa.print_set_of_final_states()
                elif option == 6 and dfa is True:
                    sequence = input("Enter the sequence: ")
                    answer = fa.check_sequence(sequence)
                    if answer:
                        print("The sequence is accepted by the DFA")
                    else:
                        print("The sequence is not accepted by the DFA")
                else:
                    print("Not a valid option")
            else:
                print("Not a valid option")

    if choice == 2:
        symbol_table = SymbolTable(16)
        scanner = Scanner(symbol_table, 'p2.py', 'IdentifierFA.in', 'StringConstantFA.in', 'IntegerConstantFA.in')
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

