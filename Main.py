#Importar bibliotecas
import pyautogui
import datetime
import Comentarios
import Lista_pessoas
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import tkinter as tk
from tkinter import messagebox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





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

#Iniciar o form
Iniciar = driver.find_element(By.ID, 'NextButton').click()


#Selecionar form balcão
form = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#FNSR000001 > div > div > div.Opt1.rbloption > label')))
form.click()

#avançar para próxima tela
driver.find_element(By.ID, 'NextButton').click()

#selecionar comeu no restaurante e avançar
driver.find_element(By.CSS_SELECTOR, '#FNSR000002 > div > div > div.Opt1.rbloption > label').click()
driver.find_element(By.ID, 'NextButton').click()

#selecionar se estava com criança ou não
Resp = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="R000003.1"]')))
Resp.click()
#driver.find_element(By.CSS_SELECTOR, '//*[@id="R000003.1"]').click
driver.find_element(By.ID, 'NextButton').click()

#Selecionar satisfação geral
driver.find_element(By.XPATH, '//*[@id="R000004.5"]').click()
driver.find_element(By.ID, 'NextButton').click()

#selecionar lista de satisfações
Sabor = driver.find_element(By.XPATH, '//*[@id="R000008.5"]').click()
Cordialidade = driver.find_element(By.XPATH, '//*[@id="R000007.5"]').click()
QualidadeComida = driver.find_element(By.XPATH, '//*[@id="R000009.5"]').click()
LimpezaRestaurante = driver.find_element(By.XPATH, '//*[@id="R000010.5"]').click()
Rapidez = driver.find_element(By.XPATH, '//*[@id="R000006.5"]').click()
CxB = driver.find_element(By.XPATH, '//*[@id="R000012.5"]').click()
driver.find_element(By.ID, 'NextButton').click()

#pedido correto
driver.find_element(By.XPATH, '//*[@id="FNSR000013"]/td[1]').click()
driver.find_element(By.ID, 'NextButton').click()

#Nota 0 - 10
driver.find_element(By.XPATH, '//*[@id="R000015.5"]').click()
driver.find_element(By.XPATH, '//*[@id="R000016.10"]').click()
driver.find_element(By.ID, 'NextButton').click()

#comentário
coment = driver.find_element(By.XPATH, '//*[@id="S000019"]')
coment.click()
coment.send_keys(Comentarios.comment)
driver.find_element(By.ID, 'NextButton').click()

#problemas na visita?
driver.find_element(By.XPATH, '//*[@id="R000020.2"]').click()
driver.find_element(By.ID, 'NextButton').click()

#preencher dados
#nome
nome = driver.find_element(By.XPATH, '//*[@id="S000036"]')
nome.click()
nome.send_keys(Lista_pessoas.first_name)
#sobrenome
sobrenome = driver.find_element(By.XPATH, '//*[@id="S000028"]')
sobrenome.click()
sobrenome.send_keys(Lista_pessoas.last_name)
#telefone
telefone = driver.find_element(By.XPATH, '//*[@id="S000035"]')
telefone.click()
telefone.send_keys(Lista_pessoas.telefone)
#email
email = driver.find_element(By.XPATH, '//*[@id="S000033"]')
email.click()
email.send_keys(Lista_pessoas.email)
confirmaEmail = driver.find_element(By.XPATH, '//*[@id="S000034"]')
confirmaEmail.click()
confirmaEmail.send_keys(Lista_pessoas.email)
driver.find_element(By.ID, 'NextButton').click()

#ultima tela




