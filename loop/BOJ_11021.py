# BOJ 11021

import sys

def main():
    input = sys.stdin.readline
    
    N = int(input())
    
    for i in range(N):
        a, b = map(int, input().split())
        print(f"Case #{i+1}: {a+b}")

if __name__ == "__main__":
    main()
