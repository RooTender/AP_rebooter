from selenium import webdriver
PATH = r"C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.google.pl/")
driver.close()