
math = int(input("수학성적입력해"))
english =int(input("영어성적입력해"))
korean = int(input("국어성적입력해"))

total = math + english + korean

avg = total / 3

if 0 <= korean <= 100 and 0 <= math < 100 and 0<= english <=100:
    if avg >= 80:
        print("불합격")
    else:
        print("합격")

else:
    print("잘못입력")

if korean < 0 or korean > 100 or math < 0 or math > 100 or english <0 or english > 100:
    print("잘못입력하였다")
    if avg >= 80:
        print("불합격")
    else:
        print("합격")
else:
    print("잘못 입력했다.")




