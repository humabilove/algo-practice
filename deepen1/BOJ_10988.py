# BOJ 10988

import sys

def main():
    input = sys.stdin.readline
    
    string = list(input().strip())
    string2 = list(reversed(string))
    
    if string == string2:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()
