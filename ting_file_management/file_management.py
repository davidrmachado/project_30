import sys


def txt_importer(path_file):
    if not path_file.endswith('txt'):
        return print('Formato inválido', file=sys.stderr)
    try:
        with open(path_file, mode='r') as document:
            data = document.read()
            return data.split('\n')
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
