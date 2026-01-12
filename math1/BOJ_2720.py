# BOJ 2720

import sys

def main():
    input = sys.stdin.readline
    
    T = int(input())
    
    coins = [25, 10, 5, 1]
    
    while T:
        res = [0] * 4
        C = int(input())
        for i in range(4):
            r, C = divmod(C, coins[i])
            res[i] = r
            if C == 0:
                break
        print(*res)
        T -= 1
    
if __name__ == "__main__":
    main()
