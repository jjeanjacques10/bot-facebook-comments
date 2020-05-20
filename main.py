# Author: Jean Jacques Barros
# Github: https://github.com/jjeanjacques10/

# Simple assignment
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time, json

driver = Chrome()

with Chrome() as driver:
    with open(f'config.json', 'r', encoding='utf-8') as f:
        content = json.loads(f.read())
    f.close()

    email = content['email']
    password = content['password']
    link = content['link']
    qtd_message = content['qtd_message']
    message = content['message']

    driver.get("https://www.facebook.com/")
    time.sleep(4)

    textbox_email = driver.find_element_by_xpath('//*[@id="email"]')
    textbox_email.send_keys(email)
    textbox_password = driver.find_element_by_xpath('//*[@id="pass"]')
    textbox_password.send_keys(password)

    botao = driver.find_element_by_xpath('//*[@id="loginbutton"]')
    botao.click()
    time.sleep(4)
    driver.get(link)
    time.sleep(4)

    texto = driver.find_element_by_xpath(
        '//*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[4]/div/div[2]/div[5]/div[2]/div/div/div/div/form/div[2]/div/div[2]/div')

    for i in range(qtd_message):
        texto.send_keys(message, Keys.ENTER)
        time.sleep(2)

    time.sleep(100)