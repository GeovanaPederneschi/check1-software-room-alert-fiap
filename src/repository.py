import json
import os

BASE_DIR = "data"


def carregar_json(nome_arquivo):
    caminho = os.path.join(BASE_DIR, nome_arquivo)
    if not os.path.exists(caminho):
        return []
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_json(nome_arquivo, dados):
    caminho = os.path.join(BASE_DIR, nome_arquivo)
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)