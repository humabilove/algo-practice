# BOJ 2444

import sys

def main():
    input = sys.stdin.readline
    
    N = int(input())
    
    for i in range(1,N):
        space = N - i
        star = 2*i - 1
        print(" "*space + "*"*star)
    print("*"*(2*N - 1))
    for i in range(N-1,0, -1):
        space = N - i
        star = 2*i - 1
        print(" "*space + "*"*star)
    

if __name__ == "__main__":
    main()
