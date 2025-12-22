# BOJ 10809

import sys

def main():
    input = sys.stdin.readline
    
    alpha = [-1]*26
    str = input().strip()
    for i in range(len(str)):
        idx = ord(str[i]) - 97
        if alpha[idx] == -1:
            alpha[idx] = i
    print(*alpha)
    
if __name__ == "__main__":
    main()
