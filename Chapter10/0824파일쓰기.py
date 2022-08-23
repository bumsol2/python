import csv

data = [
    ["이름", "반", "번호"],
    ["재석", 2, 30],
    ["아이유", 4, 9],
    ["유인나", 6, 42]
]

file = open("E:/python/Chapter10/student2.csv", "w", newline="", encoding="utf-8-sig")
writer = csv.writer(file)

for s in data:
    writer.writerow(s)

file.close()