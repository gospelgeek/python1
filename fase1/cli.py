"""
cli.py

Este módulo configura la interfaz de línea de comandos (CLI) para interactuar con el gestor de archivos. 
Usa argparse para recibir y procesar comandos del usuario, delegando la funcionalidad en el módulo `file_operations`.

Comandos disponibles:
- crear-archivo: Crea un archivo vacío.
- leer-archivo: Lee y muestra el contenido de un archivo.
- eliminar-archivo: Elimina un archivo existente.
- crear-directorio: Crea un directorio vacío.
- eliminar-directorio: Elimina un directorio vacío.
"""

import argparse
from file_operations import create_file, read_file, delete_file, create_directory, delete_directory

def parse_arguments():
    """
    Configura y analiza los argumentos de la línea de comandos usando argparse.

    Retorno:
    Namespace: Contiene los argumentos analizados.
    """
    parser = argparse.ArgumentParser(description='Gestor de archivos simple')
    subparsers = parser.add_subparsers(dest='command', help='Comando a ejecutar')

    # Subcomando para crear archivos
    parser_create_file = subparsers.add_parser('crear-archivo', help='Crea un archivo')
    parser_create_file.add_argument('filename', type=str, help='Nombre del archivo a crear')

    # Subcomando para leer archivos
    parser_read_file = subparsers.add_parser('leer-archivo', help='Lee un archivo')
    parser_read_file.add_argument('filename', type=str, help='Nombre del archivo a leer')

    # Subcomando para eliminar archivos
    parser_delete_file = subparsers.add_parser('eliminar-archivo', help='Elimina un archivo')
    parser_delete_file.add_argument('filename', type=str, help='Nombre del archivo a eliminar')

    # Subcomando para crear directorios
    parser_create_dir = subparsers.add_parser('crear-directorio', help='Crea un directorio')
    parser_create_dir.add_argument('dirname', type=str, help='Nombre del directorio a crear')

    # Subcomando para eliminar directorios
    parser_delete_dir = subparsers.add_parser('eliminar-directorio', help='Elimina un directorio')
    parser_delete_dir.add_argument('dirname', type=str, help='Nombre del directorio a eliminar')

    return parser.parse_args()
