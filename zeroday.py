from selenium import webdriver
import time, optparse
from banner import Banner
"""
# Script to download Alura courses

Enjoy =)
"""
Banner()

parse = optparse.OptionParser()
parse.add_option('-u','--url', help='Comand base URL', dest='url_base', metavar='https://alura.com.br/.../')
parse.add_option('-i','--initial', help='Number of first video', dest='ini', metavar='1337', type="int")
parse.add_option('-f','--final', help='Number of final video', dest='final', metavar='1356', type="int")

(options, args) = parse.parse_args()

chrome = webdriver.Chrome(executable_path='C:\\Users\\Gustavo\\Downloads\\PDFs Peakflow\\alura-down-master\\alura-down-master\\chromedriver.exe')
chrome.get('https://cursos.alura.com.br/loginForm')

user = chrome.find_element_by_xpath('//*[@id="login-email"]')
password = chrome.find_element_by_xpath('//*[@id="password"]')
user.clear()
user.send_keys('your-email')
password.clear() 
password.send_keys('your-password')
chrome.find_element_by_class_name('btn-login').click()

for i in range(options.ini, options.final+1):
    url_final = f'{options.url_base}{i}'
    chrome.get(url_final)
   
    video_sec = chrome.find_element_by_class_name('video-container')
    time.sleep(2)
    chrome.get(video_sec.find_element_by_id('video-player-frame_html5_api').get_attribute('src'))
    print(f'[ + ] SUCESS | {url_final}')
  
print('-----------DONE-----------')







