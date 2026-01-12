# BOJ 2745_2

import sys

def main():
    input = sys.stdin.readline
    
    N, B = input().split()
    B = int(B)
    
    ans = 0
    for ch in N:
        if '0' <= ch <= '9':
            v = ord(ch) - ord('0')
        else:
            v = ord(ch) - ord('A') + 10
        ans = ans * B + v
        
    print(ans)

if __name__ == "__main__":
    main()
