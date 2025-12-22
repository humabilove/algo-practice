# BOJ 2765

import sys

def main():
    input = sys.stdin.readline
    
    T = int(input())
    
    while T:
        R, S = map(str, input().split())
        R = int(R)
        S = S.strip()
        for i in range(len(S)):
            print(S[i]*R, end="")
        print()
        T -= 1

if __name__ == "__main__":
    main()
