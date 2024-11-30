"""
main.py

Punto de entrada principal para el gestor de archivos basado en Python.
Este módulo utiliza `cli.py` para interpretar los comandos y delega la ejecución de las operaciones a `file_operations.py`.

Funcionalidades principales:
- Ejecutar comandos de usuario desde la línea de comandos.
- Proporcionar una interfaz intuitiva y clara para gestionar archivos y directorios.

Dependencias:
- cli.py: Maneja la interfaz de línea de comandos.
- file_operations.py: Contiene las funciones de manipulación de archivos y directorios.
"""

from cli import parse_arguments
from file_operations import create_file, read_file, delete_file, create_directory, delete_directory

def main():
    args = parse_arguments()

    if args.command == 'crear-archivo':
        create_file(args.filename)
    elif args.command == 'leer-archivo':
        read_file(args.filename)
    elif args.command == 'eliminar-archivo':
        delete_file(args.filename)
    elif args.command == 'crear-directorio':
        create_directory(args.dirname)
    elif args.command == 'eliminar-directorio':
        delete_directory(args.dirname)
    else:
        print("Comando no reconocido. Usa --help para más información.")

if __name__ == "__main__":
    main()