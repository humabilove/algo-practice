# BOJ 10811

import sys

def main():
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    arr = list(range(N+1))
    while M:
        i, j = map(int, input().split())
        arr[i:j+1] = arr[i:j+1][::-1]
        M -= 1
    print(*arr[1:])

if __name__ == "__main__":
    main()
