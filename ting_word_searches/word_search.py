from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    data = {
        "palavra": word,
        "arquivo": instance.search(0)["nome_do_arquivo"],
        "ocorrencias": [
            {'linha': i + 1}
            for i, file in enumerate(instance.search(0)["linhas_do_arquivo"])
            if word.lower() in file.lower()
        ]
    }

    result = []

    if len(data["ocorrencias"]) != 0:
        result.append(data)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
