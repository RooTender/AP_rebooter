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
        return None

PATH = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://192.168.0.1/")

loginInput = getElement("loginPassword", By.ID)
if loginInput is None:
    driver.refresh()
    loginInput = getElement("loginPassword", By.ID)

loginInput.send_keys("82458393")
loginInput.send_keys(Keys.RETURN)
del loginInput

elementToClick = getElement("c_mu25", By.ID)
elementToClick.click()
elementToClick = getElement("c_mu27", By.ID)
elementToClick.click()
elementToClick = getElement("c_rr14", By.ID)
elementToClick.click()
elementToClick = getElement("c_st28", By.ID)
elementToClick.click()

print("Success!")

driver.quit()