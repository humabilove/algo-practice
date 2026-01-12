# BOJ 1193

import sys

def main():
    input = sys.stdin.readline
    X = int(input().strip())
    
    line = 1
    end = 1
    
    while X > end:
        line += 1
        end += line
    
    idx = X - (end - line) - 1
    
    if line % 2 == 0:
        num = 1 + idx
        den = line - idx
    else:
        num = line - idx
        den = 1 + idx
    
    print(f"{num}/{den}")
    

if __name__ == "__main__":
    main()
