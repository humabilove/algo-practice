# BOJ 25206

import sys

def main():
    input = sys.stdin.readline
    
    # 전공 평점을 계산해주는 프로그램 작성
    # 전공 평점 = 전공 과목별 (학점 x 과목평점)의 합을 학점의 총합으로 나눈 것
    # 등급이 P / F인 과목은 계산에서 제외해야 한다
    # 20줄에 걸쳐 입력이 됨
    # 적어도 한 과목은 등급이 P가 아님이 보장이 된다
    
    credits = []
    grades = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}
    total = 0
    
    for _ in range(20):
        line = list(input().split())
        if line[2] == 'P':
            continue
        # 학점이 지금 string이기 때문에 float로 변환
        credit = float(line[1])
        credits.append(credit)
        # 총합에 더해줌
        total += credit * grades.get(line[2])
    print(round(total / sum(credits),6))
if __name__ == "__main__":
    main()
