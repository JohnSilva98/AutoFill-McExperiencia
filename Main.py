#Importar bibliotecas
import datetime
import select
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# Inicializa o driver do navegador e maximiza a janela
driver = webdriver.Chrome()
driver.maximize_window()


# Acessa a página do formulário
driver.get("https://www.mcexperienciasurvey.com/Index.aspx?LanguageID=pt-BR")


#Carrega a versão com acessibilidade e seleciona o pais Brasil
driver.find_element(By.XPATH, '//*[@id="surveyQuestions"]/p/a').click()
driver.find_element(By.XPATH, '//*[@id="Index_CountryPicker.3"]').click()


#rolar a pagina até o botão avançar
nextButton = driver.find_element(By.XPATH, '//*[@id="NextButton"]')
driver.execute_script("arguments[0].scrollIntoView();", nextButton)
nextButton.click()

#Preencher CNPJ, data e horário
cnpj = driver.find_element(By.ID, 'InputCNPJ')
cnpj.send_keys("42591651067051")
data = datetime.datetime.now()#pega a data atual

# Seleciona o dia atual no dropdown
drop_dia = Select(driver.find_element(By.ID, 'InputDay'))
drop_dia.select_by_value(str(data.day))


# Seleciona o mês atual no dropdown
drop_mes= Select(driver.find_element(By.ID, 'InputMonth'))
drop_mes.select_by_value(str(data.month))

# Seleciona o ano atual no dropdown
drop_ano = Select(driver.find_element(By.ID, 'InputYear'))
drop_ano.select_by_value(str(data.year))