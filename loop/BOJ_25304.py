# BOJ 25304

import sys

def main():
    input = sys.stdin.readline
    
    total = int(input())
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        total -= a*b
    if total == 0:
        print("Yes")
    else:
        print("No")
if __name__ == "__main__":
    main()
