study = int(input("공부시간입력해"))

if study >= 10:
    print("휴대폰잠금해제")
elif study >= 5:
    print("휴대폰30분 사용가능")
else:
    print("사용불가")