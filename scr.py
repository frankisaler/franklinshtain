from transliterate import translit
from re import findall
from fake import *
import json
from datetime import datetime
from selenium import webdriver
from outlook import go
import unittest, time, re

creat_person()
go.setUp(unittest.TestCase)
go.outlook(unittest.TestCase)