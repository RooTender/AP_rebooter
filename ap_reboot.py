from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def getElement(elementName, by, timeout = 10):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, elementName))
        )
    except:
        print("Timeout {0} seconds passed!".format(timeout))
        return 0



PATH = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://192.168.0.1/")

loginInput = getElement("loginPassword", By.ID)
loginInput.send_keys("82458393")
loginInput.send_keys(Keys.RETURN)

driver.quit()