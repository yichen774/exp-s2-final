import time
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from flask import Flask,render_template, request

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('finalterm.html')


@app.route('/search',methods=['GET','POST'])
def search():
    driver = webdriver.Chrome()
    titlebtn='//*[@id="EOPMain"]/div/div[2]/div[4]/div[1]/a[1]'
    songname = request.form['keyword']
    website = "https://tw.everyonepiano.com/Music-search/?word="+songname+"&come=web"
    driver.get(website)
    imgbtn='//*[@id="EOPReadScrollerW"]/ul/li[5]/div[1]'
    time.sleep(2) 
    driver.execute_script("window.scrollTo(0,350)")
    driver.find_element(By.XPATH,titlebtn).click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    driver.execute_script("window.scrollTo(0,3000)")
    driver.find_element(By.XPATH,imgbtn).click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[2])
    web = requests.get(driver.current_url, cookies={'over18':'1'})
    soup = BeautifulSoup(web.text, "html.parser")
    imgs = soup.find_all('img')
    name = 0    #  設定圖片編號
    for i in imgs:
        print(i['src'])
        try:
            jpg = requests.get('https://tw.everyonepiano.com'+i['src']) 
            f = open(f'C:/Users/GF65/exp-s2-final/flask/static/img/252086414-00{imgs}.png', 'wb')   
            f.write(jpg.content)   
            f.close()              
            name = name + 1
        except:
            break
    data={'songname':songname,'imgs':imgs}
    return render_template('works.html' ,data=data)
if __name__ == '__main__':
    app.run()