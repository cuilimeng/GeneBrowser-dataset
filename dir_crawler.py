from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


def init_driver():
    # initiate the driver:
    driver = webdriver.Chrome()

    # set a default wait time for the browser [5 seconds here]:
    driver.wait = WebDriverWait(driver, 5)

    return driver


def close_driver(driver):
    driver.close()

    return


def test(t):

    driver = init_driver()
    driver.get(t)
    replies = []

    wait = WebDriverWait(driver, 10)

    try:
        # extract all the tweets:
        tweets = driver.find_elements(By.CSS_SELECTOR, "div[class='Gene__Body-sc-iolqfe-7 bcUdtS'] > ul > li > a")

        for thread in tweets:
            reply = {
                'url': 'https://3billion.io/gene/',
                'title': None
            }
            reply['url'] += thread.text+'/'
            reply['title'] = thread.text
            replies.append(reply)
    except NoSuchElementException:
        print("NoSuchElementException")

    # elem = driver.find_element_by_css_selector("div.js-tweet-text-container")
    # tweet_text = elem.text
    close_driver(driver)
    return replies


for i in range(ord('A'), ord('Z')+1):
    articles = test('https://3billion.io/gene/?browse='+chr(i))
    df = pd.DataFrame(data=articles, columns=('url', 'title'))
    df.to_csv('data/dir/dir_gene_browser_'+chr(i)+'.csv', index=True, encoding="utf-8-sig")