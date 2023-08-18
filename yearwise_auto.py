# # to add :
# # save to csv
# # host the project
# # api
# # make a website

# #import statements
# import time
# import pandas as pd
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# from selenium import webdriver

# # from webdriver_manager.chrome import ChromeDriverManager


# print("Enter Petitioner or respondant name : ")
# name_tag = input()
# print("Enter the year of filing")
# year = input()

# year_from = "01-01-"+year
# year_to = "31-12-"+year

# #setting the chromedriver to headless mode
# driver = webdriver.Chrome('/Users/littlebuddha/Documents/Internship/Selenium-Project/chromedriver')
# chrome_options = Options()
# chrome_options.add_argument("--headless")

# web = webdriver.Chrome(options=chrome_options)
# web.get('http://karnatakajudiciary.kar.nic.in/search_partyname.php')

# time.sleep(2)

# # Input of data in the necessary fields

# name_field = web.find_element("xpath",'//*[@id="caseDetails"]/div/div/div/div[1]/div[3]/div[2]/div/input')
# name_field.send_keys(name_tag)

# fromyear_field = web.find_element("xpath",'//*[@id="from_date"]')
# fromyear_field.send_keys(year_from)

# toyear_field = web.find_element("xpath",'//*[@id="to_date"]')
# toyear_field.send_keys(year_to)

# get_details = web.find_element("xpath",'//*[@id="caseDetails"]/div/div/div/div[1]/div[4]/div[4]/input')
# get_details.click()

# # printing details 
 
# time.sleep(2)

# soup = BeautifulSoup(web.page_source, 'lxml')

# tables = soup.find_all('table')
# dfs = pd.read_html(str(tables))

# print(f'Total tables: {len(dfs)}')
# print(dfs[0])


# to add :
# save to csv
# host the project
# api
# make a website

#import statements
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium import webdriver

# from webdriver_manager.chrome import ChromeDriverManager


def details(name_tag,year):

    year_from = "01-01-"+year
    year_to = "31-12-"+year
    #setting the chromedriver to headless mode
    driver = webdriver.Chrome('/Users/littlebuddha/Documents/Internship/Selenium-Project/chromedriver')
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    web = webdriver.Chrome(options=chrome_options)
    web.get('http://karnatakajudiciary.kar.nic.in/search_partyname.php')

    time.sleep(2)
    # Input of data in the necessary fields

    name_field = web.find_element("xpath",'//*[@id="caseDetails"]/div/div/div/div[1]/div[3]/div[2]/div/input')
    name_field.send_keys(name_tag)

    fromyear_field = web.find_element("xpath",'//*[@id="from_date"]')
    fromyear_field.send_keys(year_from)

    toyear_field = web.find_element("xpath",'//*[@id="to_date"]')
    toyear_field.send_keys(year_to)

    get_details = web.find_element("xpath",'//*[@id="caseDetails"]/div/div/div/div[1]/div[4]/div[4]/input')
    get_details.click()
    # printing details 
 
    time.sleep(2)

    soup = BeautifulSoup(web.page_source, 'lxml')

    tables = soup.find_all('table')
    dfs = pd.read_html(str(tables))

    print(f'Total tables: {len(dfs)}')
    print(dfs[0])



# print("Enter Petitioner or respondant name : ")
name_tag = "tata"
# print("Enter the year of filing")
year = "2020"
details(name_tag,year)