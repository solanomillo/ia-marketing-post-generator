# 🤖 Generador de Posts con IA – App de Escritorio

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-FFCC00?style=flat&logo=python&logoColor=black)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=flat&logo=google&logoColor=white)
![Desktop App](https://img.shields.io/badge/Desktop%20App-Windows-blue)

---

## 📌 Descripción

Aplicación de **escritorio desarrollada en Python** que permite generar múltiples versiones de posts para redes sociales utilizando **Inteligencia Artificial (Google Gemini)**.

La app está pensada para **marketers, emprendedores y creadores de contenido**, permitiendo generar textos creativos de forma rápida, copiarlos o guardarlos como archivos locales, sin necesidad de conocimientos técnicos.

---

## 🚀 Tecnologías utilizadas

- **Lenguaje:** Python 3.12+
- **Interfaz gráfica:** Tkinter (UI nativa)
- **IA Generativa:** Google Gemini API
- **Gestión de variables de entorno:** python-dotenv
- **Empaquetado:** PyInstaller
- **Buenas prácticas:** PEP 8, funciones modulares, código limpio

---

## ⚙️ Funcionalidades

✅ Generación de múltiples versiones de un post (3 variantes)  
✅ Selección de red social (Instagram, Facebook, LinkedIn, TikTok)  
✅ Selección de tono comunicacional  
✅ Uso de emojis y hashtags  
✅ Copiar resultado al portapapeles  
✅ Guardar los posts en archivos `.txt`  
✅ Interfaz simple, clara y profesional  
✅ Conversión a aplicación de escritorio (.exe)

---

## 🛠️ Instalación y configuración (modo desarrollo)

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/solanomillo/ia-marketing-post-generator.git
cd ia-marketing-post-generator
```

### 2️⃣ Crear y activar entorno virtual
```bash
python -m venv env
env\Scripts\activate      # Windows
source env/bin/activate   # Linux / Mac
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar variables de entorno
Crear un archivo .env en la raíz del proyecto:
```bash
GEMINI_API_KEY=tu_api_key_aqui
GEMINI_MODELO_FLASH=gemini-1.5-flash
```
### ▶️ Ejecutar la aplicación
```bash
python app.py
```
Se abrirá la interfaz gráfica de la aplicación.

---

## 🖥️ Convertir en aplicación de escritorio (.exe)

 ### 1️⃣ Generar el ejecutable
 ```bash
 pyinstaller --onefile --windowed --icon=ico.ico app.py
```

### 2️⃣ Resultado
El ejecutable final se generará en:

dist/app.exe

✅ El .exe puede ejecutarse sin tener Python instalado   
✅ Importante tener el archivo .env en la misma carpeta .exe para su correcto funcionamiento

---

## 📂 Estructura del proyecto
```bash
IA_WORK/
│
├── app.py                # Código principal de la app
├── .env                  # Variables de entorno (NO versionado)
├── requirements.txt      # Dependencias
├── ico.ico               # Icono de la aplicación
├── env/                  # Entorno virtual (NO versionado)
├── build/                # Archivos de PyInstaller (NO versionado)
├── dist/                 # Ejecutable final
├── .gitignore
└── README.md
```

## 🔐 Seguridad

✔️ API Key protegida con .env
✔️ .gitignore configurado correctamente
✔️ Sin credenciales hardcodeadas
✔️ Buenas prácticas para proyectos reales

