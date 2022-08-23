#try :예외발생
#except:예외발생시 실행
#else:예외발생하지 않을떄
#finally :항상
# 원화를 입력, 환율 입력 -> 달러값

won = input("원화금액을 입력해>>>")
dollar = input("환율을 입력해>>>")

try: # 예외가 발생 할 수 있는 코드
    print(int(won) / int(dollar))
except ValueError as s: # 문자 넣을시 출력
    print("문자열 예외가 발생했다.", s)
except ZeroDivisionError as s: #나누기 0 넣으면 출력
    print("나누기 0은 불가능하다.", s)
else: #숫자 넣으면 출력
    print("예외가 발생하지 않았을 때 실행되는 코드")
finally: # 무조건 실행, 리소스 반환시 코드 
    print("예외가 발생하던지, 발생하지 않던지 항상 실행되는 코드")