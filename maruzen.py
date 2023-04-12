from selenium import webdriver
import time
from docx import Document
from msedge.selenium_tools import Edge, EdgeOptions
import urllib.request
from docx.shared import Cm


url = 'https://elib.maruzen.co.jp/elib/html/Viewer/Id/3000072739?17'

path = r"C:\Users\asd-0\Downloads\edgedriver_win64\msedgedriver.exe"
driver = Edge(path)


driver.get(url)
time.sleep(1)

driver.implicitly_wait(5)
login = driver.find_element_by_class_name("guestlogingakuninbtn")
login.click()

driver.implicitly_wait(5)
driver.find_element_by_id("keytext").send_keys("金沢大学")
time.sleep(0.5)
driver.find_element_by_name("Select").click()

driver.implicitly_wait(5)
form_input_password = driver.find_element_by_id("password")
form_input_id = driver.find_element_by_id("kuid")

form_input_id.send_keys("yjr03120")
form_input_password.send_keys("6g1aU!Uh")

driver.find_element_by_name("_eventId_proceed").click()

driver.implicitly_wait(5)
driver.find_element_by_class_name("btl").click()

time.sleep(0.1)

driver.switch_to.window(driver.window_handles[1])
doc = Document()
i=0
page = int(driver.find_element_by_class_name("allpageno").text)

while(i<page):
    try:
     driver.implicitly_wait(5)
     img = driver.find_element_by_id("pagepict").get_attribute("src")
     urllib.request.urlretrieve(img,"screen.png")
     time.sleep(5)
     driver.execute_script("{document.querySelector('.nextbt').click();}")
     doc.add_picture('./screen.png', Cm(18), Cm(25))
     i=i+1

    except:
        print("error")
        pass



title = driver.find_element_by_class_name("booktitle").text
doc.save('{}.docx'.format(title))

driver.quit()

