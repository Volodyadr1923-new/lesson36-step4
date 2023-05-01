from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def stepik_a(browser,link):
    try:
        browser.get(link)

        # нажатие кнопки "Войти" с проверкой возможности нажатия кнопки в течение 10 сек
        enter = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "navbar__auth_login")))
        # enter = browser.find_element(By.ID, "ember33")
        enter.click()

        # Заполнение полей в открывшемся pop-up-блоке с проверкой возможности заполнения в течение 10 сек
        # browser.implicitly_wait(5)
        email = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.ID, "id_login_email")))
        # email = browser.find_element(By.ID, "id_login_email")
        email.send_keys('Enter your email address')

        password = browser.find_element(By.ID, "id_login_password")
        password.send_keys('Enter your password')

        # Нажимаем кнопку "Войти"
        enter = browser.find_element(By.CLASS_NAME, "sign-form__btn")
        enter.click()

        # Проверка присутствия в браузере pop-up-блока
        email = WebDriverWait(browser, 20).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "modal-dialog-block")))

        # # Нажатие кнопки "Сброс"
        # send = browser.find_element(By.CLASS_NAME, "again-btn")
        # send.click()
        #
        # alert = browser.switch_to.alert
        # alert.accept()

        # Ответ
        answer = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.TAG_NAME, "textarea")))

        # password = send_keys('Enter your password')
        answer.send_keys(f'{math.log(int(time.time()))}')

        # Нажатие кнопки "Отправить"
        send = browser.find_element(By.CLASS_NAME, "submit-submission")
        send.click()

        browser.implicitly_wait(5)
        check = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
        check = check.text
        if check != "Correct!":
            print(check)

        assert check == "Correct!", "Not correct feedback!"

    finally:
        pass
