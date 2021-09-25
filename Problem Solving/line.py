def split_and_join(line):
    st=str()
    for i in line:
        if i==" ":
            st+="-"
        else:
            st+=i
    return st
            
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)