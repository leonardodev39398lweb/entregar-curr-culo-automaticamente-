from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def busca_linkedin():
 
 navegador = webdriver.Chrome()
 
 try:
  navegador.get("https://www.google.com")

  campo_busca = WebDriverWait(navegador, 10).until( EC.presence_of_element_located((By.NAME, 'q'))) 

  campo_busca.send_keys("LinkedIn")

  botao = WebDriverWait(navegador, 10).until( EC.element_to_be_clickable((By.NAME, 'btnK')))
  botao.click()
  
  navegador.find_element(By.CLASS_NAME, 'LC20lb').click()


  
  navegador.get("https://www.linkedin.com/login/")
  
  navegador.find_element(By.ID, "username").send_keys("leonardojose.silvae@gmail.com")
  navegador.find_element(By.ID, "password").send_keys("4002892225")

  botao = WebDriverWait(navegador, 10).until( EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
  botao.click()



  WebDriverWait(navegador, 20).until( EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Pesquisar"]')))
        
  campo_busca_linkedin = navegador.find_element(By.XPATH, '//input[@placeholder="Pesquisar"]')
  
  campo_busca_linkedin.send_keys('analista QA ' + Keys.ENTER)

  botao = WebDriverWait(navegador, 40).until( EC.element_to_be_clickable((By.CSS_SELECTOR, ".artdeco-pill.search-reusables__filter-pill-button")))
  botao.click()
        
  elementos_nome_vaga = WebDriverWait(navegador, 30).until( EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".job-card-container__link.job-card-list__title.job-card-list__title--link")))

  elemento_localizacao = WebDriverWait(navegador, 30).until( EC.visibility_of_all_elements_located((By.CLASS_NAME, 'job-card-container__metadata-item')))


  for vaga, localizacao in zip(elementos_nome_vaga, elemento_localizacao):
    print("LINKEDIN")
    print(f"Vaga: {vaga.text}")
    print(f"Localização: {localizacao.text}\n")
       

       
 finally:
  navegador.quit()




busca_linkedin()