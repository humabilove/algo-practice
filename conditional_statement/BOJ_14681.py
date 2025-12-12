# BOJ 14681

import sys

def main():
    input = sys.stdin.readline
    
    x = int(input())
    y = int(input())
    
    if x>0:
        if y>0:
            print(1)
        else:
            print(4)
    else:
        if y>0:
            print(2)
        else:
            print(3)

if __name__ == "__main__":
    main()
