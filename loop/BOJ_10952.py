# BOJ 10952

import sys

def main():
    input = sys.stdin.readline
    
    while True:
        a, b = map(int, input().split())
        if a+b == 0:
            break
        else:
            print(a+b)
    

if __name__ == "__main__":
    main()
