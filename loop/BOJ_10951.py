# BOJ 10951

import sys

def main():
    input = sys.stdin.readline
    
    for line in sys.stdin:
        a, b = map(int, line.split())
        print(a+b)
        
if __name__ == "__main__":
    main()
