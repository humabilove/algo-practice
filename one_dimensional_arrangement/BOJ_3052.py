# BOJ 3052

import sys

def main():
    input = sys.stdin.readline
    
    arr = [0] * 42
    
    for i in range(10):
        num = int(input())
        idx = num % 42
        if arr[idx] == 1:
            continue
        else:
            arr[idx] = 1
    print(sum(arr))
        

if __name__ == "__main__":
    main()
