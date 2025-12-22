# BOJ 11718

import sys

def main():
    input = sys.stdin.readline
    res = ""
    while True:
        try:
            line = input()
            res += line
        except EOFError:
            break
    print(res)
if __name__ == "__main__":
    main()
