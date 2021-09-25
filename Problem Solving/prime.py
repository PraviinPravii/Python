''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main(a,b):
    for num in range(a,b):
        for i in range(2,num):
            if num%i==0: break
        else:
            print(num)

a=int(input())
b=int(input())
main(a,b)

