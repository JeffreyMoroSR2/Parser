import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome('chromedriver', options=options)

driver.get("https://auto.ria.com/uk/legkovie/?page=1")
a = driver.find_elements(By.CLASS_NAME, 'content')

with open('log.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for i in a:
        Car_Arr = []
        Price_Arr = []
        Mileage_Arr = []

        Car_Name = i.find_element(By.CLASS_NAME, 'head-ticket').text
        Car_Arr.append('Модель - ' + str(Car_Name))
        # writer.writerow(Car_Arr)

        Price_UAH = i.find_element(By.CLASS_NAME, 'i-block').text
        Price_Arr.append('Ціна - ' + str(Price_UAH))
        # writer.writerow(Price_Arr)

        Mileage = i.find_element(By.CLASS_NAME, 'item-char.js-race').text
        Mileage_Arr.append('Пробіг - ' + str(Mileage))
        # writer.writerow(Mileage_Arr)

        row_print = [Car_Arr[0], Price_Arr[0], Mileage_Arr[0]]
        writer.writerow(row_print)

        print('Car - ' + Car_Name + '\n\tCar mileage - ' + Mileage + '\n\tPrice - ' + Price_UAH)
        print('=======================')

a = driver.find_element(By.XPATH, '/html/body/div[7]/section[1]/div[2]/div/div/div[26]/nav/span[8]/a')
print(a.text)
