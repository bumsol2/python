version = 3.0

def printAuther():
    print("코딩 시작")

#zmffotm
class Pay:
    def __init__(self, id, price, time):
        self.id = id
        self.price = price
        self.time = time
    def get_pat_info(self):
        return f"{self.time} {self.id} {self.price}"
    