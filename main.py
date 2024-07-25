import tkinter as tk  # Importa a biblioteca tkinter para a interface gráfica
from tkinter import ttk, messagebox, filedialog  # Importa componentes adicionais do tkinter
import matplotlib.pyplot as plt  # Importa o matplotlib para plotagem de gráficos
import numpy as np  # Importa o numpy para operações numéricas
import itertools  # Importa o itertools para gerar permutações
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Importa para integrar matplotlib com tkinter
import os  # Importa o módulo os para operações com o sistema de arquivos

# Define a classe Navigation para gerenciar a interface e a lógica de navegação
class Navigation:
    def __init__(self, root, num_to_show, progress_bar):
        # Inicializa variáveis
        self.num_polygons = 0  # Número de polígonos
        self.num_sides = 0  # Número de lados
        self.seed_permutations = []  # Lista de permutações de vértices
        self.index = 0  # Índice para navegação
        self.num_to_show = num_to_show  # Número de polígonos a serem mostrados por página
        self.x = []  # Coordenadas x dos vértices
        self.y = []  # Coordenadas y dos vértices
        self.root = root  # Referência à janela principal do tkinter
        self.save_directory = None  # Diretório para salvar as imagens
        self.progress_bar = progress_bar  # Barra de progresso

        # Cria uma figura matplotlib para plotar os polígonos
        self.fig, self.ax_list = plt.subplots(figsize=(8, 6))
        plt.subplots_adjust(bottom=0.25)  # Ajusta a figura

        self.create_widgets()  # Cria os widgets da interface

    # Função para gerar vértices de um polígono regular
    def generate_polygon_vertices(self, num_sides):
        radius = 1  # Define o raio do círculo circunscrito
        angles = np.linspace(0, 2 * np.pi, num_sides, endpoint=False)  # Calcula ângulos igualmente espaçados
        x = radius * np.cos(angles)  # Calcula coordenadas x
        y = radius * np.sin(angles)  # Calcula coordenadas y
        return x, y  # Retorna coordenadas x e y

    # Função para gerar todas as permutações possíveis dos vértices
    def generate_permutations(self, num_sides):
        points = tuple(range(1, num_sides))  # Gera uma tupla de pontos
        return list(itertools.permutations(points))  # Retorna uma lista de permutações

    # Função para plotar um polígono
    def plot_polygon(self, perm, x, y, ax, num):
        ax.clear()  # Limpa o eixo
        perm = [0] + list(perm) + [0]  # Adiciona o primeiro ponto no início e no fim da permutação
        x_perm = [x[i] for i in perm]  # Reordena coordenadas x
        y_perm = [y[i] for i in perm]  # Reordena coordenadas y
        polygon = plt.Polygon(np.column_stack([x_perm, y_perm]), closed=True, edgecolor='r', fill=None)  # Cria o polígono
        ax.add_patch(polygon)  # Adiciona o polígono ao eixo
        ax.text(0, -1.5, f'#{num}', color='blue', fontsize=10, ha='center', va='center')  # Adiciona número do polígono
        ax.set_aspect('equal')  # Define proporção igual
        ax.set_xlim(-2, 2)  # Define limites x
        ax.set_ylim(-2, 2)  # Define limites y
        ax.axis('off')  # Remove os eixos

    # Função para atualizar a plotagem
    def update_plot(self):
        num_rows = (self.num_to_show + 9) // 10  # Calcula número de linhas
        num_cols = min(10, self.num_to_show)  # Define número de colunas
        self.fig.clf()  # Limpa a figura
        self.ax_list = [self.fig.add_subplot(num_rows, num_cols, i + 1) for i in range(self.num_to_show)]  # Cria subplots
        for ax, (perm, num) in zip(self.ax_list, zip(self.seed_permutations[self.index:self.index + self.num_to_show], range(self.index, self.index + self.num_to_show))):
            self.plot_polygon(perm, self.x, self.y, ax, num)  # Plota cada polígono
        for ax in self.ax_list[len(self.seed_permutations[self.index:self.index + self.num_to_show]):]:
            ax.axis('off')  # Desativa eixos dos subplots não usados
        total_pages = (self.num_polygons + self.num_to_show - 1) // self.num_to_show  # Calcula número total de páginas
        current_page = self.index // self.num_to_show + 1  # Calcula página atual
        self.fig.suptitle(f"Página {current_page} de {total_pages}", fontsize=12)  # Define título da figura
        self.canvas.draw()  # Atualiza a tela

    # Função para criar os widgets da interface
    def create_widgets(self):
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)  # Cria widget canvas do matplotlib
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)

        # Botões de navegação
        self.btn_prev = ttk.Button(self.root, text='Voltar', command=self.on_prev_clicked)
        self.btn_prev.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.btn_next = ttk.Button(self.root, text='Avançar', command=self.on_next_clicked)
        self.btn_next.grid(row=2, column=2, padx=10, pady=10, sticky=tk.E)

    # Função para ação do botão de voltar
    def on_prev_clicked(self):
        self.index = (self.index - self.num_to_show) % self.num_polygons  # Atualiza índice para página anterior
        self.update_plot()  # Atualiza a exibição

    # Função para ação do botão de avançar
    def on_next_clicked(self):
        self.index = (self.index + self.num_to_show) % self.num_polygons  # Atualiza índice para próxima página
        self.update_plot()  # Atualiza a exibição

    # Função para ação do botão de download
    def on_download_clicked(self):
        if self.save_directory is None:
            self.save_directory = filedialog.askdirectory(title="Escolha o diretório para salvar as imagens")
            if not self.save_directory:
                return

        # Cria a pasta 'polygons_images' no diretório escolhido
        save_folder = os.path.join(self.save_directory, 'polygons_images')
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        num_pages = (self.num_polygons + self.num_to_show - 1) // self.num_to_show

        estimated_size_per_image = 20  # em KB
        total_estimated_size = num_pages * estimated_size_per_image / 1024  # em MB

        # Verifica se o número de arquivos é maior que 100
        if num_pages > 100:
            proceed = messagebox.askyesno(
                "Confirmação",
                f"Você está prestes a salvar {num_pages} arquivos, totalizando aproximadamente {total_estimated_size:.2f} MB. Deseja continuar?"
            )
            if not proceed:
                return

        # Mostrar a barra de progresso
        self.progress_bar.grid(row=4, column=0, columnspan=3, pady=10)
        self.progress_bar['maximum'] = num_pages
        self.progress_bar['value'] = 0

        for page in range(num_pages):
            self.index = page * self.num_to_show
            self.update_plot()
            self.fig.savefig(f'{save_folder}/page_{page + 1}.png')
            self.progress_bar['value'] += 1
            self.root.update_idletasks()

        messagebox.showinfo("Sucesso", f"As imagens foram salvas na pasta {save_folder}")
        self.progress_bar['value'] = 0
        # Esconde a barra de progresso após a conclusão
        self.progress_bar.grid_forget()

    # Função para resetar a interface
    def reset(self):
        # Remove o conteúdo da janela
        for widget in self.root.winfo_children():
            widget.grid_remove()
        # Mostra os widgets da tela inicial
        show_initial_widgets()

# Função para ação do botão de gerar polígonos
def on_button_click():
    global nav

    try:
        num_polygons = int(entry_polygons.get())  # Lê o número de polígonos
        num_sides = int(entry_sides.get())  # Lê o número de lados
        num_to_show = int(slider_polygons.get())  # Lê o número de polígonos por página

        if num_sides < 3:
            raise ValueError("Número de lados deve ser pelo menos 3.")
        if num_sides >= 12:
            raise ValueError("Número de lados muito alto. O desempenho será muito afetado.")

        max_polygons = len(list(itertools.permutations(range(1, num_sides))))
        if num_polygons > max_polygons:
            raise ValueError(f"Para {num_sides} lados, máximo de {max_polygons} permutações é permitido.")

        seed_permutations = list(itertools.permutations(range(1, num_sides)))

        nav = Navigation(root, num_to_show, progress_bar)
        nav.num_polygons = num_polygons
        nav.num_sides = num_sides
        nav.seed_permutations = seed_permutations[:num_polygons]
        nav.x, nav.y = nav.generate_polygon_vertices(nav.num_sides)
        nav.update_plot()

        # Mostrar os botões após desenhar os polígonos
        button_download.grid(column=0, row=3, columnspan=3, pady=10)
        button_reset.grid(column=0, row=4, columnspan=3, pady=10)

    except ValueError as e:
        messagebox.showerror("Erro", str(e))

# Função para mostrar os widgets iniciais
def show_initial_widgets():
    frame.grid(column=0, row=1, sticky=(tk.W, tk.E, tk.N, tk.S))
    button.grid(column=0, row=3, columnspan=2, pady=10)

root = tk.Tk()
root.title("Gerador de Polígonos")

root.geometry("820x600")

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=1, sticky=(tk.W, tk.E, tk.N, tk.S))

label_polygons = ttk.Label(frame, text="Quantidade de Polígonos", font=("Consolas bold", 11))
label_polygons.grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)

entry_polygons = ttk.Entry(frame, width=10, font=("Consolas", 12))
entry_polygons.grid(column=1, row=0, sticky=tk.W, padx=10, pady=10)
entry_polygons.insert(0, "10")

label_sides = ttk.Label(frame, text="Lados de cada Polígono", font=("Consolas bold", 11))
label_sides.grid(column=0, row=1, sticky=tk.W, padx=10, pady=10)

entry_sides = ttk.Entry(frame, width=10, font=("Consolas", 12))
entry_sides.grid(column=1, row=1, sticky=tk.W, padx=10, pady=10)
entry_sides.insert(0, "5")

# Adicionando o slider para selecionar a quantidade de polígonos por página
label_slider = ttk.Label(frame, text="Polígonos por Página", font=("Consolas bold", 11))
label_slider.grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)

slider_polygons = tk.Scale(frame, from_=1, to=20, orient=tk.HORIZONTAL)
slider_polygons.set(5)
slider_polygons.grid(column=1, row=2, sticky=tk.W, padx=10, pady=10)

button = ttk.Button(frame, text="Gerar", command=on_button_click)
button.grid(column=0, row=3, columnspan=2, pady=10)

button_download = ttk.Button(root, text="Salvar Imagens", command=lambda: nav.on_download_clicked())
button_download.grid(column=0, row=3, columnspan=3, pady=10)
button_download.grid_remove()  # Inicialmente escondido

button_reset = ttk.Button(root, text="Voltar para Tela Inicial", command=lambda: nav.reset())
button_reset.grid(column=0, row=4, columnspan=3, pady=15)
button_reset.grid_remove()  # Inicialmente escondido

progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate")
progress_bar.grid(column=0, row=5, columnspan=3, pady=10)
progress_bar.grid_remove()  # Inicialmente escondida

root.mainloop()
