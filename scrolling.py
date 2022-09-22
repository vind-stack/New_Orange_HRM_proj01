import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\VINAYAK L DIXIT\\chromedriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

#SCROLL DOWN THE PAGE BY PIXEL
driver.execute_script("window.scrollBy(0, 1000)", "")            #pixel value(random value) 3000

value = driver.execute_script("return window.pageYOffset;")           #just for the reference
print("Number of pixels moved: ", value)

#SCROLL DOWN THE PAGE, TILL THE ELEMENT IS VISIBLE

flag = driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
driver.execute_script("arguments[0].scrollIntoView();", flag)

value = driver.execute_script("return window.pageYOffset;")           #just for the reference
print("Number of pixels moved: ", value)

#SCROLLING DOWN  TILL THE END OF THE PAGE
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

value = driver.execute_script("return window.pageYOffset;")           #just for the reference
print("Number of pixels moved: ", value)

time.sleep(5)
#SCROLLING TO THE TOP AGAIN (REVERSE)
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")

value = driver.execute_script("return window.pageYOffset;")           #just for the reference
print("Number of pixels moved: ", value)

