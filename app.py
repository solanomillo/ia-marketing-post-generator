import os
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from dotenv import load_dotenv
from google import genai

# ==================================================
# CONFIGURACIÓN Y CONSTANTES
# ==================================================
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODELO_FLASH")
NUM_VARIANTS = 3

if not API_KEY:
    raise ValueError("No se encontró GEMINI_API_KEY en el archivo .env")

client = genai.Client(api_key=API_KEY)


# ==================================================
# LÓGICA DE NEGOCIO (IA)
# ==================================================
def build_prompt(product: str, features: str, tone: str, network: str) -> str:
    """
    Construye el prompt para generar múltiples variantes de un post.
    """
    return f"""
Actúa como un experto en marketing digital.

Escribe {NUM_VARIANTS} versiones DIFERENTES de un post para {network}.

Producto: {product}
Características: {features}
Tono: {tone}

Reglas:
- Cada versión debe ser creativa y distinta
- Usa emojis
- Incluye hashtags
- Numera las versiones como:
  Versión 1:
  Versión 2:
  Versión 3:
"""


def generate_posts(prompt: str) -> str:
    """
    Llama a la API de Gemini y devuelve el texto generado.
    """
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text


def save_content_to_file(content: str) -> None:
    """
    Abre un diálogo para guardar el contenido en un archivo.
    """
    if not content:
        messagebox.showinfo("Guardar", "No hay contenido para guardar")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    default_name = f"posts_ia_{timestamp}.txt"

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt")],
        initialfile=default_name,
        title="Guardar archivo"
    )

    if not file_path:
        return

    Path(file_path).write_text(content, encoding="utf-8")
    messagebox.showinfo("Guardado", "Archivo guardado correctamente")


# ==================================================
# FUNCIONES DE INTERFAZ
# ==================================================
def generate_button_handler() -> None:
    """
    Maneja el evento del botón "Generar Post".
    """
    product = entry_product.get().strip()
    features = text_features.get("1.0", tk.END).strip()
    tone = combo_tone.get()
    network = combo_network.get()

    if not product or not features:
        messagebox.showwarning(
            "Campos incompletos",
            "Por favor completa el producto y las características."
        )
        return

    prompt = build_prompt(product, features, tone, network)

    try:
        text_result.delete("1.0", tk.END)
        text_result.insert(tk.END, "⏳ Generando versiones...\n\n")
        root.update()

        result = generate_posts(prompt)

        text_result.delete("1.0", tk.END)
        text_result.insert(tk.END, result)

    except Exception as exc:  # pylint: disable=broad-except
        messagebox.showerror("Error", str(exc))


def copy_button_handler() -> None:
    """
    Copia el resultado al portapapeles.
    """
    content = text_result.get("1.0", tk.END).strip()

    if not content:
        messagebox.showinfo("Copiar", "No hay texto para copiar")
        return

    root.clipboard_clear()
    root.clipboard_append(content)
    messagebox.showinfo("Copiar", "Post copiado al portapapeles")


def save_button_handler() -> None:
    """
    Guarda el contenido generado en un archivo.
    """
    content = text_result.get("1.0", tk.END).strip()
    save_content_to_file(content)


# ==================================================
# INTERFAZ GRÁFICA (UI)
# ==================================================
root = tk.Tk()
root.title("Generador de Posts con IA")
root.geometry("720x660")

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)

# Producto
ttk.Label(main_frame, text="Producto").pack(anchor="w")
entry_product = ttk.Entry(main_frame)
entry_product.pack(fill="x", pady=5)

# Características
ttk.Label(main_frame, text="Características").pack(anchor="w")
text_features = tk.Text(main_frame, height=4)
text_features.pack(fill="x", pady=5)

# Tono
ttk.Label(main_frame, text="Tono").pack(anchor="w")
combo_tone = ttk.Combobox(
    main_frame,
    values=["Energético", "Profesional", "Emocional", "Juvenil"],
    state="readonly"
)
combo_tone.current(0)
combo_tone.pack(fill="x", pady=5)

# Red social
ttk.Label(main_frame, text="Red social").pack(anchor="w")
combo_network = ttk.Combobox(
    main_frame,
    values=["Instagram", "Facebook", "LinkedIn", "TikTok"],
    state="readonly"
)
combo_network.current(0)
combo_network.pack(fill="x", pady=5)

# Botones
buttons_frame = ttk.Frame(main_frame)
buttons_frame.pack(pady=15)

ttk.Button(
    buttons_frame,
    text="Generar 3 versiones",
    command=generate_button_handler
).pack(side="left", padx=5)

ttk.Button(
    buttons_frame,
    text="Copiar",
    command=copy_button_handler
).pack(side="left", padx=5)

ttk.Button(
    buttons_frame,
    text="Guardar archivo",
    command=save_button_handler
).pack(side="left", padx=5)

# Resultado
ttk.Label(main_frame, text="Resultado").pack(anchor="w")
text_result = tk.Text(main_frame, height=14)
text_result.pack(fill="both", expand=True)

root.mainloop()
