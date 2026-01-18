# BOJ 9063

import sys

def main():
    input = sys.stdin.readline
    
    N = int(input().strip())
    X = []
    Y = []
    
    if N == 1:
        print(0)
        return 0
    
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    
    print((max(X) - min(X)) * (max(Y) - min(Y)))

if __name__ == "__main__":
    main()
