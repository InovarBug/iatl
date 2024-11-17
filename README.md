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
- `gui.py`: Módulo para a interface gráfica (não utilizado diretamente, integrado em main.py)

## Como Usar

1. Execute o script `main.py`
2. Na interface gráfica, insira:
   - A tecla da habilidade que deseja automatizar
   - A região da tela onde a habilidade é exibida (formato: x,y,largura,altura)
   - A cor que indica que a habilidade está ativa (formato: R,G,B)
3. Clique em "Iniciar" para começar a automação

## Melhorias Realizadas

1. Implementação de uma interface gráfica para facilitar o uso
2. Modularização do código para melhor organização e manutenibilidade
3. Uso de processamento de imagem para detecção mais precisa de habilidades ativas

## Passos para Melhorias Futuras

1. Implementar um sistema de configuração para salvar e carregar configurações de habilidades
2. Adicionar suporte para múltiplas habilidades simultaneamente
3. Melhorar a precisão da detecção de habilidades usando técnicas mais avançadas de processamento de imagem ou machine learning
4. Implementar um sistema de logging para rastrear o uso de habilidades e possíveis erros
5. Adicionar uma funcionalidade de "modo de aprendizagem" para facilitar a configuração de novas habilidades
6. Otimizar o desempenho do script para reduzir o uso de recursos do sistema
7. Implementar medidas de segurança adicionais para evitar detecção como software não autorizado
8. Adicionar suporte para diferentes resoluções de tela e configurações gráficas do jogo
9. Criar uma documentação mais detalhada e um guia de uso passo a passo

## Aviso Legal

Este script é apenas para fins educacionais e de demonstração. O uso de scripts de automação em jogos online pode violar os termos de serviço do jogo. Use por sua própria conta e risco.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias ou correções.

