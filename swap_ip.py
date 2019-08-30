import boto3
import logging
from botocore.exceptions import ClientError
from time import sleep



def active_ip():
	stat = 'active_ip'
	with open('temp\stat_ip.txt', 'w', encoding='UTF-8') as stat_ip:
		stat_ip.write(stat)
	s3 = boto3.client('s3')
	s3.upload_file('temp\stat_ip.txt', 'franki', 'stat_ip.txt', ExtraArgs={'ACL': 'public-read'})

def boss_whait_ip():
	s3 = boto3.client('s3')
	with open('temp\stat_ip.txt', 'wb') as f:
		s3.download_fileobj('franki', 'stat_ip.txt', f)
	status = open('temp\stat_ip.txt', 'r', encoding='UTF-8')
	stat = status.read()
	while stat != 'need_ip':
		print(stat)
		status.close()		
		with open('temp\stat_ip.txt', 'wb') as f:
			s3.download_fileobj('franki', 'stat_ip.txt', f)
		status = open('temp\stat_ip.txt', 'r', encoding='UTF-8')
		stat = status.read()  
		sleep(10)

def need_ip():
	stat = 'need_ip'
	with open('temp\stat_ip.txt', 'w', encoding='UTF-8') as stat_ip:
		stat_ip.write(stat)
	s3 = boto3.client('s3')
	s3.upload_file('temp\stat_ip.txt', 'franki', 'stat_ip.txt', ExtraArgs={'ACL': 'public-read'})

def bot_whait_ip():
	s3 = boto3.client('s3')
	with open('temp\stat_ip.txt', 'wb') as f:
		try:
			s3.download_fileobj('franki', 'stat_ip.txt', f)
		except:
			stat = 'need_ip'
	status = open('temp\stat_ip.txt', 'r', encoding='UTF-8')
	stat = status.read()			
	while stat == 'need_ip':
		print(stat)
		status.close()		
		with open('temp\stat_ip.txt', 'wb') as f:
			try:
				s3.download_fileobj('franki', 'stat_ip.txt', f)				
			except:
				stat = 'need_ip'
				print(stat + ' sleep_30')
				sleep(30)
		status = open('temp\stat_ip.txt', 'r', encoding='UTF-8')
		stat = status.read()
		print(stat + ' sleep_10')
		sleep(10)