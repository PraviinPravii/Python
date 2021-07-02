
def staircase(n):
    hashs=""
    for i in range(n):
        hashs=" "*((n-1)-i)
        hashs+="#"*(i+1)
        print(hashs)
        
    # Write your code here
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
