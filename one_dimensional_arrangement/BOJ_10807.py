# BOJ 10807

import sys

def main():
    input = sys.stdin.readline
    
    N = int(input())
    arr = list(map(int, input().split()))
    num = int(input())
    count = 0
    for i in range(N):
        if num == arr[i]:
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()
