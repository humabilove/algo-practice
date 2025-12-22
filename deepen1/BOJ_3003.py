# BOJ 3003

import sys

def main():
    input = sys.stdin.readline
    
    chess = [1,1,2,2,2,8]
    real = list(map(int, input().split()))
    res = []
    for i in range(6):
        res.append(chess[i] - real[i])
    print(*res)
        
        

if __name__ == "__main__":
    main()
