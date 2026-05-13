
import json
import datetime
from pathlib import Path

def registrar_accion(ususario: str, password: str):

    archivo = Path.home() / "Downloads" / "usuarios.json"
    print("Archivo se guardará en:", archivo)

    if not archivo.exists():
        print("Archivo no existe, creando uno nuevo...")
    
    with open(archivo, "w", encoding="utf-8") as u:
        json.dump({}, u)
    
    with open(archivo, "r", encoding="utf-8") as f:
        usuarios = json.load(f)



