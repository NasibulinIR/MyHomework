from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()
url = 'https://www.divan.ru/category/svet'
driver.get(url)
time.sleep(3)

goods = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k' )
parsed_data =[]

try:
    for good in goods:
        title = good.find_element(By.CSS_SELECTOR, 'div.lsooF span').text
        price = good.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
        url = good.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')

        parsed_data.append({
            'Наименование товара': title,
            'Цена':price,
            'Ссылка на товар':url
        })
except Exception as e:
    print(f'Ошибка при парсинге товара:{e}')

driver.quit()

try:
    with open('lamps.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=parsed_data[0].keys())
        writer.writeheader()
        writer.writerows(parsed_data)
        print(f'Данные успешно сохранены в файл {f}')
except Exception as e:
    print(f'Ошибка сохранения файла {f}')