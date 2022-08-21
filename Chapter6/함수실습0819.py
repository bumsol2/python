#정의
def printHello():
    print("Hello")
# 호출
printHello()

# 매개 변수 가 있는 함수
def sum(a, b):
    print(a + b)

sum(7, 7)

# 반환값 있는 함수
import random
def getRandomNumber():
    number = random.randint(1,10)
    return number

print(getRandomNumber())

#매개 변수와 반환 값이 있는 함수

def add(a,b):
    result = a + b
    return result

print(add(5,6))