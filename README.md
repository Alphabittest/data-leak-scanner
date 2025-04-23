# data-leak-scanner
# 🔍 Sensitive Data Scanner

Um projeto em Python focado em **segurança da informação**, que realiza a varredura de arquivos em busca de **dados sensíveis**, como:

- 📧 E-mails
- 🧾 CPFs
- 💳 Cartões de crédito
- 🔐 Senhas fracas
- 🔑 Tokens de API (incluindo do GitHub, AWS e ChatGPT)

> Ideal para desenvolvedores, analistas de segurança ou qualquer pessoa que deseje garantir que arquivos não estejam vazando informações confidenciais.

---

## 🚀 Funcionalidades

- Detecta dados sensíveis usando expressões regulares (regex)
- Modularizado por tipo de dado
- Fácil de expandir e personalizar
- Roda direto pelo terminal
- Saída clara com linha e conteúdo encontrado

---

## 🛠️ Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/sensitive-data-scanner.git
cd sensitive-data-scanner
```

Crie o ambiente virtual (opcional):

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Como usar

Execute o scanner informando o caminho do arquivo que deseja analisar:

```bash
python scanner.py caminho/para/arquivo.txt
```

Exemplo:

```bash
python scanner.py test/exemplo_log.txt
```

---

## 🧪 Exemplo de saída

```bash
[ALERTA] E-mail encontrado na linha 4: contato@exemplo.com
[ALERTA] CPF encontrado na linha 7: 123.456.789-00
[ALERTA] Token de API encontrado na linha 12: sk-abc123456789...
[ALERTA] Cartão de crédito encontrado na linha 18: 1234 5678 9012 3456
[ALERTA] Senha fraca encontrada na linha 21: 123456
```

---

## 📁 Estrutura do projeto

```
sensitive-data-scanner/
│
├── scanner.py                 # Arquivo principal
├── requirements.txt
├── README.md
│
├── detectors/                 # Módulos de detecção
│   ├── __init__.py
│   ├── cpf.py
│   ├── email.py
│   ├── credit_card.py
│   ├── api_keys.py
│   └── passwords.py
│
└── test/
    └── exemplo_log.txt        # Exemplo de arquivo para teste
```

---

## 🧠 Tecnologias usadas

- Python 3.10+
- Regex (re)
- Terminal/CLI
- Estrutura modular com boas práticas

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

- Abrir issues com ideias ou bugs
- Criar PRs com melhorias
- Sugerir novos detectores


