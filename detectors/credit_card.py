#credit_card.py

import re

def detectar(linha):
    padrao = r'\b(?:\d[ -]*?){13,16}\b'
    return re.findall(padrao, linha)