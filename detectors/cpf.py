#cpf.py
import re

def detectar(linha):
    padrao = r'\b\d{3}[\.\-]?\d{3}[\.\-]?\d{3}[\.\-]?\d{2}\b'
    return re.findall(padrao, linha)