import re

def validate_size(size: str):
    result = re.search(r"(\d+)x(\d+)", size)

    if result:
        return result.groups()
    
    raise Exception("Tamanho invalido, digite o tamanho no formato `numero`x`numero`")