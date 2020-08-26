from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

passwordFilePath = "./routerPass.txt"

def checkIfPasswordExist():
    pathToPassFile = Path(passwordFilePath)
    
    if not pathToPassFile.exists():
        print("Please type password to router login page: ", end="")
        password = input()

        pathToPassFile.touch()
        del pathToPassFile

        passwordFile = open(passwordFilePath, "w")
        passwordFile.write(password)
        passwordFile.close()
    else:
        print("Password file found!")

def getElement(elementName, by, timeout = 10):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, elementName))
        )
    except:
        print("Timeout {0} seconds passed!".format(timeout))
        return None

checkIfPasswordExist()

driver = webdriver.Chrome(r"C:\Program Files (x86)\chromedriver.exe")
driver.get("http://192.168.0.1/")

loginInput = getElement("loginPassword", By.ID)
if loginInput is None:
    driver.refresh()
    loginInput = getElement("loginPassword", By.ID)

passwordFile = open(passwordFilePath, "r")

loginInput.send_keys(passwordFile.read())
loginInput.send_keys(Keys.RETURN)
del loginInput

passwordFile.close()

elements = ("c_mu25", "c_mu27", "c_rr14", "c_st28")
for element in elements:
    elementToClick = getElement(element, By.ID)
    elementToClick.click()

print("Success!")

driver.quit()