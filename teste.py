from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def main(option):
    # Configure o caminho para o ChromeDriver
    chrome_service = Service(executable_path='chromedriver.exe')  # Substitua pelo caminho do seu chromedriver

    # Configurações do navegador
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # Inicializa o navegador
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    try:
        # Acesse o site
        driver.get("https://transparencia.al.pi.leg.br/grid_transp_publico_remuneracao/index.php?nmgp_opcao=pesq&script_case_init=612")

        # Aguarde até que o elemento dropdown esteja disponível
        wait = WebDriverWait(driver, 10)
        dropdown = wait.until(EC.presence_of_element_located((By.NAME, "fp_regfolha")))

        # Crie um objeto Select para o dropdown
        select = Select(dropdown)

        # Selecione a opção desejada usando o value
        select.select_by_value(f'{option}')

        # Aguarde um pouco para garantir que a seleção seja feita
        wait.until(EC.text_to_be_present_in_element((By.NAME, "mesano"), 'DEZEMBRO/2023'))

        # Você pode continuar com outros comandos, como clicar em botões ou extrair informações

    finally:
        # Feche o navegador
        driver.quit()
