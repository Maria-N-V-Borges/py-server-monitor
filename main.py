import requests
import time
from datetime import datetime

def salvar_log(mensagem):
    # 'a' abre o arquivo no modo 'append' (adiciona ao final sem apagar o que já existe)
    with open("log_eventos.txt", "a", encoding="utf-8") as arquivo:
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        arquivo.write(f"[{data_hora}] {mensagem}\n")

def check_server(url):
    print(f"--- Iniciando Polling em: {url} ---")
    salvar_log(f"Monitoramento iniciado para: {url}")

    while True:
        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                msg = f"[ONLINE] {url} está funcionando! (Status: {response.status_code})"
            else:
                msg = f"[ALERTA] {url} respondeu com erro! (Status: {response.status_code})"
            
            print(msg)
            salvar_log(msg)
        
        except requests.exceptions.RequestException:
            msg = f"[OFFLINE] Não foi possível acessar {url}!"
            print(msg)
            salvar_log(msg)

        # Intervalo de Polling (10 segundos)
        time.sleep(10)

# URL para testar
check_server("https://www.google.com")