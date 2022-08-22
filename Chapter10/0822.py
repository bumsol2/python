# 파일 열기 => 작업 => 닫기 
# (w)write:덮어쓰기,(a)append:이어쓰기,(r)read 
#1.파일 쓰기
file = open("E:/python/Chapter10/filetest/data0823.txt", "w", encoding="utf8")
file.write("1.인생은고통이다")
file.close 

#2. 파일추가
file = open("E:/python/Chapter10/filetest/data0823.txt", "a", encoding="utf8")
file.write("\n2.상위 5% 뺴면 시궁창이다.")
file.close()

# 파일 읽기
file = open("E:/python/Chapter10/filetest/data0823.txt", "a", encoding="utf8")

# 3.1 파일 전체 읽기
data1 = file.read()
print(data1)
file.close()

# 3.2 파일 한줄 읽기
while True:
    data1 = file.readline()
    print(data1)
    if data1 == "":
        break
file.close()