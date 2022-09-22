from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\VINAYAK L DIXIT\\chromedriver.exe")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source_ele = driver.find_element(By.XPATH,"//div[@id='box3']")
distn_ele = driver.find_element(By.XPATH,"//div[@id='box103']")

act = ActionChains(driver)
act.drag_and_drop(source_ele, distn_ele).perform()


