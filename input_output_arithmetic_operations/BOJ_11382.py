import sys

def main():
    input = sys.stdin.readline
    a, b, c = map(int, input().split())
    print(a+b+c)
    
if __name__ == "__main__":
    main()