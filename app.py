#!/usr/bin/python3
#-*- coding: utf-8 -*-



import re
import requests
import urllib.request
import time
import random
import pandas as pd # 가져온 데이터를 표로 쉽게 보기

from selenium.webdriver.support.select import Select
from elasticsearch import Elasticsearch
from urllib.request import urlopen
from html_table_parser import parser_functions as parser # table crawling
# 사용 전에 파이썬 패키지 설치 (pip install html_table_parser)
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask import render_template
from flask import request

from selenium import webdriver as web #웹 자동클릭 구현 위한 WEBDRIVER use 

op = web.ChromeOptions()
op.add_argument("no-sandbox")
op.add_argument("--disable-dev-shm-usage")
op.add_argument("headless") # 창 띄우지 않고 실행하기.
op.add_argument("user-agent={Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Chrome/102.0.5005.61 Firefox/100.0}")


driver = web.Chrome(executable_path='/home/shin/chromedriver', options = op)

randtime = random.uniform(1,2)
time.sleep(randtime)
driver.get("https://knuin.knu.ac.kr/public/stddm/lectPlnInqr.knu")
randtime = random.uniform(1,2)
time.sleep(randtime)

#dropbox click

#driver.find_element_by_xpath('//*[@id="schSbjetCd1"]/option[6]').click() #elements가 아닌 element
# driver.find_element_by_xpath('//*[@id="schSbjetCd2"]/option[16]').click()

selecting = Select(driver.find_element_by_xpath('//*[@id="schSbjetCd1"]'))
selecting.select_by_visible_text("대학");


selecting2 = Select(driver.find_element_by_xpath('//*[@id="schSbjetCd2"]'))
selecting2.select_by_visible_text("IT대학");


driver.find_element_by_css_selector('#schSbjetCd3').click();
option = driver.find_element_by_xpath("//*[text()='글로벌소프트웨어융합전공']")
#driver.execute_script("arguments[0].scrollintoView();",option)
option.click();

#selecting3 = Select(driver.find_element_by_xpath('//*[@id="schSbjetCd3"]'))
#selecting3.select_by_visible_text("글로벌소프트웨어융합전공");
driver.find_element_by_css_selector('#btnSearch').click()

html = driver.page_source #해당 사이트 정보 가져오기
soup = BeautifulSoup(html, 'html.parser')
data = soup.find('table', {'class' : 'gridHeaderTableDefault'})
indata = parser.make2d(data)
tabledata = pd.DataFrame(data=indata[1:], columns=indata[0])
tabledata

