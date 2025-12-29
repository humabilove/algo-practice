# BOJ 2563

import sys

def main():
    input = sys.stdin.readline
    
    N = int(input())
    
    # 전체 도화지 행렬 생성 (처음엔 전부 0을 갖는 값으로)
    r, c = 100, 100
    grid = [[0]*c for _ in range(r)]
    
    while N:
        n, m = map(int, input().split())
        for i in range(n,n+10):
            for j in range(m, m+10):
                grid[i][j] = 1
        N -= 1
    
    count = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                count += 1
    
    
    print(count)
    
if __name__ == "__main__":
    main()
