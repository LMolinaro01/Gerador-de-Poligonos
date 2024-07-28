# Gerador de Polígonos em Python

## Descrição

Este repositório contém um aplicativo GUI (Interface Gráfica do Usuário) desenvolvido em Python usando Tkinter e Matplotlib. O aplicativo permite aos usuários gerar e visualizar polígonos com um número especificado de lados. Além disso, oferece funcionalidades para navegar entre diferentes páginas de polígonos e salvar as imagens geradas

![image](https://github.com/user-attachments/assets/657056bf-35ad-4977-abd8-1fb8d806b223)
![image](https://github.com/user-attachments/assets/84d86c6c-82ea-4e4a-a09a-75c0ff4de418)
![image](https://github.com/user-attachments/assets/db68047b-5642-4c24-b380-a2eb49b92cd5)


## Funcionalidades

- **Geração de Polígonos**: O usuário pode especificar o número de polígonos e o número de lados de cada polígono.
- **Visualização de Polígonos**: Os polígonos são exibidos na interface gráfica, permitindo a navegação entre páginas de polígonos.
- **Download de Imagens**: O usuário pode salvar as imagens dos polígonos gerados em um diretório de sua escolha.
- **Validação de Entradas**: O programa valida as entradas do usuário para garantir que o número de lados seja adequado (pelo menos 3 e menos que 12) e que a quantidade de permutações geradas não seja excessiva, evitando problemas de desempenho.

## Como Funciona

### Importação de Bibliotecas

O programa importa as bibliotecas necessárias para a interface gráfica, plotagem de gráficos e manipulação de dados.

### Classe `Navigation`

A classe `Navigation` gerencia a navegação e visualização dos polígonos. Suas principais funções incluem:

- **Inicialização**: Configura a interface gráfica e inicializa variáveis.
- **Geração de Vértices**: Gera as coordenadas dos vértices de um polígono regular.
- **Geração de Permutações**: Gera todas as permutações possíveis dos vértices (exceto o primeiro, que é fixo).
- **Plotagem de Polígonos**: Plota os polígonos com base nas permutações geradas.
- **Atualização da Plotagem**: Atualiza a interface gráfica com os polígonos plotados.
- **Criação de Widgets**: Cria os elementos da interface gráfica, como botões e canvas.
- **Navegação**: Permite ao usuário navegar entre as páginas de polígonos gerados.
- **Download**: Salva as imagens dos polígonos em um diretório escolhido pelo usuário, exibindo uma barra de progresso durante o processo.

### Função de Clique do Botão

A função `on_button_click` captura as entradas do usuário, valida os valores e inicializa a classe `Navigation` para desenhar os polígonos.

### Configuração da Janela Principal e Widgets

O código configura a janela principal da interface gráfica, incluindo entradas, botões e uma barra de progresso. Ele utiliza a biblioteca Tkinter para criar a interface e Matplotlib para plotar os polígonos.

### Main Loop da Interface Gráfica

O loop principal da interface gráfica é iniciado, permitindo a interação do usuário com o aplicativo.

## Conceito de Permutação

Permutação é uma rearranjo dos elementos de um conjunto. Por exemplo, se temos um conjunto {1, 2, 3}, as permutações possíveis são: (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2) e (3, 2, 1). No contexto deste código, permutação é utilizada para gerar todas as possíveis ordens dos vértices de um polígono, exceto o primeiro vértice que é fixo. Isso permite a criação de diferentes formas do mesmo polígono básico.

## Limitações e Verificações

O código possui verificações para assegurar que o número de lados seja adequado (pelo menos 3 e menos que 12) e que a quantidade de permutações geradas não seja excessiva, para evitar problemas de desempenho. Se qualquer verificação falhar, uma mensagem de erro é exibida.


## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
