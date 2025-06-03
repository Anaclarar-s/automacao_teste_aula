# Cenário 1: Cadastro com email e senha válidos
#1
from selenium import webdriver  # type: ignore
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoblaze.com")
time.sleep(2)

driver.find_element(By.ID, "signin2").click()
time.sleep(2)

driver.find_element(By.ID, "sign-username").send_keys("usuarioTeste1")
driver.find_element(By.ID, "sign-password").send_keys("Senha123!")
driver.find_element(By.XPATH, "//button[text()='Sign up']").click()
time.sleep(5)

driver.quit()
# Cenário 2: Cadastro com campo de email vazio

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoblaze.com")
time.sleep(2)

driver.find_element(By.ID, "signin2").click()
time.sleep(2)

driver.find_element(By.ID, "sign-username").send_keys("")
driver.find_element(By.ID, "sign-password").send_keys("Senha123!")
driver.find_element(By.XPATH, "//button[text()='Sign up']").click()
time.sleep(5)

driver.quit()
# Cenário 3: Cadastro com campo de senha vazio

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoblaze.com")
time.sleep(2)

driver.find_element(By.ID, "signin2").click()
time.sleep(2)

driver.find_element(By.ID, "sign-username").send_keys("usuarioTeste2")
driver.find_element(By.ID, "sign-password").send_keys("")
driver.find_element(By.XPATH, "//button[text()='Sign up']").click()
time.sleep(5)

driver.quit()
# Cenário 4: Login com email e senha válidos

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoblaze.com")
time.sleep(2)

driver.find_element(By.ID, "login2").click()
time.sleep(2)

driver.find_element(By.ID, "loginusername").send_keys("usuarioTeste1")
driver.find_element(By.ID, "loginpassword").send_keys("Senha123!")
driver.find_element(By.XPATH, "//button[text()='Log in']").click()
time.sleep(5)

driver.quit()
# Cenário 5: Login com email incorreto

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoblaze.com")
time.sleep(2)

driver.find_element(By.ID, "login2").click()
time.sleep(2)

driver.find_element(By.ID, "loginusername").send_keys("usuarioErrado")
driver.find_element(By.ID, "loginpassword").send_keys("Senha123!")
driver.find_element(By.XPATH, "//button[text()='Log in']").click()
time.sleep(5)

driver.quit()
# Cenário 6: Login com senha incorreta

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoblaze.com")
time.sleep(2)

driver.find_element(By.ID, "login2").click()
time.sleep(2)

driver.find_element(By.ID, "loginusername").send_keys("usuarioTeste1")
driver.find_element(By.ID, "loginpassword").send_keys("senhaErrada")
driver.find_element(By.XPATH, "//button[text()='Log in']").click()
time.sleep(5)

driver.quit()
# Cenário 7: Login com senha vazia

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoblaze.com")
time.sleep(2)

driver.find_element(By.ID, "login2").click()
time.sleep(2)

driver.find_element(By.ID, "loginusername").send_keys("usuarioTeste1")
driver.find_element(By.ID, "loginpassword").send_keys("")
driver.find_element(By.XPATH, "//button[text()='Log in']").click()
time.sleep(5)

driver.quit()
# Cenário 8: Login com email vazio

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoblaze.com")
time.sleep(2)

driver.find_element(By.ID, "login2").click()
time.sleep(2)

driver.find_element(By.ID, "loginusername").send_keys("")
driver.find
# Cenário 9: Login com email e senha que não foram cadastrados

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoblaze.com")
time.sleep(2)

driver.find_element(By.ID, "login2").click()
time.sleep(2)

driver.find_element(By.ID, "loginusername").send_keys("naoCadastrado")
driver.find_element(By.ID, "loginpassword").send_keys("Senha999!")
driver.find_element(By.XPATH, "//button[text()='Log in']").click()
time.sleep(5)

driver.quit()
# Cenário 10: Login com os dois campos vazios

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoblaze.com")
time.sleep(2)

driver.find_element(By.ID, "login2").click()
time.sleep(2)

driver.find_element(By.ID, "loginusername").send_keys("")
driver.find_element(By.ID, "loginpassword").send_keys("")
driver.find_element(By.XPATH, "//button[text()='Log in']").click()
time.sleep(5)

driver.quit()# Cenário 1: Cadastro com email e senha válidos

from selenium import webdriver  # type: ignore
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoblaze.com")
time.sleep(2)

driver.find_element(By.ID, "signin2").click()
time.sleep(2)

driver.find_element(By.ID, "sign-username").send_keys("usuarioTeste1")
driver.find_element(By.ID, "sign-password").send_keys("Senha123!")
driver.find_element(By.XPATH, "//button[text()='Sign up']").click()
time.sleep(5)

driver.quit()
# Cenário 2: Cadastro com campo de email vazio

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoblaze.com")
time.sleep(2)

driver.find_element(By.ID, "signin2").click()
time.sleep(2)

driver.find_element(By.ID, "sign-username").send_keys("")
driver.find_element(By.ID, "sign-password").send_keys("Senha123!")
driver.find_element(By.XPATH, "//button[text()='Sign up']").click()
time.sleep(5)

driver.quit()
# Cenário 3: Cadastro com campo de senha vazio

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoblaze.com")
time.sleep(2)

driver.find_element(By.ID, "signin2").click()
time.sleep(2)

driver.find_element(By.ID, "sign-username").send_keys("usuarioTeste2")
driver.find_element(By.ID, "sign-password").send_keys("")
driver.find_element(By.XPATH, "//button[text()='Sign up']").click()
time.sleep(5)

driver.quit()
# Cenário 4: Login com email e senha válidos

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoblaze.com")
time.sleep(2)

driver.find_element(By.ID, "login2").click()
time.sleep(2)

driver.find_element(By.ID, "loginusername").send_keys("usuarioTeste1")
driver.find_element(By.ID, "loginpassword").send_keys("Senha123!")
driver.find_element(By.XPATH, "//button[text()='Log in']").click()
time.sleep(5)

driver.quit()
# Cenário 5: Login com email incorreto

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoblaze.com")
time.sleep(2)

driver.find_element(By.ID, "login2").click()
time.sleep(2)

driver.find_element(By.ID, "loginusername").send_keys("usuarioErrado")
driver.find_element(By.ID, "loginpassword").send_keys("Senha123!")
driver.find_element(By.XPATH, "//button[text()='Log in']").click()
time.sleep(5)

driver.quit()
# Cenário 6: Login com senha incorreta

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoblaze.com")
time.sleep(2)

driver.find_element(By.ID, "login2").click()
time.sleep(2)

driver.find_element(By.ID, "loginusername").send_keys("usuarioTeste1")
driver.find_element(By.ID, "loginpassword").send_keys("senhaErrada")
driver.find_element(By.XPATH, "//button[text()='Log in']").click()
time.sleep(5)

driver.quit()
# Cenário 7: Login com senha vazia

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoblaze.com")
time.sleep(2)

driver.find_element(By.ID, "login2").click()
time.sleep(2)

driver.find_element(By.ID, "loginusername").send_keys("usuarioTeste1")
driver.find_element(By.ID, "loginpassword").send_keys("")
driver.find_element(By.XPATH, "//button[text()='Log in']").click()
time.sleep(5)

driver.quit()
# Cenário 8: Login com email vazio

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoblaze.com")
time.sleep(2)

driver.find_element(By.ID, "login2").click()
time.sleep(2)

driver.find_element(By.ID, "loginusername").send_keys("")
driver.find
# Cenário 9: Login com email e senha que não foram cadastrados

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoblaze.com")
time.sleep(2)

driver.find_element(By.ID, "login2").click()
time.sleep(2)

driver.find_element(By.ID, "loginusername").send_keys("naoCadastrado")
driver.find_element(By.ID, "loginpassword").send_keys("Senha999!")
driver.find_element(By.XPATH, "//button[text()='Log in']").click()
time.sleep(5)

driver.quit()
# Cenário 10: Login com os dois campos vazios

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoblaze.com")
time.sleep(2)

driver.find_element(By.ID, "login2").click()
time.sleep(2)

driver.find_element(By.ID, "loginusername").send_keys("")
driver.find_element(By.ID, "loginpassword").send_keys("")
driver.find_element(By.XPATH, "//button[text()='Log in']").click()
time.sleep(5)

driver.quit()