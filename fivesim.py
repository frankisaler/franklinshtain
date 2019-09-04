import requests
import json
from re import findall
from time import sleep


base_url = 'http://api1.5sim.net/stubs/handler_api.php?api_key=53ca6852e3d345639eafd562f190bb9a&action='

def get_balance():
	r = requests.get(base_url + 'getBalance')
	money = findall(r'[\d]+', r.text)
	return money[0]

def buy_number(service):
	r = requests.get(base_url + 'getNumber&service=' + str(service) + '&country=russia')
	zakaz = findall(r'[\d]+' , r.text)
	print(zakaz)
	return zakaz

def set_ok(number_id):
	r = requests.get(base_url + 'getStatus&status=1&id=' + str(number_id) + '&forward=$forward')
	print(r.text)

def set_double(number_id):
	r = requests.get(base_url + 'setStatus&status=3&id=' + str(number_id) + '&forward=$forward')
	print(r.text)

def order_status(number_id):
	r = requests.get(base_url + 'getStatus&id=' + str(number_id))
	code = findall(r'[\d]+' , r.text)
	len_code = len(code)
	sleep(3)
	while int(len_code) <= 0:
		r = requests.get(base_url + 'getStatus&id=' + str(number_id))
		code = findall(r'[\d]+' , r.text)
		len_code = len(code)
		sleep(3)
		print(len_code)
		print(r.text)
	r = requests.get(base_url + 'getStatus&id=' + str(number_id))
	code = findall(r'[\d]+' , r.text)
	print(code[0])
	return code[0]

'''
        airbnb
        akelni
        alibaba
        amazon
        aol
        avito
        azino
        bittube
        blablacar
        blizzard
        blockchain
        burgerking
        careem
        delivery
        dent
        discord
        dixy
        drom
        drugvokrug
        dukascopy
        ebay
        edgeless
        electroneum
        facebook
        fiverr
        forwarding
        gameflip
        gcash
        gett
        globus
        glovo
        google
        grabtaxi
        green
        hqtrivia
        icard
        icq
        instagram
        iost
        jd
        kakaotalk
        komandacard
        lazada
        lenta
        line
        linkedin
        livescore
        magnolia
        mailru
        mamba
        michat
        microsoft
        naver
        netflix
        nimses
        odnoklassniki
        okey
        olx
        openpoint
        oraclecloud
        other
        ozon
        paymaya
        perekrestok
        pokermaster
        proton
        pyaterochka
        qiwiwallet
        reuse
        ripkord
        seosprint
        shopee
        skout
        steam
        tantan
        telegram
        tencentqq
        tinder
        truecaller
        twitter
        uber
        vernyi
        viber
        vkontakte
        voopee
        wechat
        weku
        whatsapp
        yahoo
        yalla
        yandex
        youdo
        youla
'''