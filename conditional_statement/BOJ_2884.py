# BOJ 2884

import sys

def main():
    input = sys.stdin.readline
    
    H, M = map(int, input().split())
    if M >= 45:
        print(H, M-45)
    else:
        print((H+23)%24, M+15)

if __name__ == "__main__":
    main()