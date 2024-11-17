# Automação de Habilidades para Throne and Liberty

Este projeto é um script de automação de habilidades para o jogo Throne and Liberty, desenvolvido em Python. Ele utiliza captura de tela em tempo real e processamento de imagem para identificar quando uma habilidade está ativa ou não, e automaticamente ativa a habilidade quando necessário.

## Funcionalidades

1. Captura de tela em tempo real
2. Processamento de imagem para detecção de habilidades ativas
3. Automação de teclas para ativar habilidades
4. Interface gráfica para controle do script

## Estrutura do Projeto

- `main.py`: Arquivo principal que integra todos os módulos e executa a interface gráfica
- `screen_capture.py`: Módulo para captura de tela
- `image_processing.py`: Módulo para processamento de imagem
- `skill_detection.py`: Módulo para detecção de habilidades ativas
- `key_automation.py`: Módulo para automação de teclas
- `gui.py`: Módulo para a interface gráfica

## Como Usar

1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute o script: `python main.py`
4. Na interface gráfica, insira:
   - A tecla da habilidade que deseja automatizar
   - A região da tela onde a habilidade é exibida (formato: x,y,largura,altura)
   - A cor que indica que a habilidade está ativa (formato: R,G,B)
5. Clique em "Iniciar" para começar a automação

## Aviso Legal

Este script é apenas para fins educacionais e de demonstração. O uso de scripts de automação em jogos online pode violar os termos de serviço do jogo. Use por sua própria conta e risco.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias ou correções.
