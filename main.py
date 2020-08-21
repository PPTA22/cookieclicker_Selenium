import sys
from time import sleep
import time
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MOUSE_CLICK_COOKIE_TIMES = 40
MOUSE_CLICK_GAP_IN_SECOND = 4


def click_golden_cookie():
    #can also in the main.js of the webpage
    #find the `me.time++` change to `me.time = me.time+500`
    #so the golden cookie will always spawn
    try:
        driver.find_element_by_class_name('shimmer').click()
        print('[o] clicked Golden cookie')
    except Exception as e:
        pass


PATH = 'C:/Program Files (x86)/WebDriver/msedgedriver.exe'

driver = webdriver.Edge(PATH)
print(driver.title)

driver.get("https://orteil.dashnet.org/cookieclicker/")
print(driver.title)

try:
    main = WebDriverWait(driver, 20).until(
        # EC.presence_of_all_elements_located((By.ID, 'prefsButton'))
        EC.presence_of_all_elements_located((By.ID, 'bigCookie'))
    )
    sleep(4)

    print('[o] hey u found it')
    # print(driver.page_source)

except:
    print('[X] err')
    sleep(5)
    driver.quit()
    print('[!] Bye')
    sys.exit()

driver.find_element_by_id('prefsButton').click()
saving_path = 'C:/Users/tim10n/Downloads/CookieBakery.txt'
driver.find_element_by_id('FileLoadInput').send_keys(saving_path)

# get all the items ava to buy
while True:
    try:
        items = driver.find_elements_by_class_name('product.unlocked.enabled')

        click_golden_cookie()
        for i in reversed(items[10:]):
            i.click()
            print('clicked : ' + i.find_element_by_class_name('title').text +
                  '[' + i.find_element_by_class_name('title.owned').text + ']')
        # sleep(10)
        for i in range(MOUSE_CLICK_COOKIE_TIMES):
            driver.find_element(By.ID, 'bigCookie').click()
        sleep(MOUSE_CLICK_GAP_IN_SECOND)
    except ElementClickInterceptedException as e:
        #print(e)
        print('[!] the big cookie may be overlaped by golden cookie')
    except Exception as e:
        print(e)
        # export to save bt
        # if (driver.)
        t=driver.find_element_by_id('prefsButton')
        if 'selected' not in t.get_attribute('class'):
            driver.find_element_by_id('prefsButton').click()
        print('clicked Options bt')

        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[18]/div[2]/div[4]/div[3]/div[3]/a[1]').click()
        # saving record
        text_record = driver.find_element_by_xpath('/html/body/div/div[2]/div[11]/div/div[1]/div[2]/textarea').text

        with open('C:/Users/tim10n/Downloads/CookieBakery2.txt', 'w') as f:
            f.write(text_record)
        print('[!] saved record')
