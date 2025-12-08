import sys

def main():
    input = sys.stdin.readline # 입력 빠르게
    a, b = map(int, input().split())
    print(a / b)
    
if __name__ == "__main__":
    main()