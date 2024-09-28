# type: ignore
from  pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
ROOT_FOLDER = Path(__file__).parent
PATH_DRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'
# print(PATH_DRIVER_EXEC)

def make_chrome_browser(*options: str) -> webdriver.Chrome:

    chrome_options = webdriver.ChromeOptions()
    if options is not None:
        for option in options:            
            chrome_options.add_argument(option)

    chrome_service = Service(executable_path=str(PATH_DRIVER_EXEC))
    chrome_browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )    
    return chrome_browser

if __name__ == '__main__':
    # exemplo 
    options = ('--disable-gpu', '--no-sandbox')
    browser = make_chrome_browser(*options) 
    browser.get('https://www.google.com.br/')
    # espere para encontrar o input
    search_input = WebDriverWait(browser,10).until(
        EC.presence_of_element_located(
           ( By.NAME,'q')
        )
    )
    search_input.send_keys('hello world')
    search_input.send_keys(Keys.ENTER)
    results = browser.find_element(By.ID,'search')
    print('buscando links')
    links = results.find_elements(By.TAG_NAME,'a')
    print('#'* 100)
    print(links[0])
    print('#'* 100)
    print('clicando')
    print('#'* 100)
    links[0].click()
    print('#'* 100)
    sleep(10)
