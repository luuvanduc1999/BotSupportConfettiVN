import os
import json
from bs4 import BeautifulSoup
import argparse
import sys
import wx
import sys
import re
import time
from telethon import TelegramClient
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
import requests
import pickle
from colorama import Fore, Back, Style
from colorama import init
import time
from halo import Halo


init(autoreset=True)
driver = webdriver.Chrome()
driver.get("http://www.google.com")


def get_env(name, message, cast=str):
    if name in os.environ:
        return os.environ[name]
    while True:
        value = input(message)
        try:
            return cast(value)
        except ValueError as e:
            print(e, file=sys.stderr)
            time.sleep(1)

session = os.environ.get('TG_SESSION', 'printer')
api_id = 892934
api_hash = 'a1d95763f40384bfeee1c848f846888e'
proxy = None  # https://github.com/Anorov/PySocks

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

def SearchNEGG(qes,optionX):

    

    A1=0
    A2=0
    A3=0
    G1=0
    G2=0
    G3=0
    LH=max(len(optionX[0]),len(optionX[1]),len(optionX[2]))
    SPACE="               "
    op1=split_string(optionX[0])
    op2=split_string(optionX[1])
    op3=split_string(optionX[2])
    driver.get("https://www.google.com/search?q="+qes)
    GET="x=document.getElementById(\"search\");y=x.textContent.toLowerCase();z=y.match(/"+optionX[0].lower()+"/g);KQ=((z==null)?0:z.length);return(KQ);"
    G1=driver.execute_script(GET)

    GET="x=document.getElementById(\"search\");y=x.textContent.toLowerCase();z=y.match(/"+optionX[1].lower()+"/g);KQ=((z==null)?0:z.length);return(KQ);"
    G2=driver.execute_script(GET)

    GET="x=document.getElementById(\"search\");y=x.textContent.toLowerCase();z=y.match(/"+optionX[2].lower()+"/g);KQ=((z==null)?0:z.length);return(KQ);"
    G3=driver.execute_script(GET)


    driver.get("https://www.google.com/search?q="+qes+' '+optionX[0])
    a=driver.find_element_by_id('resultStats')
    x=a.text
    A1=int(''.join(filter(str.isdigit, x[0:x.index('(')])))

    driver.get("https://www.google.com/search?q="+qes+' '+optionX[1])
    a=driver.find_element_by_id('resultStats')
    x=a.text
    A2=int(''.join(filter(str.isdigit, x[0:x.index('(')])))

    driver.get("https://www.google.com/search?q="+qes+' '+optionX[2])
    a=driver.find_element_by_id('resultStats')
    x=a.text
    A3=int(''.join(filter(str.isdigit, x[0:x.index('(')])))

    X1=G1
    X2=G2
    X3=G3
    f1=0
    f2=0
    f3=0
    if ((X1<X2)&(X1<X3)):
        print(Back.CYAN+"[    Dap an: 11111   ]")
        f1=1
    elif ((X2<X1)&(X2<X3)):
        print(Back.CYAN+"[    Dap an: 22222   ]")
        f2=1
    elif ((X3<X1)&(X3<X2)):
        print(Back.CYAN+"[    Dap an: 33333   ]")
        f3=1
    else:
        print(Back.RED+"[ KHONG TIM DUOC DAP AN ]")
        if (X1>0):
            print(Back.RED+"[ KHONG PHAI 1 ]")
        else:
            print()
        if (X2>0):
            print(Back.RED+"[ KHONG PHAI 2 ]")
        else:
            print()
        if (X3>0):
            print(Back.RED+"[ KHONG PHAI 3 ]")
        else:
            print()

        if ((A1<A2)&(A1<A3)):
            f1=1
        elif ((A2<A1)&(A2<A3)):
            f2=1
        elif ((A3<A1)&(A3<A2)):
            f3=1
    print()
    print(Back.MAGENTA*f1+"1. "+optionX[0]+SPACE[1:LH-len(optionX[0])+1],"\t",G1,"\t",A1)
    print(Back.MAGENTA*f2+"2. "+optionX[1]+SPACE[1:LH-len(optionX[1])+1],"\t",G2,"\t",A2)
    print(Back.MAGENTA*f3+"3. "+optionX[2]+SPACE[1:LH-len(optionX[2])+1],"\t",G3,"\t",A3)

'''y=document.getElementsByTagName("body")[0].innerText.toLowerCase(); X=y[0].match("GTK3");'''

'''
def SearchNEG(qes,option):


    X1=0
    X2=0
    X3=0


    driver.get("https://www.google.com/search?q="+qes+"\""+option[0]+"\"")
    a=driver.find_element_by_id('resultStats')
    x=a.text
    X1=int(''.join(filter(str.isdigit, x)))
    print("1. ", option[0],"\t", re.search('g (.+?) k',x).group(1))

    driver.get("https://www.google.com/search?q="+qes+"\""+option[1]+"\"")
    a=driver.find_element_by_id('resultStats')
    x=a.text
    X2=int(''.join(filter(str.isdigit, x)))
    print("2. ", option[1],"\t", re.search('g (.+?) k',x).group(1))
    driver.get("https://www.google.com/search?q="+qes+"\""+option[2]+"\"")
    a=driver.find_element_by_id('resultStats')
    x=a.text
    X3=int(''.join(filter(str.isdigit, x)))
    print("3. ", option[2],"\t", re.search('g (.+?) k',x).group(1))    
    print(" ")
    if ((X1<X2)&(X1<X3)):
        print(Back.RED+"[    Dap an: 11111   ]\n")
    elif ((X2<X1)&(X2<X3)):
        print(Back.GREEN+"[    Dap an: 22222   ]\n")
    elif ((X3<X1)&(X3<X2)):
        print(Back.BLUE+"[    Dap an: 33333   ]\n")

    print(" ")

def SearchWG(qes,optionX, HO):

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
    LH=max(len(optionX[0]),len(optionX[1]),len(optionX[2]))
    SPACE="               "
    op1=split_string(optionX[0])
    op2=split_string(optionX[1])
    op3=split_string(optionX[2])
    driver.get("https://www.google.com/search?q="+qes)
    GET="x=document.getElementsByClassName(\"rc\");y=x[0].textContent.toLowerCase();z=y.match(/"+optionX[0].lower()+"/g);KQ1=(z==null)?0:z.length;x=document.getElementById(\"search\");y=x.textContent.toLowerCase();z=y.match(/"+optionX[0].lower()+"/g);KQ=((z==null)?0:z.length);return([KQ,KQ1]);"
    
    GW=driver.execute_script(GET)
    G1=GW[0]
    W1=GW[1]
    for word in op1:
        GET="x=document.getElementById(\"search\"); y=x.textContent.toLowerCase(); z=y.match(/"+word.lower()+"/g); if (z==null) {return (0)} else {return z.length}"
        GD1+=driver.execute_script(GET)    

    GET="x=document.getElementsByClassName(\"rc\");y=x[0].textContent.toLowerCase();z=y.match(/"+optionX[1].lower()+"/g);KQ2=(z==null)?0:z.length;x=document.getElementById(\"search\");y=x.textContent.toLowerCase();z=y.match(/"+optionX[1].lower()+"/g);KQ=((z==null)?0:z.length);return([KQ,KQ2]);"
    GW2=driver.execute_script(GET)
    G2=GW2[0]
    W2=GW2[1]
    for word in op2:
        GET="x=document.getElementById(\"search\"); y=x.textContent.toLowerCase(); z=y.match(/"+word.lower()+"/g); if (z==null) {return (0)} else {return z.length}"
        GD2+=driver.execute_script(GET)   
    GET="x=document.getElementsByClassName(\"rc\");y=x[0].textContent.toLowerCase();z=y.match(/"+optionX[2].lower()+"/g);KQ3=(z==null)?0:z.length;x=document.getElementById(\"search\");y=x.textContent.toLowerCase();z=y.match(/"+optionX[2].lower()+"/g);KQ=((z==null)?0:z.length);return([KQ,KQ3]);"
    GW3=driver.execute_script(GET)
    G3=GW3[0]
    W3=GW3[1]
    for word in op3:
        GET="x=document.getElementById(\"search\"); y=x.textContent.toLowerCase(); z=y.match(/"+word.lower()+"/g); if (z==null) {return (0)} else {return z.length}"
        GD3+=driver.execute_script(GET)   


    X1=G1+GD1/100+W1*10
    X2=G2+GD2/100+W2*10
    X3=G3+GD3/100+W3*10
    print(" ")
    print(Fore.YELLOW+qes)
    f1=0
    f2=0
    f3=0
    print()
    if ((X1>X2)&(X1>X3)):
        if (X1>=1):
            print(Back.CYAN+"[    Dap an: 11111   ]")
        else:
            print(Back.RED+"[ KHONG TIM DUOC DAP AN ]")
        f1=1
    if ((X2>X1)&(X2>X3)):
        if (X2>=1):
            print(Back.CYAN+"[    Dap an: 22222   ]")
        else:
            print(Back.RED+"[ KHONG TIM DUOC DAP AN ]")
        f2=1
    if ((X3>X1)&(X3>X2)):
        if (X3>=1):
            print(Back.CYAN+"[    Dap an: 33333   ]")
        else:
            print(Back.RED+"[ KHONG TIM DUOC DAP AN ]")
        f3=1
    print()
    print(Back.MAGENTA*f1+"1. "+optionX[0]+SPACE[1:LH-len(optionX[0])+1],"\t",W1,"\t",G1+GD1/100)
    print(Back.MAGENTA*f2+"2. "+optionX[1]+SPACE[1:LH-len(optionX[1])+1],"\t",W2,"\t",G2+GD2/100)
    print(Back.MAGENTA*f3+"3. "+optionX[2]+SPACE[1:LH-len(optionX[2])+1],"\t",W3,"\t",G3+GD3/100)
'''
def SearchWG(qes,optionX):
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
    LH=max(len(optionX[0]),len(optionX[1]),len(optionX[2]))
    SPACE="               "
    op1=split_string(optionX[0])
    op2=split_string(optionX[1])
    op3=split_string(optionX[2])
    driver.get("https://www.google.com/search?q="+qes)
    GET="x=document.getElementsByClassName(\"rc\");y=x[0].textContent.toLowerCase();z=y.match(/"+optionX[0].lower()+"/g);KQ1=(z==null)?0:z.length;x=document.getElementById(\"search\");y=x.textContent.toLowerCase();z=y.match(/"+optionX[0].lower()+"/g);KQ=((z==null)?0:z.length);return([KQ,KQ1]);"
    
    GW=driver.execute_script(GET)
    G1=GW[0]
    W1=GW[1]
    for word in op1:
        GET="x=document.getElementById(\"search\"); y=x.textContent.toLowerCase(); z=y.match(/"+word.lower()+"/g); if (z==null) {return (0)} else {return z.length}"
        GD1+=driver.execute_script(GET)    

    GET="x=document.getElementsByClassName(\"rc\");y=x[0].textContent.toLowerCase();z=y.match(/"+optionX[1].lower()+"/g);KQ2=(z==null)?0:z.length;x=document.getElementById(\"search\");y=x.textContent.toLowerCase();z=y.match(/"+optionX[1].lower()+"/g);KQ=((z==null)?0:z.length);return([KQ,KQ2]);"
    GW2=driver.execute_script(GET)
    G2=GW2[0]
    W2=GW2[1]
    for word in op2:
        GET="x=document.getElementById(\"search\"); y=x.textContent.toLowerCase(); z=y.match(/"+word.lower()+"/g); if (z==null) {return (0)} else {return z.length}"
        GD2+=driver.execute_script(GET)   
    GET="x=document.getElementsByClassName(\"rc\");y=x[0].textContent.toLowerCase();z=y.match(/"+optionX[2].lower()+"/g);KQ3=(z==null)?0:z.length;x=document.getElementById(\"search\");y=x.textContent.toLowerCase();z=y.match(/"+optionX[2].lower()+"/g);KQ=((z==null)?0:z.length);return([KQ,KQ3]);"
    GW3=driver.execute_script(GET)
    G3=GW3[0]
    W3=GW3[1]
    for word in op3:
        GET="x=document.getElementById(\"search\"); y=x.textContent.toLowerCase(); z=y.match(/"+word.lower()+"/g); if (z==null) {return (0)} else {return z.length}"
        GD3+=driver.execute_script(GET)   
    
    driver.get("https://www.google.com/search?q="+qes.replace("\"","")+" ("+" OR ".join(optionX)+")")

    GET="x=document.getElementsByClassName(\"rc\");y=x[0].textContent.toLowerCase();z=y.match(/"+optionX[0].lower()+"/g);KQ1=(z==null)?0:z.length;x=document.getElementById(\"search\"); return(KQ1);"
    WD1=driver.execute_script(GET)
    GET="x=document.getElementsByClassName(\"rc\");y=x[0].textContent.toLowerCase();z=y.match(/"+optionX[1].lower()+"/g);KQ1=(z==null)?0:z.length;x=document.getElementById(\"search\"); return(KQ1);"
    WD2=driver.execute_script(GET)
    GET="x=document.getElementsByClassName(\"rc\");y=x[0].textContent.toLowerCase();z=y.match(/"+optionX[2].lower()+"/g);KQ1=(z==null)?0:z.length;x=document.getElementById(\"search\"); return(KQ1);"
    WD3=driver.execute_script(GET)


    X1=G1+GD1/1000+W1*10+WD1*2
    X2=G2+GD2/1000+W2*10+WD2*2
    X3=G3+GD3/1000+W3*10+WD3*2

    f1=0
    f2=0
    f3=0
    print()

    if ((X1>X2)&(X1>X3)):
        if (X1>=1):
            print(Back.CYAN+"[    Dap an: 11111   ]")
        else:
            print(Back.RED+"[ KHONG TIM DUOC DAP AN ]")
        f1=1
    if ((X2>X1)&(X2>X3)):
        if (X2>=1):
            print(Back.CYAN+"[    Dap an: 22222   ]")
        else:
            print(Back.RED+"[ KHONG TIM DUOC DAP AN ]")
        f2=1
    if ((X3>X1)&(X3>X2)):
        if (X3>=1):
            print(Back.CYAN+"[    Dap an: 33333   ]")
        else:
            print(Back.RED+"[ KHONG TIM DUOC DAP AN ]")
        f3=1
    print()
    print(Back.MAGENTA*f1+"1. "+optionX[0]+SPACE[1:LH-len(optionX[0])+1],"\t",W1+WD1/10,"\t",G1+GD1/1000)
    print(Back.MAGENTA*f2+"2. "+optionX[1]+SPACE[1:LH-len(optionX[1])+1],"\t",W2+WD2/10,"\t",G2+GD2/1000)
    print(Back.MAGENTA*f3+"3. "+optionX[2]+SPACE[1:LH-len(optionX[2])+1],"\t",W3+WD3/10,"\t",G3+GD3/1000)


def Solve(str):
    if ((str[0]=='#') & ((str[6]=='B') | (str[5]=='B'))):
        os.system('cls')
        start_time = time.time()
        str=str.replace("Câu hỏi: ","")
        X=str.splitlines()
        print(X[0])
        qes=X[3]
        neg=qes.count("KHÔNG")+qes.count("CHƯA")   
        qes=qes.replace("KHÔNG","")
        qes=qes.replace("Điền vào chỗ trống ","")
        qes=qes.replace("Điền các chữ cái còn thiếu để ", " ")
        qes=qes.replace("CHƯA","")
        O1=X[5][3:X[5].index('(')-1]
        O2=X[6][3:X[6].index('(')-1]
        O3=X[7][3:X[7].index('(')-1]
        option=list()
        option.append(O1)
        option.append(O2)
        option.append(O3)
        print("----------------------------------------")
        print(Fore.YELLOW+qes)
        print(" ")
        if (neg>0):
            SearchNEGG(qes,option)
        else:
            SearchWG(qes,option)
        elapsed_time = time.time() - start_time
        print("\nHoàn thành trong ",elapsed_time, " giây.\n")
    else:
        print(Fore.CYAN+str,"\n")
    
async def handler(update):
    Solve(update.message.message)


with TelegramClient(session, api_id, api_hash, proxy=proxy) as client:
    client.add_event_handler(handler)
    print('(Press Ctrl+C to stop this)')
    client.run_until_disconnected()
