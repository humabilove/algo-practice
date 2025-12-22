# BOJ 9086

import sys

def main():
    input = sys.stdin.readline
    
    N = int(input())
    
    while N:
        S = input().strip()
        print(S[0]+S[-1])
        N -= 1

if __name__ == "__main__":
    main()
