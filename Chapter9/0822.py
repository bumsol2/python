#내장모듈
# 파이썬 설치시 자동 모듈 

from math import pi, ceil as c
print(pi)
print(c(2.7))

#외부모듈
# : 다른 사람이 만든 파이썬 파일 pip로 설치해서 사용
# pyautogui
import pyautogui as pg

pg.moveTo(500, 500, duration=2, tween=pg.easeInOutQuad)
