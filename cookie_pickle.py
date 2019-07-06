from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle

driver = webdriver.Firefox()
driver.get("https://www.google.com/search?q=hi")
#khúc này import cookies vào rồi quay lại gõ bất kỳ
s=input()
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
