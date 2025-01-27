
import pandas as pd
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

price_list = []
product_list = []
# Iniciando Instancia Chrome
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Acessar Site
# link = https://lista.mercadolivre.com.br/_CustId_1075392339_NoIndex_True?segmentation_enabled=false
sleep(2)
url = input('Cole o link da lista do Mercado Livre: ')
driver.get(url=url)


def goto_next_page():
    next_bt = driver.find_element(
        By.CLASS_NAME, 'andes-pagination__button--next')
    _class = next_bt.get_attribute('class')
    if _class == 'andes-pagination__button andes-pagination__button--next':
        next_page_link = next_bt.find_element(
            By.CLASS_NAME, 'andes-pagination__link').get_attribute('href')
        driver.get(url=next_page_link)
        get_data()
    elif _class == 'andes-pagination__button andes-pagination__button--next andes-pagination__button--disabled':
        print('ALL PAGES GET')
        make_dataframe()


def get_data():
    global driver
    global price_list
    global product_list
    # Encontrar dados por elementos na página
    e_list = driver.find_elements(By.CLASS_NAME, 'poly-component__title')
    for title in range(len(e_list)):
        price = driver.find_elements(
            By.CLASS_NAME, 'andes-money-amount--cents-superscript')[title]
        amount = price.find_element(
            By.CLASS_NAME, 'andes-money-amount__fraction').text
        try:
            cents = price.find_elements(
                By.CLASS_NAME, 'andes-money-amount__cents')[title].text
        except:
            cents = '00'

        price_list.append(str(f'R${amount},{cents}'))

    p_list = [title.text for title in e_list]
    for item in p_list:
        product_list.append(item.replace(',', ' -').replace('.', ''))
    goto_next_page()


def make_dataframe():
    print('Fazendo DATAFRAME')
    global product_list
    global price_list
    print(f'products = {len(product_list)} | prices = {len(price_list)}')
    data = {'PRODUTO': product_list, 'PREÇO': price_list}
    dataframe = pd.DataFrame(data)
    print(dataframe.to_string())
    dataframe.to_csv(r'./output/product_data_mercadolivre.csv', sep='\t',
                     encoding='utf-8', header='true')


get_data()
