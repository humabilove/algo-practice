# BOJ 10871

import sys

def main():
    input = sys.stdin.readline
    
    N, v = map(int, input().split())
    
    arr = list(map(int, input().split()))

    res = [x for x in arr if x < v]
    if res:
        print(*res)

if __name__ == "__main__":
    main()
