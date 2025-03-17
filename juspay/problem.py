from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# run the driver 
driver = webdriver.Chrome()

# getting the url 
def get_url(url):
    driver.get(url)
# xpath for login 
def login(path):
    driver.find_element(By.XPATH,path).click()
# update the phone number 
def type_phone_number(path, text):
    driver.find_element(By.CLASS_NAME, path).send_keys(text)
# click operation function 
def click(path):
    driver.find_element(By.XPATH,path).click()
# product finding function 
def product(path):
    driver.find_element(By.XPATH,path)



# giving the url into the driver 
get_url("https://www.flipkart.com/")
time.sleep(2)

# perform login procedure
login('//a[@title="Login"]')
time.sleep(2)
# login with phone number 
type_phone_number("r4vIwl", "9051260845")
click('//button[contains(text(), "Request OTP")]')
time.sleep(20)
# product taking
search_box = driver.find_element(By.NAME, "q")  
product_name = "Apple iPhone 14 (Blue, 128 GB)"
search_box.send_keys(product_name)
search_box.send_keys(Keys.RETURN)
#  wait for 3sec
time.sleep(3)

# getting product details
try:
    first_product = driver.find_element(By.XPATH, "//div[contains(@class,'KzDlHZ')]")  # Product name
    price = driver.find_element(By.XPATH, "//div[contains(@class,'Nx9bqj')]")  # Price
    link = driver.find_element(By.XPATH, "//a[contains(@class,'CGtC98')]").get_attribute("href")  # Product link

    print("Product Name:", first_product.text)
    print("Price:", price.text)
    print("Link:", link)
except:
    print("Product not found or Flipkart's structure has changed.")


def place_order(card_number_xpath, card_number, month_xpath, year_xpath, month, year,cvv_path,cvv_number):
    # input card number.
    card_number_input = driver.find_element(By.XPATH, card_number_xpath) 
    card_number_input.send_keys(card_number) 

    # select month 
    month_select_element = driver.find_element(By.XPATH, month_xpath)
    month_select = Select(month_select_element)
    month_select.select_by_value(month) 

    # select year
    year_select_element = driver.find_element(By.XPATH, year_xpath)
    year_select = Select(year_select_element)
    year_select.select_by_value(year)

    cvv=driver.find_element(By.XPATH, cvv_path)
    cvv.send_keys(cvv_number)

time.sleep(10)

# getting the link from the scrapped product 
driver.get(link)
# perform buy now operation 
click('//button[@type="button"]')
time.sleep(2)
# perform deliver here
click('//button[text()="Deliver Here"]')
time.sleep(2)
# click continue process 
driver.find_element(By.CLASS_NAME, "QqFHMw").click()
time.sleep(5)
# popup for accept and continue operation 
click('//button[text()="Accept & Continue"]')
time.sleep(2)
# select the payment option
click('//label[@for="CREDIT"]')
time.sleep(1)
# input for payment details 
place_order(
    card_number_xpath='//input[@name="cardNumber"]',
    card_number='4111111111111111',
    month_xpath='//select[@name="month"]',
    year_xpath='//select[@name="year"]',
    month='05',
    year='41',
    cvv_path='//input[@name="cvv"]',
    cvv_number='1234'
)

driver.quit()