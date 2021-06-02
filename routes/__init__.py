from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
from flask import jsonify, request
from app_core import app
import os

@app.route("/")
def root():
    return jsonify({'mensage':'inicio API'}) 

@app.route("/scraping", methods=['POST'])
def scraping( ):
    req = request.get_json(silent=True)
    if not req:
        return jsonify({'mensage':'error'})
    # ubicacion = os.getcwd() +"/driver/" + "chromedriver.exe"
    # driver = webdriver.Chrome(executable_path=ubicacion) 
    driver = webdriver.Chrome(os.path.normpath(os.getcwd()+"\\webdriver\\chromedriver.exe")) 
    try:    
    
        # ubicacion = "C:\\INSERTE_RUTA\\chromedriver.exe"
        
   
        _nro =  request.json['nro']
        _id =  request.json['id']
        _correo =  request.json['email']

        driver.get("https://www.pagostore.com/app")
        time.sleep(10)
        driver.maximize_window()

        driver.find_element_by_class_name("_3TqH_GzIKGvl5zE4o8qVY_").click() 
        time.sleep(2)

        divFrame = driver.find_element_by_class_name("_398I0fs2EPlZotPmbmuUDk")
        divOpciones = divFrame.find_elements_by_class_name("CoL3r47acbYtO6eGLcT6G")
        i = 0
        for divOpcione in divOpciones:
            i = i + 1
            if i == 2:
                divOpcione.click()

        imputID = driver.find_element_by_class_name("oxVbmPqVSkCVx79GnnLc7")
        imputID.send_keys(_id)
        time.sleep(60)

        # presiono boton captcha
        driver.find_element_by_class_name("_3duKww4d68rWsj1YAVEbYt").click()
        time.sleep(4)

        # busco el diamante requerido
        divDiamante = driver.find_element_by_class_name("_3itcD-Pl_RmzhuigTd5VQN")
        aDiamantes = divDiamante.find_elements_by_class_name("qeVolXTT3AXVHe1jJL3lt")
        i = 0
        for aDiamante in aDiamantes:
            i = i + 1
            divDato = aDiamante.find_element_by_class_name("_3V9DM0qZ5XUDQCKZboGom")
            divDatoDiamante = divDato.find_element_by_class_name("_1v4QMCKGPgfdVXYRO07us")
            # print(divDatoDiamante.text)
            if i == int(_nro):
                aDiamante.click()

        #ingreso el correo
        time.sleep(2)
        imputCorreo = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[5]/div[2]/div[3]/div/div[2]/div[5]/div/div[2]/input")
        imputCorreo.send_keys(_correo)

        # preciono boton proceder pago
        driver.find_element_by_class_name("_3duKww4d68rWsj1YAVEbYt").click()
        time.sleep(6)

        # escojo el pago  
        apphome = driver.find_element_by_tag_name("app-home")

        divResultado = apphome.find_element_by_class_name("boxTransaction")
        pResultados = divResultado.find_elements_by_tag_name("p")
        selecc = 0
        for pResultado in pResultados:
            selecc = selecc + 1
            if selecc == 1:
                regresa = pResultado.text

            # print(pResultado.text)
        # print(regresa)
        
        driver.close()
        driver.quit()
        regresa = regresa.split(":")
        return jsonify({'respuesta':regresa[1].strip()})
    
    except Exception:
        driver.close()
        driver.quit()
        return jsonify({'respuesta':'error'})
  



from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException   
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException


import random
import urllib
import speech_recognition as sr
import patch
import pydub


@app.route("/dos")
def dos( ):
    while(True):
        try:
            #create chrome driver
            driver = webdriver.Chrome(os.path.normpath(os.getcwd()+"\\webdriver\\chromedriver.exe")) 
            time.sleep(random.randint(2,3))
            #go to website
            driver.get("https://www.google.com/recaptcha/api2/demo")
            break
        except:
            #patch chromedriver if not available or outdated
            try:
                driver
            except NameError:
                is_patched = patch.download_lastest_chromedriver()
            else:
                is_patched = patch.download_lastest_chromedriver(driver.capabilities['version'])
            if (not is_patched): 
                return jsonify({'mensage':'[-] Please update the chromedriver.exe in the webdriver folder according to your chrome version:https://chromedriver.chromium.org/downloads'})
                # print("[-] Please update the chromedriver.exe in the webdriver folder according to your chrome version:https://chromedriver.chromium.org/downloads")
                break
            return jsonify({'mensage':'error'})
            
    #main program        
    #switch to recaptcha frame
    frames=driver.find_elements_by_tag_name("iframe")
    driver.switch_to.frame(frames[0])
    time.sleep(random.randint(2,3))
    
    #click on checkbox to activate recaptcha
    driver.find_element_by_class_name("recaptcha-checkbox-border").click()
    
    #switch to recaptcha audio control frame
    driver.switch_to.default_content()
    frames=driver.find_element_by_xpath("/html/body/div[2]/div[4]").find_elements_by_tag_name("iframe")
    driver.switch_to.frame(frames[0])
    time.sleep(random.randint(2,3))
    
    #click on audio challenge
    driver.find_element_by_id("recaptcha-audio-button").click()
    
    #switch to recaptcha audio challenge frame
    driver.switch_to.default_content()
    frames= driver.find_elements_by_tag_name("iframe")
    driver.switch_to.frame(frames[-1])
    time.sleep(random.randint(2,3))
    
    #click on the play button
    driver.find_element_by_xpath("/html/body/div/div/div[3]/div/button").click()
    
    #get the mp3 audio file
    src = driver.find_element_by_id("audio-source").get_attribute("src")
    print("[INFO] Audio src: %s"%src)
    
    #download the mp3 audio file from the source
    urllib.request.urlretrieve(src, os.path.normpath(os.getcwd()+"\\sample.mp3"))
    time.sleep(random.randint(2,3))
    
    #load downloaded mp3 audio file as .wav
    try:
        sound = pydub.AudioSegment.from_mp3(os.path.normpath(os.getcwd()+"\\sample.mp3"))
        sound.export(os.path.normpath(os.getcwd()+"\\sample.wav"), format="wav")
        sample_audio = sr.AudioFile(os.path.normpath(os.getcwd()+"\\sample.wav"))
    except:
        print("[-] Please run program as administrator or download ffmpeg manually, http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/")
        
    #translate audio to text with google voice recognition
    r= sr.Recognizer()
    with sample_audio as source:
        audio = r.record(source)
    key=r.recognize_google(audio)
    print("[INFO] Recaptcha Passcode: %s"%key)
    
    #key in results and submit
    driver.find_element_by_id("audio-response").send_keys(key.lower())
    driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)
    driver.switch_to.default_content()
    time.sleep(random.randint(2,3))
    driver.find_element_by_id("recaptcha-demo-submit").click()
    time.sleep(random.randint(2,3))
    driver.close()
    driver.quit()
    return jsonify({'mensage':'ok'})
    

    