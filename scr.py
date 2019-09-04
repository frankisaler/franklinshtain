from transliterate import translit
from re import findall
from fake import *
import json
from datetime import datetime
from selenium import webdriver
from outlook import out
import unittest, time, re
import boto3
import logging
from botocore.exceptions import ClientError
from swap_ip import *
from selenium import webdriver
from instagram import inst
from fivesim import  *

need_ip()
while True:
	bot_whait_ip()
	creat_person()
	balance = get_balance()
	if int(balance) <= 4:
		break
	else:
		inst.inst_setup(unittest.TestCase)
		inst.inst_start(unittest.TestCase)
		need_ip()




