import tkinter as tk
from tkinter import ttk
import main

# Dicionário de opções do ComboBox
options = {
    "JUNHO2024": "684##@@JUNHO/2024",
    "MAIO2024": "683##@@MAIO/2024",
    "ABRIL2024": "682##@@ABRIL/2024",
    "MARCO2024": "681##@@MARCO/2024",
    "FEVEREIRO2024": "679##@@FEVEREIRO/2024",
    "JANEIRO2024": "678##@@JANEIRO/2024",
    "DEZEMBRO2023": "677##@@DEZEMBRO/2023",
    "NOVEMBRO2023": "676##@@NOVEMBRO/2023",
    "OUTUBRO2023": "675##@@OUTUBRO/2023",
    "SETEMBRO2023": "674##@@SETEMBRO/2023",
    "AGOSTO2023": "673##@@AGOSTO/2023",
    "JULHO2023": "672##@@JULHO/2023",
    "JUNHO2023": "671##@@JUNHO/2023",
    "MAIO2023": "670##@@MAIO/2023",
    "ABRIL2023": "669##@@ABRIL/2023",
    "MARCO2023": "668##@@MARCO/2023",
    "FEVEREIRO2023": "667##@@FEVEREIRO/2023",
    "JANEIRO2023": "666##@@JANEIRO/2023",
    "DEZEMBRO2022": "665##@@DEZEMBRO/2022",
    "NOVEMBRO2022": "664##@@NOVEMBRO/2022",
    "OUTUBRO2022": "663##@@OUTUBRO/2022",
    "SETEMBRO2022": "662##@@SETEMBRO/2022",
    "AGOSTO2022": "661##@@AGOSTO/2022",
    "JULHO2022": "660##@@JULHO/2022",
    "JUNHO2022": "659##@@JUNHO/2022",
    "MAIO2022": "658##@@MAIO/2022",
    "ABRIL2022": "657##@@ABRIL/2022",
    "MARCO2022": "656##@@MARCO/2022",
    "FEVEREIRO2022": "655##@@FEVEREIRO/2022",
    "JANEIRO2022": "654##@@JANEIRO/2022",
    "DEZEMBRO2021": "653##@@DEZEMBRO/2021",
    "NOVEMBRO2021": "652##@@NOVEMBRO/2021",
    "OUTUBRO2021": "651##@@OUTUBRO/2021",
    "SETEMBRO2021": "650##@@SETEMBRO/2021",
    "AGOSTO2021": "649##@@AGOSTO/2021",
    "JULHO2021": "648##@@JULHO/2021",
    "JUNHO2021": "647##@@JUNHO/2021",
    "MAIO2021": "646##@@MAIO/2021",
    "ABRIL2021": "645##@@ABRIL/2021",
    "MARCO2021": "644##@@MARCO/2021",
    "FEVEREIRO2021": "643##@@FEVEREIRO/2021",
    "JANEIRO2021": "642##@@JANEIRO/2021",
    "DEZEMBRO2020": "641##@@DEZEMBRO/2020",
    "NOVEMBRO2020": "640##@@NOVEMBRO/2020",
    "OUTUBRO2020": "639##@@OUTUBRO/2020",
    "SETEMBRO2020": "638##@@SETEMBRO/2020",
    "AGOSTO2020": "637##@@AGOSTO/2020",
    "JULHO2020": "636##@@JULHO/2020",
    "JUNHO2020": "635##@@JUNHO/2020",
    "MAIO2020": "634##@@MAIO/2020",
    "ABRIL2020": "633##@@ABRIL/2020",
    "MARCO2020": "632##@@MARCO/2020",
    "FEVEREIRO2020": "631##@@FEVEREIRO/2020",
    "JANEIRO2020": "630##@@JANEIRO/2020",
    "DEZEMBRO2019": "629##@@DEZEMBRO/2019",
    "NOVEMBRO2019": "628##@@NOVEMBRO/2019",
    "OUTUBRO2019": "627##@@OUTUBRO/2019",
    "SETEMBRO2019": "626##@@SETEMBRO/2019",
    "AGOSTO2019": "625##@@AGOSTO/2019",
    "JULHO2019": "624##@@JULHO/2019",
    "JUNHO2019": "623##@@JUNHO/2019",
    "MAIO2019": "622##@@MAIO/2019",
    "ABRIL2019": "621##@@ABRIL/2019",
    "MARCO2019": "620##@@MARCO/2019",
    "FEVEREIRO2019": "619##@@FEVEREIRO/2019",
    "JANEIRO2019": "618##@@JANEIRO/2019",
    "DEZEMBRO2018": "617##@@DEZEMBRO/2018",
    "NOVEMBRO2018": "616##@@NOVEMBRO/2018",
    "OUTUBRO2018": "615##@@OUTUBRO/2018",
    "SETEMBRO2018": "614##@@SETEMBRO/2018",
    "AGOSTO2018": "613##@@AGOSTO/2018",
    "JULHO2018": "612##@@JULHO/2018",
    "JUNHO2018": "611##@@JUNHO/2018",
    "MAIO2018": "610##@@MAIO/2018",
    "ABRIL2018": "609##@@ABRIL/2018",
    "MARCO2018": "608##@@MARCO/2018",
    "FEVEREIRO2018": "607##@@FEVEREIRO/2018",
    "JANEIRO2018": "606##@@JANEIRO/2018",
    "DEZEMBRO2017": "579##@@DEZEMBRO/2017",
    "DEZEMBRO2007MIGRADO": "332##@@DEZEMBRO/2007 MIGRADO"
}

# Função para exibir o valor selecionado
def show_selected_value():
    # Obtém o item selecionado no ComboBox
    selected_month = combo.get()
    
    # Obtém o valor associado à opção selecionada
    value = options.get(selected_month)
    
    # Obtém o valor extra digitado no campo de entrada
    extra_value = extra_entry.get()
    
    # Converte o valor extra para um número inteiro
    qtd = int(extra_value)
    
    # Chama a função principal do módulo 'main' com os valores selecionados
    main.main(value, selected_month, qtd)


    #Se passar a quantidade como 0 ele inicia o loop infinito
# Configuração da janela principal
root = tk.Tk()
root.title("Selecionar Período")  # Define o título da janela
root.geometry("500x200")  # Define o tamanho da janela

# Cria um ComboBox com as chaves do dicionário como opções
combo = ttk.Combobox(root, values=list(options.keys()), state="readonly")
combo.pack(pady=20, padx=10, side=tk.LEFT)  # Adiciona o ComboBox à janela

# Cria um campo de entrada para o usuário digitar um valor extra
extra_entry = tk.Entry(root)
extra_entry.pack(pady=20, padx=10, side=tk.LEFT)  # Adiciona o campo de entrada à janela

# Cria um botão que chama a função 'show_selected_value' quando clicado
select_button = tk.Button(root, text="enviar", command=show_selected_value)
select_button.pack(pady=10, padx=10, side=tk.LEFT)  # Adiciona o botão à janela

# Inicia o loop principal da aplicação, que aguarda eventos
root.mainloop()