# BOJ 10810

import sys

def main():
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    arr = [0] * (N+1)
    
    while M:
        i, j, k = map(int, input().split())
        for idx in range(i,j+1):
            arr[idx] = k
            
        M -= 1
    
    arr.pop(0)
    print(*arr)
    
if __name__ == "__main__":
    main()
