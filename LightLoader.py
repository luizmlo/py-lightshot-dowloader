#!/usr/bin/env python
# -*- coding: utf-8 -*-

####***THIS SCRIPT USES PYTHON 3.7***####

from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import random, string, requests, os

# - Output folder name.
DIRNAME = "Output"


# - Generates lightshot link using generateId() function
def generateLink(fileName):
    return "https://prnt.sc/" + fileName


# - Generates random string
def generateId(size):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(size))


# - Downloads HTML File from link previously generated
def generateHtml(fileName):
    url = generateLink(fileName)
    page = requests.get(url)
    return page


# - Looks for raw image link in HTML File
def generateImgur(url, fileName):
    soup = BeautifulSoup(generateHtml(fileName).content, 'html.parser')
    imgUrl = soup.find('img', id='screenshot-image')['src']

    # - Prevents "Error Image" From being downloaded
    if imgUrl != "//st.prntscr.com/2017/07/03/0920/img/0_173a7b_211be8ff.png":
        pathArquivo = DIRNAME + "/" + fileName + ".png"
        urlretrieve(imgUrl, pathArquivo)
        print("File: " + fileName + " - Saved to " + DIRNAME + " folder.")

    else:
        print("The requested url is invalid. Trying a new combination...")


# - Creates "Output" folder if not present
if not os.path.exists(DIRNAME):
    os.makedirs(DIRNAME)

while True:
    fileName = generateId(5)
    url = generateLink(fileName)
    generateImgur(url, fileName)
