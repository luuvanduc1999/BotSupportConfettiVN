import json
import urllib.request as urllib2
from bs4 import BeautifulSoup
from google import google
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import re
import pyscreenshot as Imagegrab
import sys
import wx
import time
from halo import Halo
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
import requests
import pickle
from colorama import Fore, Back, Style

def split_string(source):
	splitlist = ",!-.;/?@ #"
	output = []
	atsplit = True
	for char in source:
		if char in splitlist:
			atsplit = True
		else:
			if atsplit:
				output.append(char)
				atsplit = False
			else:
				output[-1] = output[-1] + char
	return output

def SearchX(qes,option):


    X1=0
    X2=0
    X3=0
    words=split_string(qes)


    driver.get("https://www.google.com/search?q="+qes+"\""+option[0]+"\"")
    a=driver.find_elements_by_class_name('st')
    ax=a[0].text+a[1].text+a[2].text
    for word in words:
        X1=X1+ax.count(word)
    print(X1)

    op2=split_string(option[1])


    driver.get("https://www.google.com/search?q="+qes+"\""+option[1]+"\"")
    b=driver.find_elements_by_class_name('st')
    bx=b[0].text+b[1].text+b[2].text
    for word in words:
        X2=X2+bx.count(word)
    print(X2)


    op3=split_string(option[2])


    driver.get("https://www.google.com/search?q="+qes+"\""+option[2]+"\"")
    c=driver.find_elements_by_class_name('st')
    cx=c[0].text+c[1].text+c[2].text
    for word in words:
        X3=X3+cx.count(word)
    print(X3) 


def OCR():
    question=""
    option=list()
    im = Imagegrab.grab(bbox=(272,528,727,655))
    question = pytesseract.image_to_string(im, lang = 'vie')
    question = question.replace('\n',' ')+" "
    question = question.replace('º','o')
    question = question.replace('ï','i')
    question = question.replace('\"',' ')+" "
    neg=question.count("KHÔNG")+question.count("CHƯA")
    question = question.replace("KHÔNG", " ")
    question = question.replace("CHƯA"," ")

    im = Imagegrab.grab(bbox=(281,655,693,852))
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 
    
    c=pytesseract.image_to_string(im, lang = 'vie')    
    c = c.replace('º','o')
    c = c.replace('ï','i')
    c = c.replace("\n\n","\n")


    i=0
    o1=""
    o2=""
    o3=""
    while (c[i]!='\n'):
        o1=o1+c[i]
        i=i+1
    i=i+1

    while (c[i]!='\n'):
        o2=o2+c[i]
        i=i+1
    i=i+1

    while (i<len(c)):
        o3=o3+c[i]
        i=i+1
    i=i+1

    option.append(o1)
    option.append(o2)
    option.append(o3)
    return question,option,neg

def SearchNEG(qes,option):

    start_time = time.time()

    X1=0
    X2=0
    X3=0


    driver.get("https://www.google.com/search?q="+qes+"\""+option[0]+"\"")
    a=driver.find_element_by_id('resultStats')
    x=a.text
    print("1. ", option[0],"\t", re.search('g (.+?) k',x).group(1))

    driver.get("https://www.google.com/search?q="+qes+"\""+option[1]+"\"")
    a=driver.find_element_by_id('resultStats')
    x=a.text
    print("2. ", option[1],"\t", re.search('g (.+?) k',x).group(1))
    driver.get("https://www.google.com/search?q="+qes+"\""+option[2]+"\"")
    a=driver.find_element_by_id('resultStats')
    x=a.text
    print("3. ", option[2],"\t", re.search('g (.+?) k',x).group(1))    
    print(" ")
    print(" ")
    elapsed_time = time.time() - start_time



    print("Hoàn thành trong : ",elapsed_time," giây.")


def SearchEND(qes,optionX):

    start_time = time.time()
    print("----------------------------------------")

    X1=0
    X2=0
    X3=0
    driver.get("https://www.google.com/search?q="+qes)
    a=driver.find_element_by_id('search')
    ba=a.text.lower()
    X1=ba.count(optionX[0].lower())
    X2=ba.count(optionX[1].lower())
    X3=ba.count(optionX[2].lower())

    if ((X1>X2)&(X1>X3)):
        print("[    Dap an: 11111   ]\n")
    if ((X2>X1)&(X2>X3)):
        print("[    Dap an: 22222   ]\n")
    if ((X3>X1)&(X3>X2)):
        print("[    Dap an: 33333   ]\n")
    driver.get("https://www.google.com/search?q="+qes+"\""+optionX[0]+"\"")
    a=driver.find_element_by_class_name('st')
    b=driver.find_element_by_id('resultStats')
    print(b.text)
    x=re.sub('<em>\w+</em>',' ',a.get_attribute('innerHTML'))
    x=re.sub('</em>.*?<em>',' ',x)
    x=re.sub('</em>.*',' ',x)
    x=re.sub('.*<em>',' ',x)
    print(x)
    driver.get("https://www.google.com/search?q="+qes+"\""+optionX[1]+"\"")
    a=driver.find_element_by_class_name('st')
    print("----------------------------------------")
    x=re.sub('<em>\w+</em>',' ',a.get_attribute('innerHTML'))
    x=re.sub('</em>.*?<em>',' ',x)
    b=driver.find_element_by_id('resultStats')
    print(b.text)
    x=re.sub('</em>.*',' ',x)
    x=re.sub('.*<em>',' ',x)
    print(x)
    driver.get("https://www.google.com/search?q="+qes+"\""+optionX[2]+"\"")
    a=driver.find_element_by_class_name('st')
    print("----------------------------------------")
    b=driver.find_element_by_id('resultStats')
    print(b.text)
    x=re.sub('<em>\w+</em>',' ',a.get_attribute('innerHTML'))
    x=re.sub('</em>.*?<em>',' ',x)
    x=re.sub('</em>.*',' ',x)
    x=re.sub('.*<em>',' ',x)
    print(x)
    

    print(" ")  
    print(" ")
    print(" ")

    elapsed_time = time.time() - start_time

    print(elapsed_time)

def SearchWG(qes,optionX):

    print("----------------------------------------")

    W1=0
    WD1=0
    W2=0
    WD2=0
    W3=0
    WD3=0
    G1=0
    GD1=0
    G2=0
    GD2=0
    G3=0
    GD3=0
    op1=split_string(optionX[0])
    op2=split_string(optionX[1])
    op3=split_string(optionX[2])

    driver.get("https://www.google.com/search?q="+qes)
    GET="x=document.getElementById(\"search\"); y=x.textContent.toLowerCase(); z=y.match(/"+optionX[0].lower()+"/g); if (z==null) {return (0)} else {return z.length}"
    G1=driver.execute_script(GET)
    for word in op1:
        GET="x=document.getElementById(\"search\"); y=x.textContent.toLowerCase(); z=y.match(/"+word.lower()+"/g); if (z==null) {return (0)} else {return z.length}"
        GD1+=driver.execute_script(GET)    

    GET="x=document.getElementById(\"search\"); y=x.textContent.toLowerCase(); z=y.match(/"+optionX[1].lower()+"/g); if (z==null) {return (0)} else {return z.length}"
    G2=driver.execute_script(GET)
    for word in op2:
        GET="x=document.getElementById(\"search\"); y=x.textContent.toLowerCase(); z=y.match(/"+word.lower()+"/g); if (z==null) {return (0)} else {return z.length}"
        GD2+=driver.execute_script(GET)   
    GET="x=document.getElementById(\"search\"); y=x.textContent.toLowerCase(); z=y.match(/"+optionX[2].lower()+"/g); if (z==null) {return (0)} else {return z.length}"
    G3=driver.execute_script(GET)
    for word in op3:
        GET="x=document.getElementById(\"search\"); y=x.textContent.toLowerCase(); z=y.match(/"+word.lower()+"/g); if (z==null) {return (0)} else {return z.length}"
        GD3+=driver.execute_script(GET)   

    driver.get("https://www.google.com/search?q="+qes+"site:vi.wikipedia.org")
    GET="x=document.getElementById(\"search\"); y=x.textContent.toLowerCase(); z=y.match(/"+optionX[0].lower()+"/g); if (z==null) {return (0)} else {return z.length}"
    W1=driver.execute_script(GET)
    for word in op1:
        GET="x=document.getElementById(\"search\"); y=x.textContent.toLowerCase(); z=y.match(/"+word.lower()+"/g); if (z==null) {return (0)} else {return z.length}"
        WD1+=driver.execute_script(GET)    

    GET="x=document.getElementById(\"search\"); y=x.textContent.toLowerCase(); z=y.match(/"+optionX[1].lower()+"/g); if (z==null) {return (0)} else {return z.length}"
    W2=driver.execute_script(GET)
    for word in op2:
        GET="x=document.getElementById(\"search\"); y=x.textContent.toLowerCase(); z=y.match(/"+word.lower()+"/g); if (z==null) {return (0)} else {return z.length}"
        WD2+=driver.execute_script(GET)  

    GET="x=document.getElementById(\"search\"); y=x.textContent.toLowerCase(); z=y.match(/"+optionX[2].lower()+"/g); if (z==null) {return (0)} else {return z.length}"
    W3=driver.execute_script(GET)
    for word in op3:
        GET="x=document.getElementById(\"search\"); y=x.textContent.toLowerCase(); z=y.match(/"+word.lower()+"/g); if (z==null) {return (0)} else {return z.length}"
        WD3+=driver.execute_script(GET)  
    X1=W1+G1+GD1/100+WD1/100
    X2=W2+G2+GD2/100+WD2/100
    X3=W3+G3+GD3/100+WD3/100
    print(" ")
    print(Fore.YELLOW+qes)
    f1=0
    f2=0
    f3=0
    if ((X1>X2)&(X1>X3)):
        print(Back.CYAN+"[    Dap an: 11111   ]\n")
        f1=1
    if ((X2>X1)&(X2>X3)):
        print(Back.CYAN+"[    Dap an: 22222   ]\n")
        f2=1
    if ((X3>X1)&(X3>X2)):
        print(Back.CYAN+"[    Dap an: 33333   ]\n")
        f3=1
    print(Back.CYAN*f1+"1. ",Back.CYAN*f1+optionX[0],"\t",W1+WD1/100,"\t",G1+GD1/100)
    print(Back.CYAN*f2+"2. ",Back.CYAN*f2+optionX[1],"\t",W2+WD2/100,"\t",G2+GD2/100)
    print(Back.CYAN*f3+"3. ",Back.CYAN*f3+optionX[2],"\t",W3+WD2/100,"\t",G3+GD3/100)



def solve():
    os.system('cls')
    start_time = time.time()
    question,option,neg=OCR()
    if (neg>0):
        SearchNEG(question,option)
    else:
        SearchWG(question,option)
    elapsed_time = time.time() - start_time

    print("\nHoàn thành trong ",elapsed_time, " giây.")

if __name__ == "__main__":
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 
    driver = webdriver.Firefox()
    driver.get("http://www.google.com")
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    s = requests.session()

    while(1):
        keypressed = input()
        if keypressed == 's':
            solve()
        else: break
    driver.close()
