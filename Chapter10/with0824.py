# with 구문을 사용하면 자동으로 file close 해준다.
with open("E:/python/Chapter10/filetest/data0823.txt", "r", encoding="utf8") as file:
    data = file.read()
    print(data)