# BOJ 2753

import sys

def main():
    input = sys.stdin.readline
    
    year = int(input())
    
    if year % 4 == 0:
        if year % 400 == 0:
            print(1)
        elif year % 100 == 0:
            print(0)
        else:
            print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()
