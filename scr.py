from transliterate import translit
from re import findall
from fake import *
import json
from datetime import datetime
from selenium import webdriver
from outlook import go
import unittest, time, re
import boto3
import logging
from botocore.exceptions import ClientError


creat_person()
file = []
new =  open(r'temp\person.json', 'r')
new_person = json.load(new)
file.append(new_person[0])
new.close()



'''
s3 = boto3.client('s3')
with open('temp\outlook.json', 'wb') as f:
		s3.download_fileobj('franki', 'outlook.json', f)
'''
out =  open(r'temp\outlook.json', 'r')
outlook = json.loads(out)
file.append(outlook[0])
out.close()

with open(r'temp\outlook.json', 'w') as d:
	json.dumps(file, d, indent=2)

s3.upload_file('temp\outlook.json', 'franki', 'outlook.json', ExtraArgs={'ACL': 'public-read'})

'''
except:
	print('No file on server')


data_outlook = open(r'temp\outlook.json', 'r')
outlook = json.load(data_outlook)
print(outlook)



with open(r'temp\outlook.json', 'r') as save:		
	load_json = json.load(save)
	file.append(load_json[0])
	file.append(jlo[0])
	print('\nok_download \n' + load_json)
with open('temp\outlook.json', 'w') as f:
	json.dump(file, f, indent=2)

s3.upload_file('temp\outlook.json', 'franki', 'outlook.json', ExtraArgs={'ACL': 'public-read'})
'''