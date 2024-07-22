import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import matplotlib.pyplot as plt
import numpy as np
import itertools
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

class Navigation:
    def __init__(self, root, num_to_show, progress_bar):
        self.num_polygons = 0
        self.num_sides = 0
        self.seed_permutations = []
        self.index = 0
        self.num_to_show = num_to_show
        self.x = []
        self.y = []
        self.root = root
        self.save_directory = None
        self.progress_bar = progress_bar

        self.fig, self.ax_list = plt.subplots(figsize=(8, 6))  # Tamanho reduzido da figura
        plt.subplots_adjust(bottom=0.25)

        self.create_widgets()

    def generate_polygon_vertices(self, num_sides):
        radius = 1
        angles = np.linspace(0, 2 * np.pi, num_sides, endpoint=False)
        x = radius * np.cos(angles)
        y = radius * np.sin(angles)
        return x, y

    def generate_permutations(self, num_sides):
        points = tuple(range(1, num_sides))
        return list(itertools.permutations(points))

    def plot_polygon(self, perm, x, y, ax, num):
        ax.clear()
        perm = [0] + list(perm) + [0]
        x_perm = [x[i] for i in perm]
        y_perm = [y[i] for i in perm]
        polygon = plt.Polygon(np.column_stack([x_perm, y_perm]), closed=True, edgecolor='r', fill=None)
        ax.add_patch(polygon)
        ax.text(0, -1.5, f'#{num}', color='blue', fontsize=10, ha='center', va='center')
        ax.set_aspect('equal')
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.axis('off')

    def update_plot(self):
        num_rows = (self.num_to_show + 9) // 10
        num_cols = min(10, self.num_to_show)
        self.fig.clf()
        self.ax_list = [self.fig.add_subplot(num_rows, num_cols, i + 1) for i in range(self.num_to_show)]
        for ax, (perm, num) in zip(self.ax_list, zip(self.seed_permutations[self.index:self.index + self.num_to_show], range(self.index, self.index + self.num_to_show))):
            self.plot_polygon(perm, self.x, self.y, ax, num)
        for ax in self.ax_list[len(self.seed_permutations[self.index:self.index + self.num_to_show]):]:
            ax.axis('off')
        total_pages = (self.num_polygons + self.num_to_show - 1) // self.num_to_show
        current_page = self.index // self.num_to_show + 1
        self.fig.suptitle(f"Página {current_page} de {total_pages}", fontsize=12)
        self.canvas.draw()

    def create_widgets(self):
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Botões de navegação
        self.btn_prev = ttk.Button(self.root, text='Voltar', command=self.on_prev_clicked)
        self.btn_prev.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

        self.btn_next = ttk.Button(self.root, text='Avançar', command=self.on_next_clicked)
        self.btn_next.grid(row=4, column=2, padx=10, pady=10, sticky=tk.E)

    def on_prev_clicked(self):
        self.index = (self.index - self.num_to_show) % self.num_polygons
        self.update_plot()

    def on_next_clicked(self):
        self.index = (self.index + self.num_to_show) % self.num_polygons
        self.update_plot()

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
        self.progress_bar.grid(row=6, column=0, columnspan=2, pady=10)
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

def on_button_click():
    global nav

    try:
        num_polygons = int(entry_polygons.get())
        num_sides = int(entry_sides.get())
        num_to_show = int(slider_polygons.get())

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

        # Mostrar o botão de download após desenhar os polígonos
        button_download.grid(column=0, row=5, columnspan=2, pady=10)

    except ValueError as e:
        messagebox.showerror("Erro", str(e))

root = tk.Tk()
root.title("Desenho de Polígonos")

frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_polygons = ttk.Label(frame, text="Quantidade de Polígonos:")
label_polygons.grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)

entry_polygons = ttk.Entry(frame, width=10)
entry_polygons.grid(column=1, row=0, sticky=tk.W, padx=10, pady=10)
entry_polygons.insert(0, "10")

label_sides = ttk.Label(frame, text="Lados de cada Polígono:")
label_sides.grid(column=0, row=1, sticky=tk.W, padx=10, pady=10)

entry_sides = ttk.Entry(frame, width=10)
entry_sides.grid(column=1, row=1, sticky=tk.W, padx=10, pady=10)
entry_sides.insert(0, "5")

# Adicionando o slider para selecionar a quantidade de polígonos por página
label_slider = ttk.Label(frame, text="Polígonos por Página:")
label_slider.grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)

slider_polygons = tk.Scale(frame, from_=1, to=20, orient=tk.HORIZONTAL)
slider_polygons.set(5)
slider_polygons.grid(column=1, row=2, sticky=tk.W, padx=10, pady=10)

button_draw = ttk.Button(frame, text="Desenhar Polígonos", command=on_button_click)
button_draw.grid(column=0, row=3, columnspan=2, pady=20)

# Barra de progresso
progress_bar = ttk.Progressbar(frame, orient="horizontal", length=200, mode="determinate")
# Barra de progresso inicialmente oculta
progress_bar.grid_forget()

# Adicionando botão de download logo abaixo do botão de desenhar
button_download = ttk.Button(frame, text="Download", command=lambda: nav.on_download_clicked() if nav else None)
button_download.grid_forget()  # Esconde o botão inicialmente


root.mainloop()
