import os
import argparse

def create_file(filename):
    with open(filename, 'w') as f:
        pass

# ... otras funciones

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Gestor de archivos')
    parser.add_argument("-a")
    # ... agregar argumentos
    args = parser.parse_args()

    parser.add_argument('-o', '--operacion',
                        type=str,
                        choices=['suma', 'resta', 'multiplicacion'],
                        default='suma', required=False,
                        help='Operación a realizar con a y b')
    if args.operacion == 'suma':
        print(args.numero_a + args.numero_b)


    variables = vars(args)
    create_file(args.a)
    print(variables)

    # ... ejecutar la función correspondiente