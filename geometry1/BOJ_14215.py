# BOJ 14215

import sys

def main():
    input = sys.stdin.readline
    
    a, b, c = map(int, input().split())
    
    small_two = sum((a,b,c)) - max((a,b,c))
    if small_two <= max((a,b,c)):
        res = small_two * 2 - 1
    else:
        res = a + b + c
    
    print(res)

if __name__ == "__main__":
    main()
