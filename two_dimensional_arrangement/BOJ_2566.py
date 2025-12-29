# BOJ 2566

import sys

def main():
    input = sys.stdin.readline
    
    # 같이 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 
    # 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.
    n, m = 9, 9
    max = -10**18
    max_i = 0
    max_j = 0
    
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] > max:
                max = grid[i][j]
                max_i = i+1
                max_j = j+1
    
    print(max)
    print(max_i, max_j)
    

if __name__ == "__main__":
    main()
