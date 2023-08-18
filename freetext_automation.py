#import statements
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium import webdriver
import pytesseract

print("Enter Petitioner or respondant name : ")
name_tag = input()

#setting the chromedriver to headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

web = webdriver.Chrome(options=chrome_options)
web.get('https://judgments.ecourts.gov.in/pdfsearch/?p=pdf_search/index&state_code=29~3&dist_code=1')
time.sleep(2)

# name_field = web.find_element("xpath",'//*[@id="caseDetails"]/div/div/div/div[1]/div[3]/div[2]/div/input')
name_field = web.find_element("xpath",'//*[@id="pet_res"]')
name_field.send_keys(name_tag)

captcha_img_loc = web.find_element("xpath",'//*[@id="captcha_image"]').get_attribute("src")



img = get_captcha(captcha_img_loc)
img.save('captcha_original.png')
gray = img.convert('L')
gray.save('captcha_gray.png')
bw = gray.point(lambda x: 0 if x < 1 else 255, '1')
bw.save('captcha_thresholded.png')

