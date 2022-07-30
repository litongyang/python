from os import times
from bs4 import BeautifulSoup
# import urllib.error
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver
import time




options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://food.jd.com")
js = '''
            let height = 0
    let interval = setInterval(() => {
        window.scrollTo({
            top: height,
            behavior: "smooth"
        });
        height += 500
    }, 500);
    setTimeout(() => {
        clearInterval(interval)
    }, 7000);
'''
driver.execute_script(js)
time.sleep(8)
bs = BeautifulSoup(driver.page_source, "html.parser")
driver.close()
print bs.text
# list = bs.select(".goods-item__title")
# for i in range(len(list)):
#     list[i] = list[i].get_text()
#     print("%s\n" % list[i])


