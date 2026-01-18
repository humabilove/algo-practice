# BOJ 1085

import sys

def main():
    input = sys.stdin.readline
    
    x, y, w, h = map(int, input().split())
    print(min(x, y, w-x, h-y))

if __name__ == "__main__":
    main()
