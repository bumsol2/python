#raise 예외("에러메세지")
# class 예외(Exception):
#  def __ init__(self):
#   super().__init__("에러메세지")
#Exception 밑에 ValueError 
class PositiveNumberError(Exception):
    def __init__(self):
        super().__init__("양수입력불가하다")

try:
    num = int(input("음수 입력해"))
    if num >= 0:
        raise PositiveNumberError
except PositiveNumberError as s:
    print("에러발생",s)

# class PositiveNumberError(Exception):
#     def __init__(self):
#         super().__init__("양수는 입력 불가")

# try:
#     num = int(input("음수를 입력해 주세요>>>"))
#     if num >= 0:
#         raise PositiveNumberError
# except PositiveNumberError as e:
#     print("에러 발생!", e)