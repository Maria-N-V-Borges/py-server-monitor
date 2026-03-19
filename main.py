import requests
import time
from datetime import datetime

# Passo 1: Tradutor de status para o seu log ficar mais rico!
STATUS_NOMES = {
    200: "OK (Sucesso)",
    404: "Não Encontrado (URL Errada)",
    403: "Proibido (Sem Acesso)",
    500: "Erro Interno no Servidor",
    503: "Serviço Indisponível"
}

def salvar_log(mensagem):
    # 'a' abre o arquivo no modo 'append' (adiciona ao final sem apagar o que já existe)
    with open("log_eventos.txt", "a", encoding="utf-8") as arquivo:
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        arquivo.write(f"[{data_hora}] {mensagem}\n")

def check_server(lista_de_urls):
    print(f"--- Iniciando Monitoramento de {len(lista_de_urls)} servidores ---")

    while True:
        for url in lista_de_urls:
            try:
                # Simulando um navegador real (User-Agent)
                headers = {'User-Agent': 'Mozilla/5.0'}
                response = requests.get(url, timeout=5, headers=headers)

                # O .get() busca no dicionário. Se não achar, mostra o número puro.
                status_info = STATUS_NOMES.get(response.status_code, f"Código {response.status_code}")

                if response.status_code == 200:
                    msg = f"[ONLINE] {url} - {status_info}"
                else:
                    msg = f"[ALERTA] {url} - Problema Detectado: {status_info}"
            
                print(msg)
                salvar_log(msg)
        
            except requests.exceptions.RequestException:
                msg = f"[OFFLINE] {url} - Incalcançável!"
                print(msg)
                salvar_log(msg)

        print("-" * 30) # Linha separadora para o log ficar organizado
        time.sleep(10)

meus_sites = [
    "https://www.google.com",
    "https://github.com/Maria-N-V-Borges", 
    "https://www.siteque-nao-existe.com.br"
]

check_server(meus_sites)