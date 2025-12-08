import sys

def main():
    input = sys.stdin.readline
    a, b = map(int, input().split())
    print(a+b)
    
if __name__ == "__main__":
    main()