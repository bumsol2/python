#클래스를 사용하는 이유
champion1_name ="그웬"
champion1_health = 700
champion1_attack = 90

print(f"{champion1_name}님 소환사의 협곡에 오신것을 환영합니다.")

champion2_name ="비에고"
champion2_health = 800
champion2_attack = 95

print(f"{champion2_name}님 소환사의 협곡에 오신것을 환영합니다.")

champion3_name ="야스오"
champion3_health = 900
champion3_attack = 100

print(f"{champion3_name}님 소환사의 협곡에 오신것을 환영합니다.")

def basic_attack(name, attack):
    print(f"{name} 기본공격 {attack}")

basic_attack(champion1_name, champion1_attack)
basic_attack(champion2_name, champion2_attack)
basic_attack(champion3_name, champion3_attack)

print("==========클래스를 사용하는 경우==========")

class Champion:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        print(f"{name}님 소환사의 협곡에 오신것을 환영합니다.")
    def basic_attack(self):
        print(f"{self.name} 기본공격 {self.attack}")

ezreal = Champion("이즈리얼", 700, 90)
leesin = Champion("리신", 800, 95)
yeasuo = Champion("야스오", 900, 100)
ezreal.basic_attack()
leesin.basic_attack()
yeasuo.basic_attack()

#인스턴스=클래스이름() goblin= monster()
#인스턴스.메서드()    goblin.say()