# BOJ 11005

import sys

def main():
    input = sys.stdin.readline
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    N, B = map(int, input().split())
    
    if N == 0:
        print("0")
        return
    
    res = []
    
    while N>0:
        N, r = divmod(N, B)
        res.append(digits[r])
    
    print(''.join(reversed(res)))

if __name__ == "__main__":
    main()
