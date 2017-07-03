#!/usr/bin/env python
# -*- coding: utf-8 -*-

####***THIS SCRIPT USES PYTHON 3.7***####

from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import random, string, requests, os

dirname = "Output"


# - Generates lightshot link using generateId() function
def generateLink(nomeImg):
    return "https://prnt.sc/" + nomeImg


# - Generates random string
def generateId(size):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(size))


# - Downloads HTML file from link previously generated
def generateHtml(nomeImg):
    url = generateLink(nomeImg)
    page = requests.get(url)
    return page


# - Looks for raw image link in HTML file
def generateImgur(url, nomeImg):
    soup = BeautifulSoup(generateHtml(nomeImg).content, 'html.parser')
    imgUrl = soup.find('img', id='screenshot-image')['src']

    # - Prevents "Error Image" From being downloaded
    if imgUrl != "//st.prntscr.com/2017/07/03/0920/img/0_173a7b_211be8ff.png":
        pathArquivo = dirname + "/" + nomeImg + ".png"
        urlretrieve(imgUrl, pathArquivo)
        print("New File Downloaded to Output")

    else:
        print("Url not found.")


# - Creates "Output" folder if not present
if not os.path.exists(dirname):
    os.makedirs(dirname)

while True:
    nomeImg = generateId(5)
    url = generateLink(nomeImg)
    generateImgur(url, nomeImg)
