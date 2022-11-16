
class FiniteAutomata:

    def __init__(self, file_name):
        self.set_of_states = set()
        self.alphabet = set()
        self.transitions = []
        self.initial_state = ""
        self.set_of_final_states = set()
        self.file = file_name

    def read_fa(self):
        lines = open(self.file, 'r').read().splitlines()
        self.set_of_states = lines[0].split(' ')
        self.alphabet = lines[1].split(' ')
        self.initial_state = lines[2]
        self.set_of_final_states = lines[3].split(' ')
        lines = lines[4:]
        for line in lines:
            elements = line.split(' ')
            if elements[0] in self.set_of_states and elements[2] in self.set_of_states and elements[1] in self.alphabet:
                transition = (elements[0], elements[1])
                self.transitions.append((transition, elements[2]))

    def print_set_of_states(self):
        print("Set of states:")
        print(*self.set_of_states)

    def print_alphabet(self):
        print("Alphabet:")
        print(*self.alphabet)

    def print_initial_state(self):
        print("Initial states:")
        print(self.initial_state)

    def print_set_of_final_states(self):
        print("Set of final states:")
        print(*self.set_of_final_states)

    def print_transitions(self):
        print("Transitions:")
        for transition in self.transitions:
            print("(" + str(transition[0][0]) + ", " + str(transition[0][1]) + ") " + "-> " + str(transition[1]))

    def check_dfa(self):
        transitions = [i[0] for i in self.transitions]
        return len(transitions) == len(set(transitions))

    def check_sequence(self, sequence):

        state = self.initial_state
        for i in range(len(sequence)):
            transition = (state, sequence[i])
            if transition in [i[0] for i in self.transitions]:
                next_state = [i for i in self.transitions if i[0] == transition]
                state = next_state[0][1]
            else:
                return False

        if state in self.set_of_final_states:
            return True
        else:
            return False
