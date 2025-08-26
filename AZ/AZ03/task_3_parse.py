from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By
import csv

from selenium.webdriver.support.wait import WebDriverWait

headless = webdriver.ChromeOptions()
headless.add_argument('--headless')

driver = webdriver.Chrome(options=headless)
url = 'https://www.divan.ru/category/divany-i-kresla'
driver.get(url)
wait = WebDriverWait(driver, 15)
divans = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div._Ud0k')))
parsed_data = []

try:
    for divan in divans:
        title = divan.find_element(By.CSS_SELECTOR,'span[itemprop="name"]').text
        price = divan.find_element(By.CSS_SELECTOR, 'span[class="ui-LD-ZU KIkOH"]').text

        parsed_data.append({
            'Наименование товара':title,
            'Цена':price
        })

except Exception as e:
    print(f'Ошибка при парсинге товара:{e}')

driver.quit()

try:
    with open('divans.csv', 'w', encoding='utf-8', newline='')as f:
        writer = csv.DictWriter(f, fieldnames=parsed_data[0].keys())
        writer.writeheader()
        writer.writerows(parsed_data)
        print(f'Данные успешно сохранены в файл {f}')
        f.close()
except Exception as e:
    print(f'Ошибка сохранения файла {f}')





