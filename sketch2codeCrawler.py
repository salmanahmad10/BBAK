from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import os
import urllib
import urllib.request as req



def loadImages(dire):
    IMAGES=[]
    for filename in os.listdir(dire):
        if(filename[-3:]=='jpg'):
            IMAGES.append(filename)
    return IMAGES

#idhr neechay images dir ke location dal dae
data=loadImages('..')





path='./chromedriver.exe'
chrome_options = webdriver.ChromeOptions()

driver=webdriver.Chrome(chrome_options=chrome_options,executable_path=path)
driver.get("https://sketch2code.azurewebsites.net/")
driver.maximize_window()
for iteration,i in enumerate(range(len(data))):
    print("#### IMAGES REMAINING ==>",len(data)-iteration)
    driver.find_element_by_id('imageData').send_keys(data[i])
    time.sleep(30)
    img=driver.find_elements_by_class_name("img-finish")
    try:
        src = img[1].get_attribute('src')
        arrr=data[i].split('/')
        imageName=str(arrr[len(arrr)-1]+" converted.png")
        req.urlretrieve(src,imageName)
    except Exception as e:
        print("image not found",e)
    time.sleep(15)

    driver.get("https://sketch2code.azurewebsites.net/")