# BOJ 11720

import sys

def main():
    input = sys.stdin.readline
    
    N = int(input())
    str = input().strip()
    sum = 0
    for i in range(N):
        sum += int(str[i])
    print(sum)

if __name__ == "__main__":
    main()
