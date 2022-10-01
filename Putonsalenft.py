from ast import Try
import undetected_chromedriver as uc
from selenium import webdriver
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import *
from seleniumwire import undetected_chromedriver as uc
from fake_useragent import UserAgent
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pyclick import HumanClicker
import pyautogui
import time







if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    
 
   
  
    options.add_extension("metamask.crx")
    
    driver= webdriver.Chrome(

        options=options,
        
    )
    
    driver.maximize_window()
    driver.switch_to.window(driver.window_handles[0])
    driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome')
    driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome')
    # get started
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#app-content > div > div.main-container-wrapper > div > div > div > button'))).click()
     # agree
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#app-content > div > div.main-container-wrapper > div > div > div > div.metametrics-opt-in__footer > div.page-container__footer > footer > button.button.btn--rounded.btn-primary.page-container__footer-button'))).click()
    # new wallet
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#app-content > div > div.main-container-wrapper > div > div > div.select-action__wrapper > div > div.select-action__select-buttons > div:nth-child(2) > button'))).click()
   
    # passwd
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#create-password'))).send_keys('Rajput&225')
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#confirm-password'))).send_keys('Rajput&225')
    # checkbox
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#app-content > div > div.main-container-wrapper > div > div > div:nth-child(2) > form > div.first-time-flow__checkbox-container > div'))).click()
    # create
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#app-content > div > div.main-container-wrapper > div > div > div:nth-child(2) > form > button'))).click()
    # next
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#app-content > div > div.main-container-wrapper > div > div > div.seed-phrase-intro > div > div.seed-phrase-intro__left > div.box.box--flex-direction-row.box--width-1\/3 > button'))).click()
    # remid me later
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#app-content > div > div.main-container-wrapper > div > div > div.reveal-seed-phrase > div.reveal-seed-phrase__buttons > button.button.btn--rounded.btn-secondary.first-time-flow__button'))).click()
    # all network
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#app-content > div > div.app-header > div > div.app-header__account-menu-container > div > div > span'))).click()
    # show test net
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#app-content > div > div.menu-droppo-container.network-droppo > div > div.network-dropdown-header > div.network-dropdown-content > span > a'))).click()
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#app-content > div > div.main-container-wrapper > div > div.settings-page__content > div.settings-page__content__modules > div.settings-page__body > div:nth-child(7) > div:nth-child(2) > div > label > div:nth-child(1) > div:nth-child(2)'))).click()
    # add n test network
    driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/networks/add-network')
    # networkname
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/label/input'))).send_keys('Mumbai')
    # rpc
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/label/input'))).send_keys('https://polygon-mumbai.infura.io/v3/22348f916b8944be930ac83951a7a245')
    # cahinId
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/label/input'))).send_keys('80001')
    # urrency symbol
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/label/input'))).send_keys('MATIC')
    # add network
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]'))).click()

    # import wallet 
    driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#new-account/import')
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="private-key-box"]'))).send_keys('7c852118294e51e653712a81e05800f419141751be58f605c371e15141b007a6')
    time.sleep(5)
    WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app-content"]/div/div[3]/div/div/div[2]/div[2]/div[2]/button[2]'))).click()
    # 
    # driver.get('https://faucet.polygon.technology/')
    # time.sleep(60)
    driver.get('https://bellart.vercel.app/connect')
    time.sleep(3)
    # connect wallet
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[2]/div[3]/button'))).click()
    # metamask
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="chakra-modal--body-3"]/div/div/button[3]'))).click()
    
    time.sleep(10)
    hc=HumanClicker()
    nx,ny=pyautogui.locateCenterOnScreen('next.png',confidence=.8,grayscale=True)
    hc.move((nx,ny),1)
    hc.click()
    time.sleep(10)
    
    cx,cy=pyautogui.locateCenterOnScreen('connect.png',confidence=0.8,grayscale=True)
    hc.move((cx,cy),1)
    hc.click()
    time.sleep(10)
    sx,sy=pyautogui.locateCenterOnScreen('sign.png',confidence=0.8,grayscale=True)
    hc.move((sx,sy),1)
    hc.click()

    time.sleep(5)
    # home
    driver.find_element(By.XPATH,'//*[@id="root"]/div/header/div/div/div[1]/div[1]/a[1]/img').click()
    # author
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="list-item-1"]/div[1]/div[2]/div[4]/div/a'))).click()
    # nft click
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="nav-profile"]/div/div/div/a/img'))).click()
    # put price
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="price"]'))).send_keys('0.1')
    time.sleep(10)
    # click put onsale
    px,py=pyautogui.locateCenterOnScreen('sale.png',confidence=.8,grayscale=True)
    hc.move((px,py),1)
    hc.click()
    time.sleep(5)
    time.sleep(30)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/header/div/div/div[1]/div[1]/a[1]/img').click()
    # driver.find_element(By.XPATH,'//*[@id="createinputfile1"]').send_keys('/home/baibars313/Documents/youtubeBot/nft1.jpg')
    # time.sleep(30)
    # driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[4]/div/div/button').click()

    


    # 
    
    
   
    
    time.sleep(1000)