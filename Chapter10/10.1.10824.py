#수익금 ,수익률 출력
#수익금 = (목표가-매입가) * 수량
#수익률 = (목표가/매입가-1) * 100

# 종목,매입가,수량,목표가
# 삼성전자,85000,10,90000
# NAVER,380000,5,400000

import csv

def showprofile(data):
    name = data[0] #종목
    purchase_price = int(data[1]) #매입가
    amount = int(data[2]) #수량
    target_price = int(data[3]) #목표가

    profit = (target_price - purchase_price) * amount 
    profit_ratio = (target_price/purchase_price-1) *100

    print(f" {name} {profit} {profit_ratio:.2f} ") 
    


# 파일 열기
file = open("E:\python\Chapter10\mystock.csv", "r", encoding='UTF-8')


# 파일 데이터 읽기
# reader = csv.reader(file)
# for data in reader[1:]: #csv 인덱싱 지원하지 않는다. list 로 형변환
#     print(data)

# file.close()

reads = list(csv.reader(file))
for data in reads[1:]: #csv 인덱싱 지원하지 않는다. list 로 형변환
    showprofile(data) 

file.close()


