# BOJ 11653

import sys

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    
    d = 2
    while d * d <= n:
        while n % d == 0:
            n //= d
            print(d)
        d += 1
    
    if n > 1:
        print(n)        

if __name__ == "__main__":
    main()
