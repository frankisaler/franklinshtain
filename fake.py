from random import randint
from re import findall
from python3_anticaptcha import ImageToTextTask
import json
from datetime import datetime
from connect import *
import boto3
import logging
from botocore.exceptions import ClientError

def first_name():
	with open(r'data\first.txt', 'r', encoding='UTF-8') as f:
		find = findall(r'[\S]+', f.read())
		R = randint(0, len(find) - 1)
		return find[R]
	
def last_name():	
	with open(r'data\last.txt', 'r', encoding='UTF-8') as f:
		find = findall(r'[\S]+', f.read())
		R = randint(0, len(find) - 1)
		return find[R]

def fish():
	with open(r'data\fish.txt', 'r', encoding='UTF-8') as f:
		find = findall(r'[\S]+', f.read())
		R = randint(0, len(find) - 1)
		fish = find[R]
		return fish.lower()

def password():
	password = ''
	for n in range(randint(10, 16)):
		printable = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*'
		x = randint(0, len(printable) - 1)
		password += printable[x]
	return password

def login(first, last):
	fishka = fish()
	fdiv = int(int(len(first)) / 2)
	ldiv = int(int(len(last)) / 2)
	return last[0:ldiv] + fishka + first[0:fdiv].lower()

def mounth():
	mounths_rus = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
	mounths_eng = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	how = randint(0, 11)
	return mounths_eng[how]

def day():
	day = ''
	day += str(randint(1, 28))
	return day

def year():
	year = ''
	year = str(randint(1975, 2002))
	return year

def captcha(image_link):
	ANTICAPTCHA_KEY = "059b63917d2c27b0a6874c943867581d"
	answer_user = ImageToTextTask.ImageToTextTask(anticaptcha_key = ANTICAPTCHA_KEY).captcha_handler(captcha_link=image_link)
	return answer_user

def dt():
	return findall(r'[\S]+', str(datetime.now()))

def ip():
	for server in conn.compute.servers():
		addresses = server['addresses']
		return addresses['network_5435'][1]['addr']

def creat_person():
	first = first_name()
	last = last_name()
	log = login(first, last)
	d = dt()
	fake = {
		'first':first,
		'last':last,
		'first_last':first + ' ' + last,
		'login':log,
		'password':password(),
		'mounth':mounth(),
		'day':day(),
		'year':year(),
		'email':log + '@outlook.com',
		'date':str(d[0][8:10]) + '-' + str(d[0][5:7]) + '-' + str(d[0][0:4]),
		'time':d[1][0:8],
		'ip':ip()
	}
	with open(r'temp\person.json', 'w') as p:
		person = []
		person.append(fake)
		json.dump(person, p, indent=2)

def jload():
	with open(r'temp\person.json', 'r') as p:
		jlo = json.load(p)
		return jlo[0]

def write_outlook_json():
	json_file = r'temp\outlook.json'
	write_dict = jload()
	s3 = boto3.client('s3')
	with open(json_file, 'wb') as f:
		s3.download_fileobj('franki', 'outlook.json', f)
	try:
		data = json.load(open(json_file))
	except:
		data = []
	data.append(write_dict)
	with open(json_file, 'w') as file:
		json.dump(data, file, indent=2)
	s3.upload_file(json_file, 'franki', 'outlook.json')

def write_instagram_json(tel_number):
	telephone = {'phone':tel_number}
	json_file = r'temp\instagram.json'
	write_dict = jload()
	s3 = boto3.client('s3')
	with open(json_file, 'wb') as f:
		s3.download_fileobj('franki', 'instagram.json', f)
	try:
		data = json.load(open(json_file))
	except:
		data = []
	data.append(write_dict)
	data.append(telephone)
	with open(json_file, 'w') as file:
		json.dump(data, file, indent=2)
	s3.upload_file(json_file, 'franki', 'instagram.json')