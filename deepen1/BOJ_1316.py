# BOJ 1316

import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    count = 0
    
    for _ in range(N):
        s = input().strip()
        seen = set()
        last = ''
        is_group = True
        for ch in s:
            if ch != last:
                # 현재 문자가 이전 문자와 다를 때
                if ch in seen:
                    is_group = False
                    break
                seen.add(ch)
                last = ch
            else:
                # 같은 문자 연속이면 그냥 통과
                continue
        if is_group:
            count += 1
    
    print(count)
    
if __name__ == "__main__":
    main()
