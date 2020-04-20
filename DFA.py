class DFA:
    #DFA is a 5-tuples
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
    K = [0,1,2]
    A = ['a','b']
    TF = {}
    TF[(0,'a')] = 2
    TF[(0,'b')] = 0
    TF[(1,'a')] = 1
    TF[(1,'b')] = 2
    TF[(2,'a')] = 1
    TF[(2,'b')] = 0
    S = 1
    F = [0,2]

    M = DFA(K,A,TF,S,F)
    try:
        print("Enter a String : ",end='')
        inp_str = input()
        for i in inp_str:
            if i not in A:
                raise NameError
                break
    except NameError:
        print("The String entered is not valid!")
    else:
        M.check_str_validity(inp_str)
