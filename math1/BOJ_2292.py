# BOJ 2292

import sys

def main():
    input = sys.stdin.readline
    
    N = int(input())
    
    i = 1
    
    while True:
        # 처음엔 i = 1
        upper = 3*(i**2) - 3*i + 1
        if N <= upper:
            print(i)
            break
        i += 1
if __name__ == "__main__":
    main()
