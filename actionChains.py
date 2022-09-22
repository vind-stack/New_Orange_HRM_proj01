from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\VINAYAK L DIXIT\\chromedriver.exe")
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

button = driver.find_element(By.XPATH,"//span[contains(text(),'right click me')]")
print(button.location)
act = ActionChains(driver)
act.context_click(button).perform()
driver.close()