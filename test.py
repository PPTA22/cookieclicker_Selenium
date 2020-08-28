
from time import sleep
import  time
from pip._vendor.distro import distro_release_info
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import selenium

PATH = 'C:/Program Files (x86)/WebDriver/msedgedriver.exe'

driver = webdriver.Edge(PATH)
print(driver.title)
url = 'https://www.cathaypacificcargo.com/ManageYourShipment/TrackYourShipment/tabid/108/SingleAWBNo/160-18927112/language/en-US/Default.aspx'

driver.get(url)
# driver.get("https://orteil.dashnet.org/cookieclicker/")
print(driver.title)

try:
    WebDriverWait(driver,15).until(
        # EC.presence_of_all_elements_located((By.ID, 'prefsButton'))
        EC.presence_of_element_located((By.ID, 'tntTab2'))
    )

    print('[o] hey u found it')
    # print(driver.page_source)

except Exception as e:
    print('[X] err')
    print(e)
    sleep(5)
    driver.quit()
driver.find_element_by_class_name('tntTabBtn2.tntTabBtn').click()
booking_status_tab = driver.find_element_by_id('tntTab2')
css_class = booking_status_tab.find_elements_by_class_name('tntField.tntW150')
for c in css_class:
    print(c.text)
    print()



print()

print()
# search = driver.find_element_by_name("q")   #this is to find the search tag
# search.send_keys("test", Keys.ARROW_DOWN)  #this is the text wnat to search
# search.send_keys(Keys.RETURN)   #this means enter
#
# try:
#     main = WebDriverWait(driver,10).until(
#         EC.presence_of_all_elements_located((By.ID, "search"))
#     )
#
#     print('[o] hey u found it')
#     # print(driver.page_source)
# except:
#     print('[X] err')
#
# sleep(1)
#
# # results = driver.find_element_by_class_name('g')
# results = driver.find_elements_by_class_name('g')
# # print(results.text)
# print(len(results))
# sleep(5)
# driver.quit()

# driver.find_element()