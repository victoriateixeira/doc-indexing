from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    words_list = []
    for file in instance._data:
        lines = txt_importer(file)
        occurencies = []
        for index, line in enumerate(lines):
            if word.lower() in line.lower():
                occurencies.append({"linha": index + 1})

        if len(occurencies) != 0:
            words_list.append(
                {
                    "palavra": word,
                    "arquivo": file,
                    "ocorrencias": occurencies,
                }
            )

    return words_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
