#파이썬 객체 pickle로 저장
import pickle

data =  {
    "목표1": "매일 링피트 1회",
    "목표2": "매일 코딩 2시간이상"
}

file = open("E:/python/Chapter10/data2.pickle","wb")
pickle.dump(data,file)
file.close()

file = open("E:/python/Chapter10/data2.pickle","rb")
data = pickle.load(file)
print(data)
file.close()
