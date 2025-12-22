# BOJ 5597

import sys

def main():
    input = sys.stdin.readline
    
    arr = [0] * 31
    for _ in range(28):
        idx = int(input())
        arr[idx] = 1

    for i in range(31):
        if i == 0:
            continue
        if arr[i] == 0:
            print(i)
    

if __name__ == "__main__":
    main()
