#실습 문제 5.2.2

data = [] #빈 리스트


a = int(input("1일차 턱걸이 횟수 "))
data.append(a)
a = int(input("2일차 턱걸이 횟수 "))
data.append(a)
a = int(input("3일차 턱걸이 횟수 "))
data.append(a)
a = int(input("4일차 턱걸이 횟수 "))
data.append(a)
a = int(input("5일차 턱걸이 횟수 "))
data.append(a)
a = int(input("6일차 턱걸이 횟수 "))
data.append(a)
a = int(input("7일차 턱걸이 횟수 "))
data.append(a)

total = data[0] + data[1] + data[2] + data[3] + data[4] + data[5] +data[6]

avg = total / 7
print(int(avg))



