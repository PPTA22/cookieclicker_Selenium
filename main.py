import sys
from time import sleep
import time
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MOUSE_CLICK_COOKIE_TIMES = 30
MOUSE_CLICK_GAP_IN_SECOND = 6
START_FROM_BUYING = 10  #10=Portal, 11=Time Machine
GOLDEN_COOKIE_TIME_COUNTER = 0
PATH = 'C:/Program Files (x86)/WebDriver/msedgedriver.exe'


def click_golden_cookie():
    global GOLDEN_COOKIE_TIME_COUNTER
    '''
    can also in the main.js of the webpage
    find the `me.time++` change to `me.time = me.time+200`
    so the golden cookie will always spawn
    '''
    try:
        gd_coks = driver.find_elements_by_class_name('shimmer')
        if  gd_coks:
            for c in gd_coks:
                c.click()
            # driver.find_element_by_class_name('shimmer').click()

            # print('[o] clicked Golden cookie: ',  int(time.time() - GOLDEN_COOKIE_TIME_COUNTER), 's')
        GOLDEN_COOKIE_TIME_COUNTER = time.time()

    except NoSuchElementException:
        #   if not found the gd cok, will catch here
        pass
    except StaleElementReferenceException:
        print('[X] StaleElementReferenceException is occured')
        print('\tbut not sure wt this means')
        #   Message: stale element reference: element is not attached to the page document

#   start of the program
try:
    driver = webdriver.Edge(PATH)
    print(driver.title)

    driver.get("https://orteil.dashnet.org/cookieclicker/")
    print('[title]: driver.title')
    main = WebDriverWait(driver, 20).until(
        # EC.presence_of_all_elements_located((By.ID, 'prefsButton'))
        EC.presence_of_all_elements_located((By.ID, 'bigCookie'))
    )
    sleep(5)

    print('[!] Page animation shd fully loaded')
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

        # for i in reversed(items[START_FROM_BUYING:]):
        #     i.click()
        #     print('clicked : ' + i.find_element_by_class_name('title').text +
        #           '[' + i.find_element_by_class_name('title.owned').text + ']')

        # if not in `info` page, click longer n sleep less
        '''
        if 'selected' in driver.find_element_by_id('logButton').get_attribute('class'):
            for i in range(MOUSE_CLICK_COOKIE_TIMES ):
                driver.find_element(By.ID, 'bigCookie').click()
            sleep(MOUSE_CLICK_GAP_IN_SECOND)
        else:
            for i in range(MOUSE_CLICK_COOKIE_TIMES+100 ):
                driver.find_element(By.ID, 'bigCookie').click()
            sleep(MOUSE_CLICK_GAP_IN_SECOND-3)
        '''
        sleep(0.1)

    except ElementClickInterceptedException:
        # print(e)
        print('[!] the big cookie may be overlapped by golden cookie')
        continue

    except Exception as e:
        print(e)
        # export to save bt
        # if (driver.)
        t=driver.find_element_by_id('prefsButton')
        if 'selected' not in t.get_attribute('class'):
            driver.find_element_by_id('prefsButton').click()
        print('clicked Options bt')

        #click the show saving textbox
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[18]/div[2]/div[4]/div[3]/div[3]/a[1]').click()
        # get the saving record
        text_record = driver.find_element_by_xpath('/html/body/div/div[2]/div[11]/div/div[1]/div[2]/textarea').text

        #save the record to the file
        with open('C:/Users/tim10n/Downloads/CookieBakery2.txt', 'w') as f:
            f.write(text_record)
        print('[!] saved record')
