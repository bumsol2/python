#8.1.1
# 개발자 MMORPG 게임아이템구성안 만들었다
# 아이템 공통 : 이름, 가격, 무게, 판매하기, 버리기
# 장비 아이템 : 착용효과, 착용하기
# 소모품 아이템 : 사용효과, 사용하기
# (단, 버리기는 버릴 수 있는 아이템만 가능하다)
# 그리고 구성안을 토대로 클래스 다이어그램을 설계하였다. 


class item:
    def __init__(self, name, price, weight, drop):
        self.name = name
        self.price = price
        self.weight = weight
        self.drop = drop

    def sale(self):  #공통된 메서드 판매
        print(f"[{self.name}] 판매가격은 [{self.price}]")
    
    def discard(self):  #버리는 메서드
        if self.drop:
            print(f"[{self.name}] 버렸습니다.") 
        else:
            print(f"[{self.name}] 버릴 수 없습니다.")

class WearItem(item): #장비아이템
    def __init__(self, name, price, weight, drop, effect): #사용효과 추가
        super().__init__(name, price, weight, drop) #부모클래스 호출
        self.effect = effect         
    def wear(self):  #착용효과
        print(f"[{self.name}] 착용했다. {self.effect}")    

class Expendables(item):    #소모품아이템
    def __init__(self, name, price, weight, drop, effect):
        super().__init__(name, price, weight, drop) #부모클래스 호출
        self.effect = effect
    def use(self): #사용하기
        print(f"[{self.name}]사용했다. {self.effect}")

# 장비 생성
sword = WearItem("광선검", 100000, 4.5, True, "체력 10000증가, 마력 500000증가")
sword.wear()
sword.sale()
sword.discard()

potion = Expendables("초강력물약", 1500000, 0.5, False, "모든능력 백배증가 지속")
potion.discard()
potion.sale()
potion.use()


    



# 아이템 공통 : 이름, 가격, 무게, 판매하기, 버리기
# 장비 아이템 : 착용효과, 착용하기
# 소모품 아이템 : 사용효과, 사용하기
# (단, 버리기는 버릴 수 있는 아이템만 가능하다)
# 구성안과 설계도를 보고 클래스를 코드로 완성해보자. 
# (메서드 구현은 자유롭게 한다)
