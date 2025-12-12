# BOJ 8393

import sys


def main():
    input = sys.stdin.readline
    
    num = int(input())
    # 1부터 n까지의 합 = n*(n+1)/2
    result = num * (num + 1) // 2
    print(result)
    

if __name__ == "__main__":
    main()
