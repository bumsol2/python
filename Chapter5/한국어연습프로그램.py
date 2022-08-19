#1.연습할 한국어 담긴 리스트
#2. 리스트 순서대로 단어 가져와 화면 출력
#3. 프로그램 사용자는 단어를 그대로 입력
#4. 맞추면 다음단어를 가져온다 틀리면 프로그램 종료

korea_word = ["헬조선","횡령","배임","내부자거래","분식회계","저출산","고령화","자살률","노인빈곤률"]

# 점수
score = 0

print("Lets lerarning korean")

for hell in korea_word:
    print(hell)
    data = input()
    if data == hell:
        score += 1 # 점수 1 증가

print("전체 문제 개수 :", len(korea_word))

print("맞힌 개수:",score)

print("틀린개수 :", len(korea_word)-score)



