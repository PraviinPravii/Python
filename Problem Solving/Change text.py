

def mutate_string(string, position, character):
    st=str()
    for i in range(len(string)):
        if i==position:
            st+=character
        else:
            st+=string[i]
    return st
            
    

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)