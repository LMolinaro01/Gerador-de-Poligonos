<h1 align = "center"> Gerador de Polígonos em Python </h1>

## **Introdução**

O código apresentado é uma aplicação gráfica desenvolvida em Python utilizando a biblioteca `tkinter` para a interface gráfica e `matplotlib` para a visualização de polígonos. O objetivo principal do programa é gerar e exibir polígonos regulares com base em permutações de vértices, permitindo ao usuário navegar entre diferentes configurações e salvar as imagens geradas. Este documento visa explicar o funcionamento do código de forma técnica, detalhando cada componente e sua funcionalidade, ao mesmo tempo em que busca ser didático para facilitar o entendimento.

![{9CD32CBB-C6F7-414D-9EC4-A1AC4D4A19C1}](https://github.com/user-attachments/assets/bbea152d-9a54-45f7-95d9-90ae1de1ea34)

![image](https://github.com/user-attachments/assets/e63b7bb9-7a01-40c9-9f23-2f96c54f9775)

![{C48EF9C6-CA7A-4679-87F7-C51C25A8BD32}](https://github.com/user-attachments/assets/f9feb3a7-bd31-4404-a7e3-606cc5f3ce91)


## **Conceito de Permutação**

Permutação é a reorganização dos elementos de um conjunto. Por exemplo, se temos o conjunto {1, 2, 3}, as permutações possíveis são: (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2) e (3, 2, 1). No contexto deste código, a permutação é usada para gerar todas as possíveis ordens dos vértices de um polígono, mantendo o primeiro vértice fixo. Isso permite criar diferentes formas para o mesmo polígono básico.

## **Estrutura do Código**

O código está organizado em uma classe principal chamada `Navigation`, que gerencia a lógica de geração, exibição e navegação dos polígonos. Além disso, há funções auxiliares para interação com o usuário e controle da interface gráfica. A seguir, detalharemos cada parte do código.


### **1. Importação de Bibliotecas**

O código começa com a importação das bibliotecas necessárias:

- `tkinter`: Para criar a interface gráfica.
- `matplotlib`: Para plotar os polígonos.
- `numpy`: Para cálculos matemáticos, como geração de coordenadas dos vértices.
- `itertools`: Para gerar permutações dos vértices.
- `os`: Para manipulação de diretórios durante o salvamento das imagens.

``` py
pip install tk matplotlib numpy
```


Essas bibliotecas são essenciais para o funcionamento do programa, cada uma desempenhando um papel específico.

### **2. Classe `Navigation`**

A classe `Navigation` é o núcleo do programa. Ela encapsula toda a lógica de geração e exibição dos polígonos, além de gerenciar a navegação entre as páginas de resultados.

#### **2.1. Método `__init__`**

O método `__init__` inicializa os atributos da classe, como o número de polígonos, o número de lados, as permutações geradas e o índice atual de exibição. Além disso, ele configura a interface gráfica, criando uma figura do `matplotlib` e ajustando o layout para exibir os polígonos.

#### **2.2. Método `generate_polygon_vertices`**

Este método calcula as coordenadas dos vértices de um polígono regular com base no número de lados fornecido. Utiliza funções trigonométricas (`np.cos` e `np.sin`) para determinar as posições dos vértices em um círculo unitário.

#### **2.3. Método `generate_permutations`**

Gera todas as permutações possíveis dos vértices do polígono, excluindo o vértice inicial (0) para evitar redundâncias. Essas permutações são usadas para criar diferentes configurações do polígono.

#### **2.4. Método `plot_polygon`**

Este método plota um polígono com base em uma permutação específica de vértices. Ele utiliza a classe `Polygon` do `matplotlib` para desenhar o polígono e adiciona um rótulo numérico para identificação.

#### **2.5. Método `update_plot`**

Atualiza a exibição dos polígonos na interface gráfica. Ele divide a figura em subplots para exibir múltiplos polígonos por página e ajusta o layout conforme necessário.

#### **2.6. Métodos de Navegação (`on_prev_clicked` e `on_next_clicked`)**

Esses métodos permitem ao usuário navegar entre as páginas de polígonos, atualizando o índice de exibição e redesenhandoo a figura.

#### **2.7. Método `on_download_clicked`**

Permite ao usuário salvar as imagens dos polígonos em um diretório escolhido. O método também inclui uma barra de progresso para fornecer feedback visual durante o processo de salvamento.

![{FAAD842A-805F-4898-A494-5A6875F1125A}](https://github.com/user-attachments/assets/d331181f-9fba-4523-95ca-e6094fa56621)


#### **2.8. Método `create_widgets`**

Cria os widgets da interface gráfica, como botões de navegação e a área de exibição dos polígonos.

### **3. Funções Auxiliares**

#### **3.1. `on_button_click`**

Esta função é acionada quando o usuário clica no botão "Gerar". Ela valida as entradas do usuário (número de polígonos e lados) e inicia o processo de geração e exibição dos polígonos.

#### **3.2. `show_initial_widgets`**

Reinicia a interface gráfica para o estado inicial, permitindo ao usuário inserir novos parâmetros.

### **4. Interface Gráfica**

A interface gráfica é construída utilizando `tkinter`. Ela inclui:

- Campos de entrada para o número de polígonos e lados.
- Um slider para definir quantos polígonos serão exibidos por página.
- Botões para gerar polígonos, navegar entre páginas, salvar imagens e resetar a interface.

## **Funcionamento do Programa**

1. O usuário insere o número de polígonos e lados desejados.
2. O programa gera as permutações dos vértices e calcula as coordenadas dos polígonos.
3. Os polígonos são exibidos em uma grade, com navegação entre páginas.
4. O usuário pode salvar as imagens dos polígonos em um diretório escolhido.

## **Considerações Finais**

O código apresentado é um exemplo de como combinar diferentes bibliotecas Python para criar uma aplicação gráfica interativa. Ele demonstra conceitos importantes, como:

- Geração de polígonos regulares.
- Uso de permutações para criar variações.
- Integração entre `tkinter` e `matplotlib`.
- Gerenciamento de interface gráfica e interação com o usuário.

Este programa pode ser expandido de várias formas, como a adição de mais opções de personalização (cores, estilos de linha) ou a implementação de funcionalidades avançadas, como a exportação de animações ou a geração de polígonos em 3D.


## **Conclusão**

O código é uma ferramenta poderosa para explorar conceitos geométricos e de programação. Ele combina técnicas de matemática, programação e design de interface para criar uma experiência interativa e educativa. Compreender seu funcionamento é um passo importante para dominar o desenvolvimento de aplicações gráficas em Python.



## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).
