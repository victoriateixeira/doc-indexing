from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    if path_file in instance._data:
        return
    out = txt_importer(path_file)
    out_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(out),
        "linhas_do_arquivo": out,
    }
    instance.enqueue(path_file)
    sys.stdout.write(str(out_dict))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
