# BOJ 10798

import sys

def main():
    input = sys.stdin.readline
    
    n = 5
    # 최대 열이 15개이고 출력할 때 문제가 없어야하니 ''로 초기화해주고
    # transpose할 때 zip함수를 사용하고 싶기 떄문에 행렬의 크기를 일정하게 해주기
    grid = [['']*15 for _ in range(n)]
    
    for i in range(n):
        li = list(input().strip())
        for j in range(len(li)):
            grid[i][j] = li[j]
    
    transposed = list(map(list, zip(*grid)))
    
    for i in range(15):
        for j in range(n):
            print(transposed[i][j], end="")
        

if __name__ == "__main__":
    main()
