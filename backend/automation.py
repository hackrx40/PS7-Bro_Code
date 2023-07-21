import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions

download_dir = r'C:\Users\HP\Desktop\HackRx'
options = ChromeOptions()
options.add_experimental_option('prefs', {
    'download.default_directory': download_dir,
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
})

driver = webdriver.Chrome(options=options)

driver.get('https://phantombuster.com/login')


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Email'][@type='email']")))
email_input = driver.find_element(By.XPATH, "//input[@placeholder='Email'][@type='email']")

email_input.send_keys("suyashsngh250@gmail.com")


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password'][@type='password']")))
password_input = driver.find_element(By.XPATH, "//input[@placeholder='Password'][@type='password']")

password_input.send_keys("SuyashSingh@1004")

password_input.send_keys(Keys.RETURN)


driver.get("https://phantombuster.com/8715273940022424/phantoms/2650057009673459/console")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[analyticsid='agentConsoleMoreButton']")))
more_button = driver.find_element(By.CSS_SELECTOR, "[analyticsid='agentConsoleMoreButton']")
more_button.click()


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[analyticsid='agentConsoleDownloadSectionDownloadBtn']")))
more_button = driver.find_element(By.CSS_SELECTOR, "[analyticsid='agentConsoleDownloadSectionDownloadBtn']")
more_button.click()

time.sleep(3)

