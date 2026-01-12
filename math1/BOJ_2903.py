# BOJ 2903

import sys

def main():
    input = sys.stdin.readline
    
    N = int(input())
    print(4**N + 2**(N+1) + 1)

if __name__ == "__main__":
    main()
