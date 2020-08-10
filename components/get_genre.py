from selenium import webdriver
import time


def getGenre(fname):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        driver = webdriver.Chrome(chrome_options=options)

        driver.get('https://www.google.com/')
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(fname)
        driver.find_element_by_xpath(
            '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()
        time.sleep(2)
        scrap = driver.find_element_by_xpath(
            '//*[@id="wp-tabs-container"]/div[1]/div[3]/div/div/div/div[2]/div/span').text
        time.sleep(1)
        driver.quit()
        genre = scrap.split()[2].split('/')[0]
        return genre
    except Exception as e:
        print(e)
        return None
