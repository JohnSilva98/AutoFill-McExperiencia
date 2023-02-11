#Importar bibliotecas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Inicializa o driver do navegador
driver = webdriver.Chrome()


# Acessa a página do formulário
driver.get("https://www.mcexperienciasurvey.com/Index.aspx?LanguageID=pt-BR")

#Seleciona Pais Brasil
driver.find_element(By.XPATH, '//*[@id="Index_CountryPicker.3"]')