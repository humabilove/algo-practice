# BOJ 2439

import sys

def main():
    input = sys.stdin.readline
    
    N = int(input())
    
    for i in range(N):
        print(("*"*(i+1)).rjust(N))

if __name__ == "__main__":
    main()
