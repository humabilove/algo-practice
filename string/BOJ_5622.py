# BOJ 5622

import sys

def main():
    input = sys.stdin.readline
    
    time = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]
    string = input().strip()
    total_time = 0
    for ch in string:
        total_time += time[ord(ch) - 65]
    print(total_time)

if __name__ == "__main__":
    main()
