from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.remote.remote_connection import RemoteConnection 
import time 
remote_hub_url='http://127.0.0.1:4444/wd/hub' 
options = Options() 
#options.headless = True 
driver =webdriver.Remote(remote_hub_url,options=options) 
driver.get("https://en.wikipedia.org/wiki/Reddit")
time.sleep(10)
