import sys

def main():
    input = sys.stdin.readline # 입력 빠르게
    x = int(input())
    y = int(input())
    n_1 = x * (y % 10)
    n_10 = x * ((y % 100) // 10)
    n_100 = x * (y // 100)
    print(n_1)
    print(n_10)
    print(n_100)
    print(n_100*100 + n_10*10 + n_1)
    
if __name__ == "__main__":
    main()