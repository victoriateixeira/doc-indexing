from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    words_list = search_by_word(word, instance)
    if len(words_list) != 0:
        for case in words_list:
            for ocorrencia in case["ocorrencias"]:
                ocorrencia.pop("conteudo")

        return words_list
    else:
        return []


def search_by_word(word, instance):
    words_list = []
    for file in instance._data:
        lines = txt_importer(file)
        occurencies = []
        for index, line in enumerate(lines):
            if word.lower() in line.lower():
                occurencies.append({"linha": index + 1, "conteudo": line})

        if len(occurencies) != 0:
            words_list.append(
                {
                    "palavra": word,
                    "arquivo": file,
                    "ocorrencias": occurencies,
                }
            )

    return words_list
