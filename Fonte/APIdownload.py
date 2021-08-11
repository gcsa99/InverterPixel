#Imports Packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

def carregarImagem(keyword):
    #Opens up web driver and goes to Google Images
    driver = webdriver.Edge('C:/msedgedriver.exe')
    driver.get('https://www.google.com.br/imghp?hl=pt-BR&ogbl')

    box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')

    box.send_keys(keyword)
    box.send_keys(Keys.ENTER)
    imagem = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
    imagem.click()
    driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img').screenshot('images/'+keyword+'.jpg')
    return 'images/'+keyword+'.jpg'
