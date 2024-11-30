"""
file_operations.py

Este módulo contiene funciones para realizar operaciones básicas en el sistema de archivos,
como crear, leer y eliminar archivos y directorios.

Funciones disponibles:
- create_file(filename): Crea un archivo vacío.
- read_file(filename): Lee y muestra el contenido de un archivo.
- delete_file(filename): Elimina un archivo.
- create_directory(dirname): Crea un directorio vacío.
- delete_directory(dirname): Elimina un directorio vacío.
"""

import os

# Variable global para el directorio base
BASE_DIR = os.path.join(os.getcwd(), "results")  


def create_file(filename):
    """
    Crea un archivo vacío con el nombre especificado.

    Parámetros:
    - filename (str): Nombre del archivo a crear.

    Excepciones:
    - Si el archivo ya existe, se mostrará un mensaje de error.
    - Si ocurre un error al crear, se mostrará un mensaje con detalles.
    
    Retorno:
    None
    """
    try:
        filepath = os.path.join(BASE_DIR, filename)
        with open(filepath, 'w') as f:
            pass
        print(f"Archivo '{filename}' creado exitosamente.")
    except FileExistsError:
        print(f"Error: El archivo '{filename}' ya existe.")
    except Exception as e:
        print(f"Error al crear el archivo '{filename}': {e}")


def read_file(filename):
    """
    Lee el contenido de un archivo y lo imprime en la consola.

    Parámetros:
    - filename (str): Nombre del archivo a leer. Puede incluir una ruta relativa o absoluta.

    Excepciones:
    - Si el archivo no existe, se mostrará un mensaje de error.
    - Si ocurre un error al leer, se mostrará un mensaje con detalles.

    Retorno:
    None
    """
    try:
        filepath = os.path.join(BASE_DIR, filename)
        with open(filepath, 'r') as f:
            content = f.read()
        print(f"Contenido de '{filename}':\n{content}")
        return content
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no existe.")
    except Exception as e:
        print(f"Error al leer el archivo '{filename}': {e}")


def delete_file(filename):
    """
    Elimina un archivo especificado.

    Parámetros:
    - filename (str): Nombre del archivo a eliminar. Puede incluir una ruta relativa o absoluta.

    Comportamiento:
    - Si el archivo no existe, se mostrará un mensaje de error.
    - Si ocurre un error al eliminar, se mostrará un mensaje con detalles.

    Retorno:
    None
    """
    try:
        filepath = os.path.join(BASE_DIR, filename)
        os.remove(filepath)
        print(f"Archivo '{filename}' eliminado exitosamente.")
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no existe.")
    except Exception as e:
        print(f"Error al eliminar el archivo '{filename}': {e}")


def create_directory(dirname):
    """
    Crea un directorio con el nombre especificado.

    Parámetros:
    - dirname (str): Nombre del directorio a crear. Puede incluir una ruta relativa o absoluta.

    Excepciones:
    - Si el directorio ya existe, no se realizará ninguna acción (por defecto de os.makedirs).
    - Si ocurre un error, se mostrará un mensaje con detalles.

    Retorno:
    None
    """
    try:
        filepath = os.path.join(BASE_DIR, dirname)
        os.makedirs(filepath, exist_ok=True)
        print(f"Directorio '{dirname}' creado exitosamente.")
    except FileExistsError:
        print(f"Error: El directorio '{dirname}' ya existe.")
    except Exception as e:
        print(f"Error al crear el directorio '{dirname}': {e}")


def delete_directory(dirname):
    """
    Elimina un directorio vacío especificado.

    Parámetros:
    - dirname (str): Nombre del directorio a eliminar. Puede incluir una ruta relativa o absoluta.

    Comportamiento:
    - Si el directorio no está vacío, se mostrará un mensaje de error.
    - Si el directorio no existe, se mostrará un mensaje de error.
    - Si ocurre un error, se mostrará un mensaje con detalles.

    Retorno:
    None
    """
    try:
        filepath = os.path.join(BASE_DIR, dirname)
        os.rmdir(filepath)
        print(f"Directorio '{dirname}' eliminado exitosamente.")
    except FileNotFoundError:
        print(f"Error: El directorio '{dirname}' no existe.")
    except OSError:
        print(f"Error: El directorio '{dirname}' no está vacío.")
    except Exception as e:
        print(f"Error al eliminar el directorio '{dirname}': {e}")

