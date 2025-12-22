# BOJ 2562

import sys

def main():
    input = sys.stdin.readline
    
    max = 0
    for i in range(1,10):
        num = int(input())
        if max < num:
            max = num
            idx = i
    print(max)
    print(idx)

if __name__ == "__main__":
    main()
