import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


def bonadio():
    bonadio = {}

    for i in range(1,3):
        prod = {}
        
        url = f'https://apiariosbonadio.commercesuite.com.br/loja/busca.php?loja=863360&palavra_busca=.&pg={i}'

        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'html.parser')

        produtos = soup.find_all('div', class_='product-name')
        precos = soup.find_all('div', class_='prices')

        for i in range(len(produtos)):
            bonadio[produtos[i].get_text()] = f'R$ {precos[i].get_text()}'

    return bonadio


def nutri():
    NetNutri = {}

    chorme_op = Options()
    chorme_op.add_argument("--headless") #Esse deixa a página em segundo plano no pc
    chorme_op.add_argument("--disable-gpu")

    #configura qual navegador vai ser usado
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chorme_op)

    url = "https://www.netnutri.com.br/produtos/?mpage=15"
    driver.get(url)

    #tenta achar o botão pela página fisica e clica nele
    try:
        espera = WebDriverWait(driver, 60) #espera a página carregar
        cookie_btn = espera.until(EC.element_to_be_clickable((By.CLASS_NAME, "js-notification-close"))) #Procura o botão do cookie pelo html
        cookie_btn.click()
        print('Cookie aceito')
    except Exception as e:
        print('Botão não encontrado', e)

    #Esperar os produtos aparecerem
    try:
        espera.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.js-item-name")))
        print('Produtos encontrados')
    except Exception as e:
        print('Nenhum produto encontrado a tempo:', e)

    seletor_prod = "div.js-item-name"
    prods = driver.find_elements(By.CSS_SELECTOR, seletor_prod)

    seletor_preco = "span.js-price-display"
    precos = driver.find_elements(By.CSS_SELECTOR, seletor_preco)

    if prods and precos:
        for produto, preco in zip(prods, precos):
            prodN = produto.text.strip()
            prodP = preco.text.strip()
            NetNutri[prodN] = prodP

    return NetNutri


produtos = {'Apiarios Bonadio:':bonadio(), 'NetNutri: ': nutri()}

for i in produtos.keys():
    print(i)
    for y in produtos[i].items():
        print(f'{y[0]}: {y[1]}')


nomeArq = 'crawler.pdf'
titulo_doc = 'crawler'
titulo = 'Resultados do crawler'

pdf = canvas.Canvas(nomeArq)
pdf.setTitle(titulo_doc)
pdfmetrics.registerFont(
    TTFont('fonte', 'Arial.ttf')
)

texto = pdf.beginText(10, 680)
texto.setFont('fonte', 18)

for i in produtos.keys():
    texto.textLine(f'\n{i}')
    for y in produtos[i].items():
        texto.textLine(f'{y[0]}: {y[1]}')

pdf.drawText(texto)

pdf.save()