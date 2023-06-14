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
    print(str(out_dict))


def remove(instance):
    if not instance.__len__():
        return print("Não há elementos")

    file = instance.dequeue()
    print(f"Arquivo {file} removido com sucesso")


def file_metadata(instance, position):
    try:
        path_file = instance.search(position)
        out = txt_importer(path_file)
        out_dict = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(out),
            "linhas_do_arquivo": out,
        }
        print(str(out_dict))

    except IndexError:
        sys.stderr.write("Posição inválida")
