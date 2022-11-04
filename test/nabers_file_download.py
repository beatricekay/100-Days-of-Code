from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import os

# function to wait for file to download before closing chrome
def download_wait():
    seconds = 0
    dl_wait = True # True - we continue to wait for the file to download
    while dl_wait and seconds < 300: # dl_wait must be FALSE and seconds > 300 to break the loop
        time.sleep(5) # wait for 5 seconds
        dl_wait = False
        for fname in os.listdir("/Users/beatricekaystacs/Downloads"):
            if fname.endswith('.crdownload'): # if file name ends with '.crdownload', the file is still downloading
                dl_wait = True
        seconds += 1 # assume this process of checking for file takes approx. 1 second
    return seconds

# load web chrome driver to open website
# need to download chromedriver
options = webdriver.ChromeOptions()
service = Service('./chromedriver')
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.nabers.gov.au/ratings/find-a-current-rating")

# wait for website content to load
print("Waiting for website to load...")
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="node-2301"]/div/div[3]/div/div/a')))
print("Website loaded!")

# get the link element
link_element = driver.find_element(By.XPATH, '//*[@id="node-2301"]/div/div[3]/div/div/a')

# get the link of the element
link = link_element.get_attribute('href')

# click the link
driver.get(link)
print("Waiting for file to download...")
download_wait()
print("File download complete!")
driver.close()