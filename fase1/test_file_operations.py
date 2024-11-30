import os
import pytest
from file_operations import create_file, read_file, delete_file, create_directory, delete_directory, BASE_DIR


# Configuración para las pruebas
@pytest.fixture(scope="module")

def base_test_directory():
    """Crea un directorio temporal para pruebas y lo elimina al final."""
    test_dir = os.path.join(BASE_DIR, "test_results")    
    # Crea el directorio si no existe
    os.makedirs(test_dir, exist_ok=True)
    yield test_dir  # Proporciona el directorio para las pruebas
    # Limpieza: elimina el directorio de prueba y su contenido
"""    for root, dirs, files in os.walk(test_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(test_dir)
"""

def test_create_file(base_test_directory):
    """Prueba que create_file cree un archivo vacío en el directorio base."""
    filename = "test_file_SAMUEL.txt"
    create_file("test_results/"+filename)
    filepath = os.path.join(base_test_directory, filename)
    assert os.path.exists(filepath) and os.path.isfile(filepath)

def test_read_file(base_test_directory):
    """Prueba que read_file lea correctamente el contenido de un archivo."""
    filename = "test_file_to_read.txt"
    content = "Contenido de prueba"
    filepath = os.path.join(base_test_directory, filename)
    with open(filepath, 'w') as f:
        f.write(content)
    assert read_file(filepath) == content

def test_delete_file(base_test_directory):
    """Prueba que delete_file elimine un archivo correctamente."""
    filename = "test_file_to_delete.txt"
    filepath = os.path.join(base_test_directory, filename)
    create_file("test_results/"+filename)
    assert os.path.exists(filepath)
    delete_file("test_results/"+filename)
    assert not os.path.exists(filepath)

def test_create_directory(base_test_directory):
    """Prueba que create_directory cree un directorio correctamente."""
    dirname = "test_dir"
    dirpath = os.path.join(base_test_directory, dirname)
    create_directory("test_results/"+dirname)
    assert os.path.exists(dirpath) and os.path.isdir(dirpath)

def test_delete_directory(base_test_directory):
    """Prueba que delete_directory elimine un directorio correctamente."""
    dirname = "test_dir_to_delete"
    dirpath = os.path.join(base_test_directory, dirname)
    create_directory("test_results/"+dirname)
    assert os.path.exists(dirpath)
    delete_directory("test_results/"+dirname)
    assert not os.path.exists(dirpath)
