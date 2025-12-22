# BOJ 10818

import sys

def main():
    input = sys.stdin.readline
    
    N = int(input())
    arr = list(map(int, input().split()))
    
    print(min(arr), max(arr))

if __name__ == "__main__":
    main()
