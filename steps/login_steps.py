from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

# Configuração do WebDriver
@given('eu estou na página de login')
def acessar_pagina_login(context):
    context.driver = webdriver.Chrome()  # Certifique-se de ter o ChromeDriver instalado
    context.driver.get("https://exemplo.com/login")  # Substitua pela URL de login do seu sistema

@when('eu insiro "{usuario}" e "{senha}" como credenciais')
def inserir_credenciais(context, usuario, senha):
    context.driver.find_element(By.ID, "username_field").send_keys(usuario)
    context.driver.find_element(By.ID, "password_field").send_keys(senha)

@when('eu clico no botão de login')
def clicar_botao_login(context):
    context.driver.find_element(By.ID, "login_button").click()

@then('eu devo ver a mensagem de boas-vindas "{mensagem}"')
def verificar_mensagem_boas_vindas(context, mensagem):
    elemento = context.driver.find_element(By.ID, "welcome_message")
    assert elemento.text == mensagem
    context.driver.quit()
