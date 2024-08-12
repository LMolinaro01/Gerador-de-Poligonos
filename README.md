<h1 align = "center"> Gerador de Polígonos em Python </h1>

## Descrição

Este repositório contém um aplicativo com interface gráfica (GUI) desenvolvido em Python usando Tkinter e Matplotlib. O aplicativo permite que você gere e visualize polígonos com um número de lados à sua escolha. Além disso, é possível navegar entre diferentes páginas de polígonos e salvar as imagens geradas.

## Funcionalidades

- **Geração de Polígonos**: Especifique o número de polígonos e a quantidade de lados de cada um.
- **Visualização de Polígonos**: Veja os polígonos gerados na interface gráfica, com a opção de navegar entre as páginas.
- **Download de Imagens**: Salve as imagens dos polígonos em uma pasta de sua preferência.
- **Validação de Entradas**: O programa verifica se o número de lados é apropriado (mínimo de 3 e máximo de 11) e se a quantidade de permutações geradas não sobrecarrega o sistema.

## Funcionamento


### Classe Navigation

Responsável por gerenciar a navegação e visualização dos polígonos. Suas principais funções incluem:

- **Inicialização**: Configura a interface gráfica e inicializa as variáveis.
- **Geração de Vértices**: Cria as coordenadas dos vértices de um polígono regular.
- **Geração de Permutações**: Cria todas as permutações possíveis dos vértices (exceto o primeiro, que é fixo).
- **Plotagem de Polígonos**: Desenha os polígonos com base nas [permutações](#permutacao) geradas.
- **Atualização da Plotagem**: Atualiza a interface com os polígonos desenhados.
- **Criação de Widgets**: Cria os elementos da interface, como botões e canvas.
- **Navegação**: Permite a navegação entre as páginas dos polígonos gerados.
- **Download**: Salva as imagens dos polígonos na pasta escolhida, exibindo uma barra de progresso durante o processo.
---

### Função de Clique do Botão

A função captura as entradas do usuário, valida os valores e inicializa a classe Navigation para desenhar os polígonos.

---

### Configuração da Janela Principal e Widgets

A janela principal da interface é configurada, incluindo campos de entrada, botões e uma barra de progresso. A biblioteca Tkinter é usada para criar a interface, enquanto o Matplotlib é utilizado para plotar os polígonos.

---
### Loop Principal da Interface Gráfica

O loop principal da interface é iniciado, permitindo que você interaja com o aplicativo.

---
## Conceito de Permutação <a name = "permutacao"> </a>

Permutação é a reorganização dos elementos de um conjunto. Por exemplo, se temos o conjunto {1, 2, 3}, as permutações possíveis são: (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2) e (3, 2, 1). No contexto deste código, a permutação é usada para gerar todas as possíveis ordens dos vértices de um polígono, mantendo o primeiro vértice fixo. Isso permite criar diferentes formas para o mesmo polígono básico.


## Limitações e Verificações

O código inclui verificações para garantir que o número de lados seja adequado (mínimo de 3 e máximo de 11) e que a quantidade de permutações geradas não seja excessiva, evitando problemas de desempenho. Se houver algum problema, uma mensagem de erro será exibida.


## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).
