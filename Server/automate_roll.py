from util import Util
import requests
from selenium import webdriver
import time
import datetime


lista_emails = ["fczb_btc0@outlook.es",
                "carloszaragozabeato15@gmail.com",
                "carloszaragozabeato@gmail.com",]











# # '//*[@id="free_play_form_button"]'
def algoritmo_roll(driver, index):
    util = Util(driver=driver)
    util.driver.get("https://freebitco.in/")

    server_condition = True
    
    time.sleep(5)
    
    try:
        notifications = "/html/body/div[24]/div[1]/div[2]/div/div[1]"
        util.obtenerXpath(notifications).click()
    except Exception as ex:
        print("ERROR NOTIFICACION")
        print(ex)
    
    
    xpath_comprobacion_captcha = "/html/body/div[2]/div/div/div[7]/div[2]/div/div[1]/div[1]"
    no_captcha = False
    try:
        util.obtenerXpath(xPath=xpath_comprobacion_captcha)
        print("ENTR")
        time.sleep(30)
    except Exception as ex:
        no_captcha = True
    
    
    
    
    try:
        if no_captcha:
            selector = "html.js.no-touch.svg.inlinesvg.svgclippaths.no-ie8compat body div#top_margin_dep_withdraw_buttons.row div.large-12.large-centered.small-12.small-centered.columns div#main_content.large-9.small-12.small-centered.large-centered.new_border_shadow.columns div#free_play_tab.page_tabs p input#free_play_form_button.free_play_element.new_button_style.profile_page_button_style"
            util.obtener_uno_CssSelector(selector).click()
    except Exception as ex:
        print(ex)
        server_condition = False

    if server_condition:
        xpath_puntos = "/html/body/div[1]/div/nav/section/ul/li[20]/span"
        hora = datetime.datetime.now()
        xpath_puntos_obtenidos = "/html/body/div[2]/div/div/div[7]/div[3]/div/span[1]"
        
        puntos_obtenidos = util.obtenerXpath(xPath=xpath_puntos_obtenidos).text
        email = lista_emails[index]
        saldo_actual = util.obtenerXpath(xPath=xpath_puntos).text
        
        url = f"http://127.0.0.1:8000/update?saldo_actual={saldo_actual}&recogida={puntos_obtenidos}&email={email}"
        response = requests.get(url, json=data)
    
    util.driver.close()
    
    
    
for index in range(3): 
    options = webdriver.FirefoxOptions()
    ruta = f"/home/carlos/snap/firefox/common/.mozilla/firefox/{index+1}"
    options.profile = ruta 
    driver = webdriver.Firefox(options=options)
    algoritmo_roll(driver, index)



