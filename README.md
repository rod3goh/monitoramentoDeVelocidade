# monitoramentoDeVelocidade

Este projeto é um script Python que automatiza a execução de testes de velocidade da Internet utilizando o Speedtest. Os resultados do teste, incluindo velocidades de download e upload, ping e uma URL para visualizar o resultado, são salvos em um arquivo Excel.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `openpyxl`
  - `subprocess`
  - `datetime`
  - `json`
  - `os`

- Ferramenta de linha de comando Speedtest CLI:
  - [Speedtest CLI](https://www.speedtest.net/apps/cli)

## Instalação

1. Clone este repositório para sua máquina local:

   ```bash
   git clone https://github.com/seu_usuario/testes-velocidade.git
   cd testes-velocidade

1 - Instale as dependências necessárias. Você pode usar o pip para instalar o openpyxl:

pip install openpyxl

2 - Instale o Speedtest CLI seguindo as instruções em Speedtest CLI

3 - Execute o script Python:
python testes_velocidade.py

O script irá rodar um teste de velocidade a cada 10 minutos (600 segundos) e armazenar os resultados em um arquivo chamado testes_velocidade.xlsx.

O arquivo Excel conterá as seguintes colunas:

Data e Hora
Download (Mbps)
Upload (Mbps)
Ping (ms)
URL do Resultado
Funcionamento
O script tenta usar um servidor específico (ID 45663) para o teste de velocidade. Se esse servidor não estiver disponível, ele escolherá automaticamente um servidor disponível.
Os resultados do teste são extraídos e convertidos de bytes para megabits antes de serem salvos no arquivo Excel.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request.

Licença
Este projeto está licenciado sob a Licença MIT.


### Instruções para Personalização
- Substitua `seu_usuario` na linha de clone pelo seu nome de usuário do GitHub.
- Certifique-se de que o nome do arquivo Python (`testes_velocidade.py`) corresponda ao nome real do arquivo no seu projeto.
- Se houver mais detalhes específicos sobre o funcionamento ou requisitos do seu projeto, sinta-se à vontade para adicioná-los ao README.

Com esse README, qualquer pessoa que acessar seu repositório no GitHub terá uma boa ideia do que o projeto faz, como configurá-lo e como utilizá-lo. Se precisar de mais alguma coisa ou de ajustes, é só avisar!

