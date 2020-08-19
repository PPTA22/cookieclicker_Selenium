from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = 'C:/Program Files (x86)/WebDriver/msedgedriver.exe'

driver = webdriver.Edge(PATH)

driver.get("https://google.com")
print(driver.title)


search = driver.find_element_by_name("q")   #this is to find the search tag
search.send_keys("test")  #this is the text wnat to search
search.send_keys(Keys.RETURN)   #this means enter

try:
    main = WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.ID, "search"))
    )

    print('[o] hey u found it')
    # print(driver.page_source)
except:
    print('[X] err')

sleep(1)

results = driver.find_element_by_class_name('g')
print(len(results))
# sleep(5)
# driver.quit()
