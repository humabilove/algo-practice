# BOJ 5073

import sys

def main():
    input = sys.stdin.readline
    
    while True:
        a, b, c = map(int, input().split())
        if a == b == c == 0:
            break
        if sum((a,b,c)) - max((a,b,c)) <= max((a,b,c)):
            print("Invalid")
        elif a == b == c:
            print("Equilateral")
        elif a == b or b == c or c == a:
            print("Isosceles")
        else:
            print("Scalene")
        

if __name__ == "__main__":
    main()
