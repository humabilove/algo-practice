students = [] # 빈 리스트

n = int(input("학생 수를 입력하세요 : "))

for i in range(n):
    print(f"{i+1}번째 학생 정보 입력")
    
    name = input("이름 : ")
    age = int(input("나이 : " ))
    score = int(input("점수 : "))
    
    # 점수에 따라 등급
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "D"
        
    # 학생 정보를 딕셔너리로 묶기
    student = {
        "name" : name,
        "age" : age,
        "score" : score,
        "grade" : grade,
    }
    
    students.append(student) # 리스트에 추가
    print()
    
print("=== 전체 학생 정보 ===")
for s in students:
    print(f"{s['name']} ({s['age']}세) - 점수 : {s['score']}, 등급 : {s['grade']}")