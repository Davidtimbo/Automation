import pyautogui
from time import sleep 
import requests
from bs4 import BeautifulSoup
import time
      

# Abrir página de visualização manualmente

# Colocar data (dia) atual manualmente

codigos = ['10004', '10009', '10010', '10014', '10016']
for codigo in codigos:

    #Colocar código
    pyautogui.click(x, y)  # Coordenadas do campo de código
    pyautogui.write(codigo)
    
    
    # Apertar enter (pesquisar)
    pyautogui.click(x, y)  # Coordenadas do botão de pesquisa
    
    
    url = 'Sistema de visualização'  # URL do site para visualização


    site = requests.get(url)


    soup = BeautifulSoup(site.content, 'html.parser')


    # Verificar se tem escrito "CPR" e "130,00". 
    
    # Procurando o elemento no HTML
    cpr = soup.find('td', text='AVALIACAO 01/03')
 
    if cpr:
        numero_elemento = cpr.find_next('font', attrs={'size': '3'})
	 if numero_elemento:
            numero = numero_elemento.text.strip()
            pyautogui.copy(numero)    
          
        
        # Abrir app de scanner "xsane"
        pyautogui.click(x, y)  # Coordenadas do ícone do xsane
        
        # Colar o número da sequência
        pyautogui.click(x, y)  # Coordenadas do campo de sequência no xsane
        pyautogui.hotkey('ctrl', 'v')
        
        # Colocar a letra "A" depois da sequência
        pyautogui.write('A')
        
        # Usar atalho "ctrl+seta esq" para ir para o início
        pyautogui.hotkey('ctrl', 'left')
        
        # Colocar o código fornecido anteriormente
        pyautogui.write(codigo)
        
        # Colocar 6 zeros e a data atual invertida
        pyautogui.write('000000' + 'data atual invertida')
        
        # Usar atalho "ctrl+enter"
        pyautogui.hotkey('ctrl', 'enter')
        
        # Aguardar
        time.sleep(5)
    
    # Ir para o próximo código





  


