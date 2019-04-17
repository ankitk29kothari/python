from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
driver = webdriver.Ie("IEDriverServer.exe")

#driver.get("https://self.sso.infra.ftgroup/logingassifaible.jsp?activateWindows=true&TYPE=33554433&REALMOID=06-000ad14a-2fb1-1b71-8d9e-e8be0aaad064&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=$SM$oZTcp9kVJA%2flPMtmsn9zkq6Iw0B6Jp5IWpl68ZLAVXeSQkGVKLmdn732MFgqX%2bJw&TARGET=$SM$HTTPS%3a%2f%2fself%2esso%2einfra%2eftgroup%2fAuthForm%2fredirect%2ejsp%3fRETURN%3dhttp$%3A%2f%2fmytools%2esso%2einfra%2eftgroup%2fbinmytools%2fPortfolio%2easpx#");
#d_layer = driver.find_element_by_link_text('activer')
#d_layer.click()

#time.sleep(12)
driver.get("http://mytools.sso.infra.ftgroup/binbeemytools/Home/Portfolio")

time.sleep(5)
driver.get("http://sav-oceane.sso.infra.ftgroup/binOceane/Home/OpenStartPage")
time.sleep(8)

a=driver.window_handles[0]
driver.switch_to.window(a)


"""frame1 = driver.find_elements_by_xpath('//frame')
print len(frame1)"""
time.sleep(5)

html_source = driver.page_source
print(html_source)

d_layer = driver.find_element_by_link_text('ticket lists')
d_layer.click()



