import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in instance.queue:
        if path_file == i['nome_do_arquivo']:
            return None

    file = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    instance.enqueue(data)
    print(data, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
