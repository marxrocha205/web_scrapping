from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

def main(option, name, qtd):
    # Inicializa o serviço do ChromeDriver e cria uma instância do navegador
    service = Service('chromedriver.exe')  # Caminho para o seu ChromeDriver
    driver = webdriver.Chrome(service=service)

    # Define os nomes das colunas que serão usadas no DataFrame
    columns = ['Nome', 'Cargo', 'Regime', 'Salário Base', 'Auxílio', 'Abono', 'Previdência', 'Imposto de Renda']
    
    # Lista para armazenar as linhas de dados coletadas
    data = []

    try:
        # Navega para a URL especificada
        driver.get("https://transparencia.al.pi.leg.br/grid_transp_publico_remuneracao/index.php?nmgp_opcao=pesq&script_case_init=612")
        
        # Cria um objeto WebDriverWait para aguardar elementos carregarem
        wait = WebDriverWait(driver, 30)
        
        # Aguarda até que o dropdown (campo de seleção) esteja presente e seleciona o valor especificado
        dropdown = wait.until(EC.presence_of_element_located((By.NAME, "fp_regfolha")))
        select = Select(dropdown)
        select.select_by_value(f'{option}')

        time.sleep(2)  # Aguarda 2 segundos para garantir que a página tenha tempo para atualizar

        # Aguarda até que o botão de pesquisa esteja clicável e clica nele
        search_button = wait.until(EC.element_to_be_clickable((By.ID, 'sc_b_pesq_top')))
        search_button.click()

        # Aguarda o iframe ficar disponível, muda o contexto para ele e aguarda seu carregamento
        iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'nmsc_iframe_grid_transp_publico_remuneracao')))

        servidor_index = 1  # Índice para iterar sobre servidores
        page = 1  # Número da página atual

        while True:
            try:
                # Coleta os dados do servidor atual
                servidor = wait.until(EC.visibility_of_element_located((By.ID, f'id_sc_field_fp_servidor_{servidor_index}'))).text
                cargo = wait.until(EC.visibility_of_element_located((By.ID, f'id_sc_field_fp_cargo_{servidor_index}'))).text
                regime = wait.until(EC.visibility_of_element_located((By.ID, f'id_sc_field_fp_regime_{servidor_index}'))).text

                # Tenta clicar no botão associado ao servidor
                try:
                    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'.sc-actionbar-button-container.sc-actbtn-group-left_{servidor_index}')))
                    button.click()
                except Exception as e:
                    print(f"Erro ao clicar no botão para o servidor com índice {servidor_index}: {e}")
                    break

                # Tenta localizar o elemento 'tr' que contém detalhes adicionais
                try:
                    tr_element = wait.until(EC.visibility_of_element_located((By.ID, f'apl_grid_transp_publico_remuneracao_movto#?#{servidor_index}')))
                except Exception as e:
                    print(f"Erro ao localizar o elemento tr para o servidor com índice {servidor_index}: {e}")
                    servidor_index += 1
                    time.sleep(0.5)
                    continue

                # Coleta os valores dos campos específicos, se existirem
                sal_base = tr_element.find_element(By.ID, 'id_sc_field_mv_valor_1').text if tr_element.find_elements(By.ID, 'id_sc_field_mv_valor_1') else ''
                aux = tr_element.find_element(By.ID, 'id_sc_field_mv_valor_2').text if tr_element.find_elements(By.ID, 'id_sc_field_mv_valor_2') else ''
                abono = tr_element.find_element(By.ID, 'id_sc_field_mv_valor_3').text if tr_element.find_elements(By.ID, 'id_sc_field_mv_valor_3') else ''
                previdencia = tr_element.find_element(By.ID, 'id_sc_field_mv_valor_4').text if tr_element.find_elements(By.ID, 'id_sc_field_mv_valor_4') else ''
                imposto = tr_element.find_element(By.ID, 'id_sc_field_mv_valor_5').text if tr_element.find_elements(By.ID, 'id_sc_field_mv_valor_5') else ''
                button.click()  # Clique para voltar à lista de servidores
                
                # Adiciona a linha de dados coletados à lista
                new_row = [servidor, cargo, regime, sal_base, aux, abono, previdencia, imposto]
                data.append(new_row)
                
                # Incrementa o índice do servidor
                servidor_index += 1

                # Verifica se o índice de servidores excede o limite
                if servidor_index > 50:
                    page += 1
                    try:
                        # Clica no botão para avançar para a próxima página, se necessário
                        if qtd != 0 and page > qtd:
                            break
                        next_button = wait.until(EC.element_to_be_clickable((By.ID, 'forward_bot')))
                        next_button.click()
                        
                        servidor_index = 1  # Reseta o índice do servidor para a nova página
                        driver.switch_to.default_content()  # Retorna ao contexto principal
                        time.sleep(1)
                        iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'nmsc_iframe_grid_transp_publico_remuneracao')))
                        driver.execute_script("window.scrollTo(0, 0);")
                        time.sleep(3)  # Aguarda o carregamento da nova página
                    except Exception as e:
                        print(f"Erro ao clicar no botão de avançar: {e}")
                        break
                    else:
                        print(f"Página atual: {page}")
                        continue

                time.sleep(2)  # Tempo de espera entre iterações

            except Exception as e:
                print(f"Erro ao processar o servidor com índice {servidor_index}: {e}")
                break

        # Cria um DataFrame com os dados coletados e salva em um arquivo Excel
        df = pd.DataFrame(data, columns=columns)
        df.to_excel(f'{name}.xlsx', index=False, engine='openpyxl')
        print(f"Dados salvos em '{name}.xlsx'")
        
    except Exception as e:
        print(f"Erro ao interagir com a página: {e}")

    finally:
        # Garante que o navegador seja fechado corretamente
        driver.switch_to.default_content()
        driver.quit()
