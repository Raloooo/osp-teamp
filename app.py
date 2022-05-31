#!/usr/bin/python3
#-*- coding: utf-8 -*-



import re
import requests
import urllib.request
import time
import random

from elasticsearch import Elasticsearch
from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask import render_template
from flask import request

from selenium import webdriver as web #웹 자동클릭 구현 위한 WEBDRIVER use 

op = web.ChromeOptions()
op.add_argument("no-sandbox")
op.add_argument("--disable-dev-shm-usage")
op.add_argument("user-agent={Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Chrome/102.0.5005.61 Firefox/100.0}")


driver = web.Chrome(executable_path='/home/shin/chromedriver', options = op)

randtime = random.uniform(1,2)
time.sleep(randtime)
driver.get("https://knuin.knu.ac.kr/public/stddm/lectPlnInqr.knu")
randtime = random.uniform(1,2)
time.sleep(randtime)

# 동적 드롭박스 클릭 과정
driver.find_element(By.XPATH, '//*[@id="schSbjetCd1"]/option[6]').click() #elements가 아닌 element
driver.find_element(By.XPATH, '//*[@id="schSbjetCd2"]/option[16]').click()
driver.find_element(By.XPATH, '//*[@id="schSbjetCd3"]/option[2]').click()
driver.find_element(By.CSS_SELECTOR, '#btnSearch').click()


