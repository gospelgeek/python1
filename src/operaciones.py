import os

def create_file(filename):
    try:
        with open(filename, 'w') as f:
            pass
        print(f"Archivo '{filename}' creado exitosamente.")
    except Exception as e:
        print(f"Error al crear el archivo '{filename}': {e}")

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
        print(f"Contenido de '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no existe.")
    except Exception as e:
        print(f"Error al leer el archivo '{filename}': {e}")

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"Archivo '{filename}' eliminado exitosamente.")
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no existe.")
    except Exception as e:
        print(f"Error al eliminar el archivo '{filename}': {e}")

def create_directory(dirname):
    try:
        os.makedirs(dirname, exist_ok=True)
        print(f"Directorio '{dirname}' creado exitosamente.")
    except Exception as e:
        print(f"Error al crear el directorio '{dirname}': {e}")

def delete_directory(dirname):
    try:
        os.rmdir(dirname)
        print(f"Directorio '{dirname}' eliminado exitosamente.")
    except FileNotFoundError:
        print(f"Error: El directorio '{dirname}' no existe.")
    except OSError:
        print(f"Error: El directorio '{dirname}' no está vacío.")
    except Exception as e:
        print(f"Error al eliminar el directorio '{dirname}': {e}")
