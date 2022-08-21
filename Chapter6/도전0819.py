#로또번호 6개 생성
# 로또 번호 1~45까지 랜덤번호
# 6개 숫자 다 달라야된다.
#1. 반복문, 조건문
# 2. 리스트
# 3.함수 
import random
def getRandomNumber():
    number = random.randint(1,45)
    return number

lotto_num = [] # 로또 번호 저장할 리스트 

count = 0 #현재 뽑은 숫자의 갯수

while True:  # 숫자 6개
    if count > 5:
        break
    random_number = getRandomNumber() #random_number 변수 랜덤 숫자 
    if random_number not in lotto_num:
        lotto_num.append(random_number) #lottonum 리스트에 추가
        count += 1

lotto_num.sort()   #정렬

for num in lotto_num:
    print(num, end=" ")





