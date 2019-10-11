from selenium import webdriver
import time

"""
# Script para efetuar downloads da plataforma do ALURA
E-MAIL-AQUI == seu e-mail de acesso
senha-aqui == sua senha de acesso

 Enjoy =)
"""

url_base = input('Digite a url base: ')
inicio = int(input('Digite o primeiro ID: '))
fim = int(input('Digite o segundo ID: '))

chrome = webdriver.Chrome(executable_path='/Users/gvb/Documents/Scrappy/chromedriver')
chrome.get('https://cursos.alura.com.br/loginForm')


usuario = chrome.find_element_by_name('username')
senha = chrome.find_element_by_name('password')
usuario.clear()
usuario.send_keys('e-mail-aqui')
senha.clear() 
senha.send_keys('senha-aqui')
chrome.find_element_by_class_name('btn-login').click()

for i in range(inicio, fim+1):
    url_final = f'{url_base}{i}'
    chrome.get(url_final)
   
    video_sec = chrome.find_element_by_class_name('video-container')
    time.sleep(2)
    chrome.get(video_sec.find_element_by_id('video-player-frame_html5_api').get_attribute('src'))
    print(f'[ + ] SUCESS | {url_final}')
  
print('-----------DONE-----------')







