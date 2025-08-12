import time
import random
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



browser = webdriver.Chrome()
browser.get('https://ru.wikipedia.org/')

#  Цикл поиска статьи с повторными попытками при вводе запроса которого нет на Вики
while True:
    user_input = input('Введите ваш запрос (или "exit" для выхода): ')
    if user_input == 'exit':
        browser.quit()

    try:
        search_box = browser.find_element(By.ID, 'searchInput')
        search_box.clear()
        search_box.send_keys(user_input + Keys.RETURN)
        time.sleep(3)  # Ждем загрузки результатов поиска

        # Попытка перейти на точную статью
        try:
            browser.find_element(By.LINK_TEXT, user_input).click()
            time.sleep(3) # Ждем загрузки страницы
            break
        except NoSuchElementException:
            print(f"Статья '{user_input}' не найдена. Попробуйте другой запрос.\n")

    except Exception as e:
        print(f"Ошибка поиска: {e}")

# Основной цикл навигации
while True:
    try:
        page_title = browser.find_element(By.CSS_SELECTOR, 'span.mw-page-title-main').text
        paragraphs = browser.find_elements(By.TAG_NAME, 'p')
        print(f"\nТекущая статья: {page_title}")
        choice = input('\n1. Читать статью\n2. Случайная ссылка\n3. Выход\nВыбор: ')

        if choice == '3' or choice == 'exit':
            break

        elif choice == '1':
            for paragraph in paragraphs:
                if not paragraph.text.strip():
                    continue
                print("\n" + paragraph.text)
                # Цикл контролирующий корректный ввод
                while True:
                    action = input('\n[Enter] Далее | [1] - Случайная ссылка | [2] - Меню: ')
                    if action == '':
                        break

                    elif action == '1':
                        links = paragraph.find_elements(By.XPATH,
                                                        './/a[starts-with(@href, "/wiki/") and not(contains(@class, "new"))]')
                        if links:
                            random.choice(links).click()
                            time.sleep(2)
                            break
                        print("Нет доступных ссылок в этом абзаце.")
                    elif action == '2':
                        break
                    else:
                        print('Некорректный ввод. Вводите только указанные команды')
                        continue
                if action == '2':
                    break



        elif choice == '2':
            links = browser.find_elements(By.XPATH,'//a[starts-with(@href, "/wiki/")'
                                                   ' and not(contains(@class, "new"))]')
            if links:
                random.choice(links).click()
                time.sleep(3) # Загрука страницы
            else:
                print("На странице нет доступных ссылок.")
        else:
            print('\nНекорректный ввод. Вводите только указанные команды')

    except NoSuchElementException:
        print("Ошибка: Структура страницы изменилась")
        break





