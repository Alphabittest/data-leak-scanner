# detectors/passwords.py
import re

def detectar(linha):
    senhas_fracas = [
        r'\b123456\b', r'\bpassword\b', r'\bqwerty\b', r'\badmin\b', r'\bsenha\b', r'\b1234\b', r'\b12345\b', r'\b123456\b'
    ]
    encontrados = []
    for senha in senhas_fracas:
        encontrados.extend(re.findall(senha, linha, re.IGNORECASE))
    return encontrados

