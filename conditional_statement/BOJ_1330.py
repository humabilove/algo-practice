# BOJ 1330

import sys

def main():
    input = sys.stdin.readline
    
    a, b = map(int, input().split())
    if a>b:
        print(">")
    elif a<b:
        print("<")
    else:
        print("==")

if __name__ == "__main__":
    main()
