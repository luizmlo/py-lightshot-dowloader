#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import random, string, requests, os

dirname = "Output"

# Functions
def generateLink(nomeImg):
    return "https://prnt.sc/" + nomeImg

def generateId(size):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(size))

def generateHtml(nomeImg):
    url = generateLink(nomeImg)
    page = requests.get(url)
    return page

def generateImgur(url, nomeImg):
    soup = BeautifulSoup(generateHtml(nomeImg).content, 'html.parser')
    imgUrl = soup.find('img', id='screenshot-image')['src']

    if imgUrl != "//st.prntscr.com/2017/07/03/0920/img/0_173a7b_211be8ff.png":
        pathArquivo = dirname + "/" + nomeImg + ".png"
        urlretrieve(imgUrl, pathArquivo)

    else:
        print("Url not found.")

# Initialization

if not os.path.exists(dirname):
    os.makedirs(dirname)

while True:
    nomeImg = generateId(5)
    url = generateLink(nomeImg)

    generateImgur(url, nomeImg)

