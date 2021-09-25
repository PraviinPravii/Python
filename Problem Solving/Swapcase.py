def swap_case(s):
    st=str()
    for i in s:
        if i.islower():
            i=i.upper()
            st+=i
        else:
            i=i.lower()
            st+=i
    return st

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)