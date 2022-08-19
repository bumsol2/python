while True:
    print("메뉴 입력해")
    select = int(input("1.게임시작 2. 랭킹보기 3. 게임종료"))
    
    if select == 1:
        print("게임시작")
    elif select == 2:
        print("실시간랭킹")
    elif select == 3:
        print("게임종료")
        break
    else:
        print("다시입력해")