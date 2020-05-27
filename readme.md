<p align="center">
  <h3 align="center">ALURA DOWN</h3>
  <p align="center">Download Alura courses (requires account)</p>

  <p align="center">
    <a href="https://t.me/whoisgvb">
      <img src="https://img.shields.io/badge/Telegram-@whoisgvb-blue.svg">
    </a>
  </p>
</p>
<hr>

### Features
```
+ Download videos of courses only with the URL
```
### Install requirements
```
pip3 install --user -r requirements.txt
```

###  Complete Usage

```
Usage: zeroday.py [OPTIONS]

Options:
-u or --url       Base URL to download the videos courses
-i or --initial   number of first video
-f or --final     numer of final video

Download webDriver (I used chrome)
+ https://chromedriver.chromium.org/
  set in variable "chrome" the complete PATH
  example: 
  chrome = webdriver.Chrome(executable_path='/Users/gvb/Documents/Scrappy/chromedriver')
  * For Windows use two bars ('C:\\ ...')

+ replace "your-email" and "your-password" on zeroday.py
  > user.send_keys('your-email')
  > password.send_keys('your-password')

```

### Examples

```
python3 zeroday.py -u https://www.alura.com.br/curso-online-introducao-a-programacao-com-ruby-e-jogos-3/task/ -i 1337 -f 1356
                      * where '1337' is the first ID of first video and '1356' the ID of final video
                      * dont forget https:// and one bar in final '/'
```

### Contact

```
[+]Email     gvbsec@protonmail.com
[+]Linkedin  linkedin.com/in/gvilela
[+]Telegram  t.me/whoisgvb
```
