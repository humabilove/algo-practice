# BOJ 10871

import sys

def main():
    input = sys.stdin.readline
    
    N, v = map(int, input().split())
    
    arr = list(map(int, input().split()))

    # trailing space 없이 출력하려면 결과를 모아 한 번에 출력합니다
    res = [x for x in arr if x < v]
    if res:
        print(*res)

if __name__ == "__main__":
    main()
