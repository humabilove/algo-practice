# BOJ 2501

import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    
    cnt = 0
    for i in range(1, N+1):
        if N % i == 0:
            cnt += 1
            if cnt == K:
                print(i)
                return
    print(0)
    

if __name__ == "__main__":
    main()
