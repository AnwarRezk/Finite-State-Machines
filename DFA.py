class DFA:
    #DFA is a 5-tuple
    def __init__(self,finite_states,alphabet,transition_function,initial_state,final_states):
        self.finite_states = finite_states 
        self.alphabet = alphabet
        self.transition_function = transition_function #Dictionary
        self.initial_state = initial_state
        self.final_states = final_states 
    
    def check_str_validity(self,inp_str):
        curr_state = self.initial_state
        for sym in inp_str:
            if (curr_state,sym) in self.transition_function.keys():
                curr_state = self.transition_function[(curr_state,sym)]
            else:
                curr_state = None
        if curr_state in self.final_states:
            print("String is Accepted!")
        else:
            print("String is Rejected!")

if __name__ == "__main__":
    
    #Initialize DFA parameters
    K = ['S0','S1','S2']
    A = ['a','b']
    TF = {}
    TF[('S0','a')] = 'S2'
    TF[('S0','b')] = 'S0'
    TF[('S1','a')] = 'S1'
    TF[('S1','b')] = 'S2'
    TF[('S2','a')] = 'S1'
    TF[('S2','b')] = 'S0'
    S = 'S1'
    F = ['S0','S2']

    M = DFA(K,A,TF,S,F)
    try:
        print("Enter a String : ",end='')
        tape = input()
        for i in tape:
            if i not in A:
                raise NameError
                break
    except NameError:
        print("The String entered is not valid!")
    else:
        M.check_str_validity(tape)
