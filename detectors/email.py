import re

def detectar(linha):
    padrao = r'[\w\.-]+@[\w\.-]+\.\w+'
    return re.findall(padrao, linha)