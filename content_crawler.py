from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from csv import DictReader


def init_driver():
    # initiate the driver:
    driver = webdriver.Chrome()

    # set a default wait time for the browser [5 seconds here]:
    driver.wait = WebDriverWait(driver, 5)

    return driver


def close_driver(driver):
    driver.close()

    return


def test(t, title):

    driver = init_driver()
    driver.get(t)

    wait = WebDriverWait(driver, 10)

    reply = {
        'url': t,
        'title': title,
        'description': None,
        'variant counts': None,
        'patient phenotypes': None
    }
    try:
        # extract all the tweets:
        thread = driver.find_element(By.CSS_SELECTOR, "div[class='GeneDetail__Description-sc-18p75an-3 lmhyHD']")

        reply['description'] = thread.text
    except NoSuchElementException:
        print("NoSuchElementException")

    try:
        # extract all the tweets:
        thread = driver.find_element(By.CSS_SELECTOR, "div[class='VariantCount__VariantCountWrapper-sc-aqneav-0 ckfioK']")

        reply['variant counts'] = thread.text
    except NoSuchElementException:
        print("NoSuchElementException")

    try:
        # extract all the tweets:
        thread = driver.find_element(By.CSS_SELECTOR, "div[class='PatientPhenotypes__PatientPhenotypesWrapper-sc-1gpfknt-0 kjiOwj']")

        reply['patient phenotypes'] = thread.text
    except NoSuchElementException:
        print("NoSuchElementException")

    close_driver(driver)
    return reply


for i in range(ord('A'), ord('Z')+1):
    articles = []
    # open file in read mode
    print(chr(i))
    with open('data/dir/dir_gene_browser_'+chr(i)+'.csv', 'r') as read_obj:
        # pass the file object to DictReader() to get the DictReader object
        csv_dict_reader = DictReader(read_obj)
        # iterate over each line as a ordered dictionary
        for row in csv_dict_reader:
            # row variable is a dictionary that represents a row in csv
            articles += [test(row['url'], row['title'])]
            print(row['\ufeff'])

    df = pd.DataFrame(data=articles, columns=('url', 'title', 'description', 'variant counts', 'patient phenotypes'))
    df.to_csv('data/webpage/gene_browser_'+chr(i)+'.csv', index=True, encoding="utf-8-sig")