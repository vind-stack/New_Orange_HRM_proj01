from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\VINAYAK L DIXIT\\chromedriver.exe")
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_ele = driver.find_element(By.XPATH,"//body/div[2]/div[2]/span[1]")
max_ele = driver.find_element(By.XPATH,"//body/div[2]/div[2]/span[2]")

print("Location of the Sliders before moving....")
print(min_ele.location)
print(max_ele.location)

act = ActionChains(driver)
act.drag_and_drop_by_offset(min_ele, 50, 0) .perform()                 #its sliding in x axis so y always zero
act.drag_and_drop_by_offset(max_ele, -39, 0).perform()

print("***************")

print("Location of the Sliders after moving....")
print(min_ele.location)
print(max_ele.location)


