# detectors/api_keys.py
import re

def detectar(linha):
    padrao = r'\b(?:ghp_|AKIA|sk-)[A-Za-z0-9]{35}\b'
    return re.findall(padrao, linha)
