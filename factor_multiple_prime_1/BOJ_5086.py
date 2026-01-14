# BOJ 5086

import sys

def main():
    input = sys.stdin.readline

    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break

        if b % a == 0:
            print("factor")
        elif a % b == 0:
            print("multiple")
        else:
            print("neither")

if __name__ == "__main__":
    main()