from pyautogui import *
from time import sleep
from random import randint

def speed():
	spd = randint(1, 10)
	floatspd = spd / 10
	speed = float(floatspd)
	return speed

def tp(write):
	typewrite(write)
	press('enter')
	sleep(5)

def tp2(write):
	s = speed()
	typewrite(write, s)

def tp3(write):
	typewrite(write)
	press('tab')
	sleep(2)

def tp4(write):
	wrt = []
	wrt.append(write)
	wrt_one = wrt[0]
	print(wrt_one)
	wrt_len = len(wrt_one)
	print(wrt_len)
	b = 0
	while b != wrt_len:
		spd = speed()
		typewrite(wrt_one[b], spd)
		b += 1
	sleep(2)

def mt(pos1, pos2):
	spd = speed()
	moveTo(pos1, pos2, spd)
	click()
	sleep(3)

