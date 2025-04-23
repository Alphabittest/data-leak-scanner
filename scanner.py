# scanner.py
import os
import sys
from detectors import cpf, email, credit_card, api_keys, passwords

def escanear_arquivo(caminho):
    if not os.path.exists(caminho):
        print(f"[ERRO] Arquivo '{caminho}' não encontrado.")
        return

    with open(caminho, 'r', encoding='utf-8', errors='ignore') as f:
        for i, linha in enumerate(f, start=1):
            # Detectando CPF
            for alerta in cpf.detectar(linha):
                print(f"[ALERTA] CPF encontrado na linha {i}: {alerta}")
            
            # Detectando E-mail
            for alerta in email.detectar(linha):
                print(f"[ALERTA] E-mail encontrado na linha {i}: {alerta}")
            
            # Detectando Cartão de Crédito
            for alerta in credit_card.detectar(linha):
                print(f"[ALERTA] Cartão de crédito encontrado na linha {i}: {alerta}")
            
            # Detectando Tokens de API
            for alerta in api_keys.detectar(linha):
                print(f"[ALERTA] Token de API encontrado na linha {i}: {alerta}")
            
            # Detectando Senhas fracas
            for alerta in passwords.detectar(linha):
                print(f"[ALERTA] Senha fraca encontrada na linha {i}: {alerta}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python scanner.py <caminho_para_arquivo>")
    else:
        escanear_arquivo(sys.argv[1])
