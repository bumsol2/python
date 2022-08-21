# 생성자
# : 인스턴스를 만들 떄 호출되는 메서드

class Monster:
    def __init__(self, health, attack, speed): #1. __init__ 생성자 가장 먼저 실행 #매개변수 4개  3개
        self.health = health
        self.attack = attack
        self.speed = speed
    def decrease_health(self, num):
        self.health -= num
    def get_health(self):
        return self.health

# 고블린 인스턴스 생성
goblin = Monster(700,800,900)
goblin.decrease_health(100)
print(goblin.get_health())

# 늑대 인스턴스 생성
wolf = Monster(1500,200,350)  # 1500 => health로 200=> attack으로 , 350은 speed
wolf.decrease_health(1000)
print(wolf.get_health())