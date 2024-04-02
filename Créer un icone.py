import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def choisir_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        entry_image_path.delete(0, tk.END)
        entry_image_path.insert(0, file_path)

def convertir_en_ico():
    image_path = entry_image_path.get()
    if not image_path:
        messagebox.showerror("Erreur", "Veuillez sélectionner une image.")
        return
    
    icon_size = tuple(map(int, size_var.get().split(',')))
    img = Image.open(image_path)
    save_path = filedialog.asksaveasfilename(defaultextension=".ico", filetypes=[("Icon files", "*.ico")])
    if save_path:
        img.save(save_path, format='ICO', sizes=[icon_size])
        messagebox.showinfo("Succès", "L'image a été convertie en icône avec succès.")

root = tk.Tk()
root.title("Convertisseur d'Image en Icône")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry_image_path = tk.Entry(frame, width=40)
entry_image_path.pack(side=tk.LEFT, fill=tk.X, expand=True)

button_parcourir = tk.Button(frame, text="Parcourir", command=choisir_image)
button_parcourir.pack(side=tk.LEFT, padx=(10, 0))

size_var = tk.StringVar(value="32,32")  # Utilisez StringVar pour la taille
sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128)]
tk.Label(root, text="Taille de l'icône:").pack()

# Ajustement de la définition des Radiobuttons
for size in sizes:
    size_str = f"{size[0]},{size[1]}"  # Convertit le tuple en chaîne
    radio = tk.Radiobutton(root, text=f"{size[0]}x{size[1]}", variable=size_var, value=size_str)
    radio.pack(anchor=tk.W)

button_convertir = tk.Button(root, text="Convertir en .ICO", command=convertir_en_ico)
button_convertir.pack(pady=(10, 0))

root.mainloop()
