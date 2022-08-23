import csv


file = open("E:/python/Chapter10/student2.csv", "r", encoding="utf-8-sig")
reader = csv.reader(file)
for s in reader:
    print(s)
file.close()