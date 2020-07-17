from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver=webdriver.Chrome(executable_path='C:\\Users\Zein Zebib\Documents\Python Stuff\Online Automation\chromedriver.exe')

bla= int(input('1 for CHi\n'
'2 for Z\n'
'3 for t\n'))

if bla==1:
    a=input('Enter a or a/2: ')
    n=input('Enter n-1: ')
    driver.get('https://homepage.divms.uiowa.edu/~mbognar/applets/chisq.html')
    sleep(5)
    driver.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[1]/td[2]/input').send_keys(str(n))
    driver.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[2]/td[4]/input').send_keys(str(a)+Keys.ENTER)

elif bla==2:
    a=float(input('Enter a or a/2: '))
    driver.get('https://homepage.divms.uiowa.edu/~mbognar/applets/normal.html')
    sleep(5)
    driver.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[2]/td[4]/input').send_keys(str(a)+Keys.ENTER)

else:
    a=input('Enter a or a/2: ')
    n=input('Enter n-1: ')
    driver.get('https://homepage.divms.uiowa.edu/~mbognar/applets/t.html')
    sleep(5)
    driver.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[1]/td[2]/input').send_keys(n)
    driver.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[2]/td[4]/input').send_keys(str(a)+Keys.ENTER)

