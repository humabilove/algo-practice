# BOJ 15552

import sys

def main():
    input = sys.stdin.readline
    
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        print(a+b)

if __name__ == "__main__":
    main()
