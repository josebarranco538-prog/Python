import json
from pathlib import Path

# ----------------------------
# 1. DEFINIR ARCHIVO EN DESCARGAS
# ----------------------------
archivo = Path.home() / "Downloads" / "usuarios.json"

print("Archivo se guardará en:", archivo)

# ----------------------------
# 2. CREAR ARCHIVO SI NO EXISTE
# ----------------------------
if not archivo.exists():
    print("Archivo no existe, creando uno nuevo...")
    
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump({}, f)

# ----------------------------
# 3. CARGAR USUARIOS
# ----------------------------
with open(archivo, "r", encoding="utf-8") as f:
    usuarios = json.load(f)

# ----------------------------
# 4. REGISTRO
# ----------------------------
print("\n=== REGISTRO ===")

username = input("Usuario: ").strip()
password = input("Contraseña: ").strip()

if username in usuarios:
    print("Ese usuario ya existe")
else:
    usuarios[username] = password

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4)

    print("Usuario guardado")

# ----------------------------
# 5. LOGIN
# ----------------------------
print("\n=== LOGIN ===")

user_login = input("Usuario: ").strip()
pass_login = input("Contraseña: ").strip()

if user_login in usuarios and usuarios[user_login] == pass_login:
    print("Login correcto")
else:
    print("Usuario o contraseña incorrectos")