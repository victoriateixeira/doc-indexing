import sys


def txt_importer(path_file):
    news_list = []
    try:
        if not path_file.endswith(".txt"):
            sys.stderr.write("Formato inválido\n")

        with open(path_file, "r") as file:
            for line in file:
                news_list.append(line.strip())
        return news_list
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
