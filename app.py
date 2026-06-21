from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.monitor import WhatsAppMonitor


#Você abre o Chrome uma única vez assim:
#chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\ChromeDebug"
#http://127.0.0.1:9222/json - se abrir json com configs ta ok

options = Options()
options.debugger_address = "127.0.0.1:9222"

driver = webdriver.Chrome(options=options)

monitor = WhatsAppMonitor(driver)

monitor.monitorar()