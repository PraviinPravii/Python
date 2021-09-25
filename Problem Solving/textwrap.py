

def wrap(string, max_width):
    st=str()
    cnt=0
    for i in range(len(string)):
        cnt+=1
        st+=string[i]
        if cnt%max_width==0:
            cnt=0
            print(st)
            st=""
        elif cnt%max_width!=0:
            continue
    print(st)
            
            

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)