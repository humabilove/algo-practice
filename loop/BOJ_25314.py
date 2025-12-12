# BOJ 25314

import sys

def main():
    input = sys.stdin.readline
    
    N = int(input())
    N //= 4
    for _ in range(N):
        print("long", end=" ")
    print("int")

if __name__ == "__main__":
    main()
