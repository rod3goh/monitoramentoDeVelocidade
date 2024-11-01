import subprocess
import openpyxl
from datetime import datetime
import time
import json
import os

# Função para converter Bytes para Megabits
def bytes_to_megabits(bytes_value):
    return (bytes_value * 8) / 1_000_000

# Configuração do Excel
def setup_excel(filename):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Testes de Velocidade"
    sheet.append(["Data e Hora", "Download (Mbps)", "Upload (Mbps)", "Ping (ms)", "URL do Resultado"])
    workbook.save(filename)

# Função para adicionar dados ao Excel
def add_to_excel(filename, data):
    workbook = openpyxl.load_workbook(filename)
    sheet = workbook.active
    sheet.append(data)
    workbook.save(filename)

# Função para rodar o teste de velocidade
def run_speed_test(server_id=None):
    if server_id:
        result = subprocess.run(
            ["speedtest", "-s", str(server_id), "--format=json"],
            capture_output=True,
            text=True
        )
    else:
        result = subprocess.run(
            ["speedtest", "--format=json"],
            capture_output=True,
            text=True
        )
    
    if result.returncode != 0:
        raise RuntimeError(f"Erro ao executar speedtest: {result.stderr}")
    return result.stdout

# Programa principal
filename = "testes_velocidade.xlsx"

if not os.path.exists(filename):
    setup_excel(filename)

while True:
    try:
        # Tentativa de rodar o teste com o servidor específico
        output = run_speed_test(45663)
        
    except RuntimeError as e:
        print(e)
        print("Tentando rodar o teste de velocidade com o servidor automático...")
        output = run_speed_test()  # Chama o teste sem servidor

    if output:
        data_json = json.loads(output)
        download_bytes = data_json["download"]["bandwidth"]  # Bytes
        upload_bytes = data_json["upload"]["bandwidth"]      # Bytes
        ping = data_json["ping"]["latency"]
        result_url = data_json["result"]["url"]              # URL do resultado

        # Convertendo Bytes para Megabits
        download_mbps = bytes_to_megabits(download_bytes)
        upload_mbps = bytes_to_megabits(upload_bytes)

        data = [
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            download_mbps,
            upload_mbps,
            ping,
            result_url  # Adicionando a URL do resultado
        ]
        add_to_excel(filename, data)
        print(f"Teste realizado: {data}")

    time.sleep(600)  # Intervalo de 10 minutos (600 segundos)
