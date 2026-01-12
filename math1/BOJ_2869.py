# BOJ 2869

import sys

def main():
    input = sys.stdin.readline
    
    A, B, V = map(int, input().split())
    
    target = V - A
    daily = A - B
    
    # target을 daily로 올림 나눗셈
    days = (target + daily - 1) // daily
    print(days + 1)

if __name__ == "__main__":
    main()
