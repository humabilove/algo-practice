# BOJ 10813

import sys

def main():
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    arr = list(range(N+1))
    while M:
        i, j = map(int, input().split())
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        M -= 1
    arr.pop(0)
    print(*arr)

if __name__ == "__main__":
    main()
