#Importar bibliotecas
import datetime
import random
import select
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
mes = str(data.month).zfill(2)
# Seleciona o dia atual no dropdown
drop_dia = Select(driver.find_element(By.ID, 'InputDay'))
drop_dia.select_by_value(str(data.day))


# Seleciona o mês atual no dropdown

drop_mes= Select(driver.find_element(By.ID, 'InputMonth'))
drop_mes.select_by_value(str(mes))

# Seleciona o ano atual no dropdown
drop_ano = Select(driver.find_element(By.ID, 'InputYear'))
drop_ano.select_by_value(str(data.year))

#Preencher hora atual, com leves atrasos
hora = str(data.hour).zfill(2)#pega a hora atual
minutos = str((data.minute - random.randint(1, 10)) % 60).zfill(2)#pega os minutos atuais e cria um atraso aleatório

#seleciona a hora
drop_hora = Select(driver.find_element(By.ID, 'InputHour'))
drop_hora.select_by_value(hora)

#seleciona os minutos, garantindo um atraso
drop_min = Select(driver.find_element(By.ID, 'InputMinute'))
drop_min.select_by_value(minutos)

#Marcar o aceite dos termos

#rolar a pagina até o botão aceite
eula = driver.find_element(By.XPATH, '//*[@id="Index_OptIn"]')
driver.execute_script("arguments[0].scrollIntoView();", eula)
eula.click()