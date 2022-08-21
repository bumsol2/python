# 상속
# 클래스 중복 코드를 제거하고 유지보수 편하기 하기위해서 사용한다고 한다.

#부모 클래스
import random

class Monster:
    max_num = 1000
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")

# 자식 클래스

class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self): #메서드 오버라이딩
        print(f"[{self.name}]헤엄치기")

class Dragon(Monster):  #드래곤만 스킬추가

    def __init__(self, name, health, attack, skill):
        super().__init__(name, health, attack)
        self.skills = ("불공격","꼬리공격","날개치기")                                         

    def move(self): #메서드 오버라이딩
        print(f"[{self.name}]날기")

    def skill(self):
        print(f"[{self.name}] 스킬사용 {self.skills[random.randint(0,2)]}")

wolf = Wolf("울프", 1500, 200)
wolf.move()

shark = Shark("샤크", 3000, 400)
shark.move()

dragon = Dragon("드래곤", 8000, 800)
dragon.move()
dragon.skill()